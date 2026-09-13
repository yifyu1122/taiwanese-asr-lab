import os
from dataclasses import dataclass
from typing import Any, Dict, List, Union
from datasets import Dataset
import librosa
import numpy as np
import pandas as pd
import torch
import unicodedata as ud
from transformers import (
    AutoModelForCTC,
    AutoProcessor,
    Trainer,
    TrainingArguments,
    set_seed
)


set_seed(42)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

if __name__ == "__main__":
  model_path = "model_path"
  processor = None
  model = None

  if os.path.exists(model_path):
    print(f"✅ 找到本機模型路徑: {model_path}")
    processor = AutoProcessor.from_pretrained(model_path, local_files_only=True)
    model = AutoModelForCTC.from_pretrained(model_path, local_files_only=True)

    if not torch.cuda.is_available():
      raise RuntimeError(
          "❌ 錯誤：未偵測到 NVIDIA GPU！本訓練需要 GPU 支援，程式已強制終止。"
    )

    device = torch.device("cuda")
    model.to(device)
    print(
        "🚀 成功啟動 GPU 加速！目前使用顯示卡:"
        f" {torch.cuda.get_device_name(0)}"
    )
    if processor is None or model is None:
        raise RuntimeError(
            "❌ 錯誤：Processor 或 Model 未成功初始化，程式已強制終止。"
        )
    print("✨ 模型與處理器成功載入！")

    # ==========================================
    # 💡 在這裡插入：Unicode tokenizer 超小型驗證
    # ==========================================
    print("\n=== Unicode tokenizer 超小型驗證 ===")
    tests = ["tá", "tá"]
    for x in tests:
        x_nfc = ud.normalize("NFC", x)
        print(f"\n原始：{repr(x)}")
        print(f"NFC ：{repr(x_nfc)}")
        print(f"原始 code points：{[f'U+{ord(c):04X}' for c in x]}")
        print(f"NFC code points：  {[f'U+{ord(c):04X}' for c in x_nfc]}")
        print(f"Token IDs：{processor(text=x_nfc).input_ids}")
    print("\n=== 驗證結束 ===")
    # ==========================================

  else:
    raise FileNotFoundError(f"❌ 找不到路徑: {model_path}")

  DATASET_DIR = "dataset_dir"
  print(f"📂 正在掃描目錄: {DATASET_DIR} ...")
  data = []

  for root, dirs, files in os.walk(DATASET_DIR):
    for file in files:
      if file.endswith(".wav"):
        file_path = os.path.join(root, file)
        label = os.path.splitext(file)[0]
        label = (
            label.replace("【白】", "").replace("【文】", "").strip()
        )
        data.append({"file": file_path, "text": label})

  df = pd.DataFrame(data)
  print(
      f"✅ 成功載入並清洗 {len(df)} 筆資料！範例標籤："
      f" {df['text'].iloc[0] if len(df) > 0 else '無資料'}"
  )

  if len(df) == 0:
    raise ValueError(
        f"❌ 錯誤：在 {DATASET_DIR} 底下找不到任何 .wav 音檔，請檢查路徑！"
    )


  @dataclass
  class DataCollatorCTCWithPadding:
    processor: Any

    def __call__(
        self,
        features: List[Dict[str, Union[List[int], torch.Tensor]]],
    ) -> Dict[str, torch.Tensor]:
      input_features = [
          {"input_values": feature["input_values"]} for feature in features
      ]
      label_features = [
          {"input_ids": feature["labels"]} for feature in features
      ]

      batch = self.processor.pad(
          input_features,
          padding=True,
          return_tensors="pt",
      )
      labels_batch = self.processor.pad(
          labels=label_features,
          padding=True,
          return_tensors="pt",
      )

      labels = labels_batch["input_ids"].masked_fill(
          labels_batch.attention_mask.ne(1), -100
      )
      batch["labels"] = labels
      return batch


  data_collator = DataCollatorCTCWithPadding(processor=processor)


  def prepare_dataset(batch, processor):
        audio_path = batch["file"]
        try:
            speech_array, _ = librosa.load(audio_path, sr=16000, mono=True)
            speech_array = speech_array.astype(np.float32)

            batch["input_values"] = (
                processor(speech_array, sampling_rate=16000)
                .input_values[0]
                .astype(np.float32)
            )
            # 強制 NFC 正規化，確保訓練標籤編碼一致
            text = ud.normalize("NFC", batch["text"])
            batch["labels"] = list(processor(text=text).input_ids)
            batch["is_valid"] = True
        except Exception as e:
            print(f"\n⚠️ 攔截到壞檔，自動略過: {os.path.basename(audio_path)} ({e})")
            batch["input_values"] = np.zeros(1, dtype=np.float32)
            batch["labels"] = [-100]
            batch["is_valid"] = False
        return batch


  print("🔄 正在轉換為 Dataset 格式並進行 16kHz 重採樣與特徵萃取...")
  hf_dataset = Dataset.from_pandas(df)

  hf_dataset = hf_dataset.map(
    prepare_dataset,
    remove_columns=hf_dataset.column_names,
    fn_kwargs={"processor": processor}, 
    num_proc=4,  
 )

  hf_dataset = hf_dataset.filter(lambda x: x["is_valid"])
  hf_dataset = hf_dataset.remove_columns(["is_valid"])

  print(
      "✨ 預處理大功告成！成功載入有效音訊"
      f" {len(hf_dataset)} 筆，隨時可以送入模型。"
  )

  training_args = TrainingArguments(
      output_dir=model_path,
      per_device_train_batch_size=16,
      gradient_accumulation_steps=2,
      learning_rate=1e-4,
      warmup_steps=200,
      num_train_epochs=4,
      fp16=True,
      logging_steps=20,
      save_steps=200,
      save_total_limit=2,
      push_to_hub=False,
      seed=42,
      data_seed=42,
  )

  trainer = Trainer(
      model=model,
      data_collator=data_collator,
      args=training_args,
      train_dataset=hf_dataset,
      processing_class=processor.feature_extractor,
  )

  print("🚀 開始進行模型訓練...")
  trainer.train()

  trainer.save_model(model_path)
  processor.save_pretrained(model_path)
  print("✨ 模型訓練完畢並已成功儲存至本地！")
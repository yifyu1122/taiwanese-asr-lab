import torch
import torchaudio
from transformers import AutoProcessor, AutoModelForCTC

# ==========================================
# 請自行設定模型與音檔路徑
# ==========================================
MODEL_PATH = "emlinking/wav2vec2-large-xls-r-300m-tsm-asr-v6"
AUDIO_PATH = "test.wav"

def main():
    print(f"Loading model: {MODEL_PATH}")
    processor = AutoProcessor.from_pretrained(MODEL_PATH)
    model = AutoModelForCTC.from_pretrained(MODEL_PATH)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    print(f"Loading audio: {AUDIO_PATH}")
    try:
        waveform, sample_rate = torchaudio.load(AUDIO_PATH)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return

    # 確保為單聲道
    if waveform.shape[0] > 1:
        waveform = torch.mean(waveform, dim=0, keepdim=True)
        
    original_length_seconds = waveform.shape[1] / sample_rate
        
    # 模型通常預期 16kHz 取樣率
    if sample_rate != 16000:
        resampler = torchaudio.transforms.Resample(sample_rate, 16000)
        waveform = resampler(waveform)
        sample_rate = 16000

    inputs = processor(
        waveform.squeeze(),
        sampling_rate=sample_rate,
        return_tensors="pt"
    )
    
    inputs = {k: v.to(device) for k, v in inputs.items()}

    print("Running inference...")
    with torch.no_grad():
        outputs = model(**inputs)
        
    # 取出第一個 batch 的 logits
    logits = outputs.logits[0]
    
    # 找出每個 frame 分數最高的 token ID
    predicted_ids = torch.argmax(logits, dim=-1).tolist()
    
    # 對應回字元 (token)
    tokens = processor.tokenizer.convert_ids_to_tokens(predicted_ids)
    
    num_frames = len(tokens)
    
    # 計算每個 frame 代表的時間長度
    time_per_frame = original_length_seconds / num_frames if num_frames > 0 else 0
    
    print("\n=== Audio & Frame Information ===")
    print(f"Audio Length: {original_length_seconds:.3f} seconds")
    print(f"Total Frames: {num_frames}")
    print(f"Time per Frame: {time_per_frame:.4f} seconds")
    
    print("\n=== Token Timeline (Non-pad only) ===")
    pad_token = processor.tokenizer.pad_token
    for i, token in enumerate(tokens):
        # 為了版面乾淨，這裡我們只印出非空白(pad)的 token
        if token != pad_token:
            timestamp = i * time_per_frame
            print(f"[{timestamp:.3f}s] Frame {i:3d}: {token}")

if __name__ == "__main__":
    main()

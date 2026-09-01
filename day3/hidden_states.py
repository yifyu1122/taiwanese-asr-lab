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

    print("Running inference and extracting hidden states...")
    with torch.no_grad():
        # 設定 output_hidden_states=True 才能取得中間層資訊
        outputs = model(**inputs, output_hidden_states=True)
        
    # outputs.hidden_states 是一個 tuple，包含 embedding 層與各層 transformer 的輸出
    # 我們取最後一層 [-1]
    last_hidden_state = outputs.hidden_states[-1]
    
    print("\n=== Hidden States Information ===")
    print(f"Shape: {last_hidden_state.shape}")
    print(f"Batch Size: {last_hidden_state.shape[0]}")
    print(f"Time Steps (Frames): {last_hidden_state.shape[1]}")
    print(f"Hidden Dimension: {last_hidden_state.shape[2]}")

if __name__ == "__main__":
    main()

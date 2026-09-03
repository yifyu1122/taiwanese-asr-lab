import unicodedata
from transformers import AutoProcessor

def main():
    print("Loading v6 Tokenizer (this may take a moment)...")
    model_name = "emlinking/wav2vec2-large-xls-r-300m-tsm-asr-v6"
    
    # 載入模型對應的 Tokenizer
    processor = AutoProcessor.from_pretrained(model_name)
    tokenizer = processor.tokenizer
    
    # 準備測試字串：tá
    text = "tá"
    
    # 利用內建的 unicodedata 強制轉換成 NFC 與 NFD
    text_nfc = unicodedata.normalize('NFC', text)
    text_nfd = unicodedata.normalize('NFD', text)
    
    print("\n=== Unicode 底層編碼 (Code Points) ===")
    print("這裡印出字串在電腦底層的 16 進位編碼：")
    print(f"NFC: {[hex(ord(c)) for c in text_nfc]}")
    print(f"NFD: {[hex(ord(c)) for c in text_nfd]}")
    
    print("\n=== Tokenizer 轉換結果 (Token IDs) ===")
    print("這裡印出 Tokenizer 把字串轉換給模型看的 ID 陣列：")
    print(f"NFC Token IDs: {tokenizer(text_nfc).input_ids}")
    print(f"NFD Token IDs: {tokenizer(text_nfd).input_ids}")

if __name__ == "__main__":
    main()

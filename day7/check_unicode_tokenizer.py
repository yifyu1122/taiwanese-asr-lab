import unicodedata
from transformers import AutoProcessor


def show_unicode_info(label, text):
    print(f"\n=== {label} ===")
    print(f"文字: {text}")
    print(f"Code Points: {[f'U+{ord(c):04X}' for c in text]}")


def main():
    print("Loading v6 Tokenizer (this may take a moment)...")

    model_name = "emlinking/wav2vec2-large-xls-r-300m-tsm-asr-v6"

    # 載入 v6 模型對應的 Processor
    processor = AutoProcessor.from_pretrained(model_name)
    tokenizer = processor.tokenizer

    # 測試字串
    text = "tá"

    # 建立 NFC 與 NFD
    text_nfc = unicodedata.normalize("NFC", text)
    text_nfd = unicodedata.normalize("NFD", text)

    print("\n=== Unicode 底層編碼 ===")

    show_unicode_info("NFC", text_nfc)
    show_unicode_info("NFD", text_nfd)

    print("\n=== Tokenizer 結果 ===")

    nfc_ids = tokenizer(text_nfc).input_ids
    nfd_ids = tokenizer(text_nfd).input_ids

    print(f"NFC Token IDs: {nfc_ids}")
    print(f"NFD Token IDs: {nfd_ids}")

    print("\n=== 比較結果 ===")

    if nfc_ids == nfd_ids:
        print("結果：NFC 與 NFD 得到相同的 Token IDs。")
    else:
        print("結果：NFC 與 NFD 得到不同的 Token IDs。")


if __name__ == "__main__":
    main()

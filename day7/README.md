# Day 7｜Unicode NFC / NFD Tokenizer 測試

這個資料夾放的是 Day 7 文章中 Unicode 實驗的簡化公開重現版。

我當初在本機使用了幾支不同的檢查程式，確認 `[UNK]`、NFC、NFD 和 Token ID 之間的關係：

- `nfcdCheck.py`：掃描訓練集檔名，統計 NFC、NFD，以及需要修正的資料。
- `tokenizerCheck.py`：檢查 V3 tokenizer 的詞表，確認 `[UNK]` 和其他特殊 token 是否存在。
- `tokenizerCheckSame.py`：把看起來相同的臺羅字串分別轉成 NFC、NFD，再比較它們的 Code Point 與 Token ID。

這些原始程式使用的是本機資料集與不同版本的模型，因此沒有全部放進公開版。

## 公開重現程式

### `check_unicode_tokenizer.py`

這支程式使用：

`emlinking/wav2vec2-large-xls-r-300m-tsm-asr-v6`

對應的 tokenizer，將 `tá` 分別轉成 NFC 與 NFD，並印出：

1. Unicode Code Point
2. Tokenizer 轉換後的 Token ID

不需要 WAV，也不會進行 ASR 推論或重新訓練模型。

## 執行方式

先安裝：

```bash
python -m pip install transformers
````

再執行：

```bash
python check_unicode_tokenizer.py
```

第一次執行需要網路下載模型對應的 Processor／Tokenizer。

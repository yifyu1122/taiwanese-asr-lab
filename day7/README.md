# Day 7｜Unicode NFC / NFD Tokenizer 測試

這個資料夾放的是 Day 7 文章裡 Unicode 實驗的**簡化後公開重現版**。

我當初在本機其實用了三支不同的檢查程式，一路確認 `[UNK]`、NFC、NFD 和 Token ID 之間到底發生了什麼：

- `nfcdCheck.py`：掃描訓練集檔名，統計 NFC、NFD，以及需要修正的資料。
- `tokenizerCheck.py`：檢查 V3 tokenizer 的詞表，確認 `[UNK]` 和其他特殊 token 是否存在。
- `tokenizerCheckSame.py`：把看起來相同的台羅字串分別轉成 NFC、NFD，再比較它們的 Code Point 與 Token ID。

這些原始檢查程式是我專題資料夾裡的 debug 程式，使用的是本機資料集與不同版本的模型。為了讓讀者不用準備整個專題環境，我把其中最核心的驗證整理成下面這支獨立程式。

## 公開重現程式

### `check_unicode_tokenizer.py`

這支程式會載入前面實驗使用的台語 ASR tokenizer，接著把 `tá` 轉成 NFC 與 NFD 兩種形式，再印出：

1. 兩種形式的 Unicode Code Point
2. 兩種形式送進 tokenizer 後得到的 Token ID

它不需要 WAV，也不會重新訓練模型，只是把我當初檢查問題的核心步驟整理成一個可以直接重現的小實驗。

## 執行方式

請先安裝 `transformers`：

```bash
python -m pip install transformers
```

再執行：

```bash
python check_unicode_tokenizer.py
```

第一次執行需要網路，程式會從 Hugging Face 載入 tokenizer；之後如果模型已經存在本機快取，就不需要重新下載完整內容。

你應該會看到 NFC 與 NFD 的 Code Point 序列不同，送進 tokenizer 後得到的 Token ID 也可能不同。

這個結果本身不是在宣稱所有 `[UNK]` 都一定由 Unicode 造成，而是讓我們先親眼看到：**人眼看起來一樣的台羅，模型收到的輸入不一定一樣。**

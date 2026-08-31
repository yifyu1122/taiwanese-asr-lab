# Day 2｜Taiwanese ASR Model Test

這個資料夾包含鐵人賽 Day 2 實際測試的兩個台語 ASR 模型：

1. **Breeze ASR 26**
   `MediaTek-Research/Breeze-ASR-26`

2. **v6 台語 ASR**
   `emlinking/wav2vec2-large-xls-r-300m-tsm-asr-v6`

這次測試不是單純比較哪個模型的 Accuracy 最高，而是實際觀察不同 ASR 模型的輸出形式，以及這些輸出是否適合後續的台語發音分析。

## Breeze ASR 26

Breeze ASR 26 是 MediaTek Research 開發的台語語音辨識模型，基於 Whisper-large-v2，並針對台語語音進行微調。

這裡使用 Hugging Face Transformers 直接載入模型，測試它能否將 WAV 語音轉換成文字。


Breeze ASR 26 主要輸出的是文字結果，因此適合用來觀察一般 ASR 模型如何辨識同一段台語語音。

## v6 台語 ASR

v6 是以 Wav2Vec2 XLS-R 300M 為基礎微調的台語 ASR，採用 CTC 架構，直接輸出臺羅拼音。

除了最後的辨識結果之外，也可以取得模型輸出的 frame-level logits，因此可以進一步研究 token probability、時間對齊，以及後續的發音分析。


## 安裝

請先建立 Python 環境，然後安裝所需套件：

```bash
pip install -r requirements.txt
```

本範例使用 PyTorch 2.4.1 與 torchaudio 2.4.1。若需要 NVIDIA GPU 加速，請依照自己的 CUDA 環境安裝對應的 PyTorch 版本。

第一次執行程式時，Transformers 會從 Hugging Face 下載模型。

由於 Breeze ASR 26 的模型檔案較大，第一次下載可能需要較長時間，請確認磁碟空間與網路連線。

## 執行

直接執行對應的 Python 程式：

```bash
python test_breeze.py
```

```bash
python test_v6.py
```

兩個程式預設都會讀取目前資料夾中的：

```text
mystery_box.wav
```

請將測試音檔放在 `day2` 資料夾內。

## WAV 盲盒

Day 2 文章中的測試音檔會作為 WAV 盲盒使用。

我不會先公布音檔裡面錄的是什麼音。

你可以把同一個 WAV 分別交給 Breeze ASR 26 和 v6，觀察兩個模型最後會輸出什麼結果。

至於答案是什麼？

自己跑看看。


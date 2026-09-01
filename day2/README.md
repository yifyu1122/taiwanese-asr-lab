# Day 2｜Taiwanese ASR Model Test

這個資料夾包含了鐵人賽 Day 2 提到的兩個台語 ASR 模型的實際執行範例：

1. **Breeze ASR 26** (`MediaTek-Research/Breeze-ASR-26`)
2. **v6 台語 ASR** (`emlinking/wav2vec2-large-xls-r-300m-tsm-asr-v6`)

## 模型用途差異

**Breeze ASR 26**
- 基於 Whisper-large-v2 架構，並經過約 10,000 小時台語合成語音微調。
- 是一套強大的大規模台語 ASR 模型。
- 辨識結果主要以**中文漢字**呈現。
- 官方提供了很好的封裝，可以直接透過 Hugging Face Transformers 的 `pipeline` 快速測試語音轉文字。

**v6 ASR**
- 基於 Wav2Vec2 XLS-R 300M 微調。
- 使用 CTC 架構，直接輸出**臺羅拼音**。
- 能夠取得 frame-level 的 logits 資訊。
- 非常適合用於後續研究 token probability、時間對齊 (time alignment) 以及發音分析等 downstream tasks。

## 安裝

請確認你已經安裝好 Python 環境，接著執行：

```bash
pip install -r requirements.txt
```

本範例使用 PyTorch 2.4.1 與 torchaudio 2.4.1。
若需要 NVIDIA GPU 加速，請依照自己的 CUDA 環境安裝對應的 PyTorch 版本。

第一次執行時，Transformers 會自動從 Hugging Face
下載模型。由於模型檔案較大，第一次下載可能需要一些時間。

## 執行方式

這兩個程式都可以透過命令列 (CLI) 直接指定你要測試的 WAV 音檔進行辨識。

### 測試 Breeze ASR 26 模型

```bash
python test_breeze.py test.wav
```

### 測試 v6 模型

```bash
python test_v6.py test.wav
```

程式會自動判斷是否有 GPU 可以加速推論，沒有的話也能使用 CPU 執行。

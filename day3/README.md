# Day 3｜模型內部輸出觀察

這個資料夾包含了鐵人賽 Day 3 文章中，用來觀察 wav2vec2 模型內部輸出的兩個小實驗。

我們主要使用的是 `emlinking/wav2vec2-large-xls-r-300m-tsm-asr-v6` 這個台語 ASR 模型。

## 包含的實驗程式

### 1. `hidden_states.py`
輸入一個音檔，程式會透過設定 `output_hidden_states=True` 來取得模型最後一層的 Hidden States。
執行後會印出 Hidden States 的 Tensor Shape 等基本資訊（例如 Batch Size, Time Steps, Hidden Dimension），讓你了解「一個音檔進去後，模型最後一層 Hidden States 長什麼樣子」。

### 2. `logits_frame_analysis.py`
輸入一個音檔，程式會觀察模型在推論過程中產生的 logits，並找出每個 frame (時間步) 分數最高的 token。
執行後會印出音檔長度、總 frame 數，以及每個非空白 (non-pad) token 出現的時間軸，觀察模型在不同時間點偏向哪個字元。

## 執行方式

請先在程式碼開頭修改為你自己的音檔路徑，例如：

```python
# ==========================================
# 請自行設定模型與音檔路徑
# ==========================================
MODEL_PATH = "emlinking/wav2vec2-large-xls-r-300m-tsm-asr-v6"
AUDIO_PATH = "你的音檔路徑.wav"
```

修改完成後，即可直接透過 Python 執行：

```bash
python hidden_states.py
python logits_frame_analysis.py
```

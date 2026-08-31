import torch
import torchaudio
from transformers import AutoProcessor, AutoModelForCTC

model_name = "emlinking/wav2vec2-large-xls-r-300m-tsm-asr-v6"

processor = AutoProcessor.from_pretrained(model_name)
model = AutoModelForCTC.from_pretrained(model_name)

waveform, sample_rate = torchaudio.load("mystery_box.wav")

inputs = processor(
    waveform.squeeze(),
    sampling_rate=sample_rate,
    return_tensors="pt"
)

with torch.no_grad():
    outputs = model(**inputs)

predicted_ids = torch.argmax(outputs.logits, dim=-1)
result = processor.batch_decode(predicted_ids)

print(result)
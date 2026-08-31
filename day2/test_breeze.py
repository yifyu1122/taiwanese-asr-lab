from transformers import pipeline

asr = pipeline(
    "automatic-speech-recognition",
    model="MediaTek-Research/Breeze-ASR-26"
)

result = asr("mystery_box.wav")

print(result["text"])
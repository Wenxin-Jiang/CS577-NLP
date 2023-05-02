---
language: 
  - uk
license: "cc-by-nc-sa-4.0"
datasets:
- mozilla-foundation/common_voice_10_0
---

🇺🇦 Join Ukrainian Speech Recognition Community - https://t.me/speech_recognition_uk

⭐ See other Ukrainian models - https://github.com/egorsmkv/speech-recognition-uk

This model was trained using the base model https://huggingface.co/fav-kky/wav2vec2-base-cs-80k-ClTRUS (pre-trained from 80 thousand hours of Czech speech)

This model has apostrophes and hyphens.

Metrics:

| Dataset | CER | WER |
|-|-|-|
| CV7 (no LM) |  0.0978 | 0.4191 |
| CV7 (with LM) | 0.0418 | 0.13 |
| CV10 (no LM) | 0.0946 | 0.412 |
| CV10 (with LM) | 0.0328 | 0.0981 |

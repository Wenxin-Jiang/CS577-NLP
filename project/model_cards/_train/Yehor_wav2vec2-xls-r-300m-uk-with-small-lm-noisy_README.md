---
language: 
  - uk
license: "apache-2.0"
datasets:
- mozilla-foundation/common_voice_10_0
---

🇺🇦 Join Ukrainian Speech Recognition Community - https://t.me/speech_recognition_uk

⭐ See other Ukrainian models - https://github.com/egorsmkv/speech-recognition-uk

This model has been trained on noisy data in order to make the acoustic model robust to noisy audio data.

This model has apostrophes and hyphens.

The language model is trained on the texts of the Common Voice dataset, which is used during training.

Special thanks for noised data to **Dmytro Chaplynsky**, https://lang.org.ua

Noisy dataset:

- Transcriptions: https://www.dropbox.com/s/ohj3y2cq8f4207a/transcriptions.zip?dl=0
- Audio files: https://www.dropbox.com/s/v8crgclt9opbrv1/data.zip?dl=0

Metrics:

| Dataset | CER | WER |
|-|-|-|
| CV10 (no LM) | 0.0515 | 0.2617 |
| CV10 (with LM) | 0.0148 | 0.0524 |

Metrics on noisy data with [standard model](https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-small-lm):

| Dataset | CER | WER |
|-|-|-|
| CV10 (no LM) | 0.1064 | 0.3926 |
| CV10 (with LM) | 0.0497 | 0.1265 |

More:

- The same model, but trained on raw Common Voice data: https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-small-lm

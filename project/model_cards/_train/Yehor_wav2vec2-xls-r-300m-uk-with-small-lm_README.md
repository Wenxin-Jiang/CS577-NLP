---
language: 
  - uk
license: "apache-2.0"
datasets:
- mozilla-foundation/common_voice_10_0
---

🇺🇦 Join Ukrainian Speech Recognition Community - https://t.me/speech_recognition_uk

⭐ See other Ukrainian models - https://github.com/egorsmkv/speech-recognition-uk

This model has apostrophes and hyphens.

The language model is trained on the texts of the Common Voice dataset, which is used during training.

Metrics:

| Dataset | CER | WER |
|-|-|-|
| CV7 (no LM) |  0.0432 | 0.2288 |
| CV7 (with LM) | 0.0169 | 0.0706 |
| CV10 (no LM) | 0.0412 | 0.2206 |
| CV10 (with LM) | 0.0118 | 0.0463 |

More:

- The same model, but trained on noisy data: https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-with-small-lm-noisy
- Traced JIT version: https://huggingface.co/Yehor/wav2vec2-xls-r-300m-uk-traced-jit

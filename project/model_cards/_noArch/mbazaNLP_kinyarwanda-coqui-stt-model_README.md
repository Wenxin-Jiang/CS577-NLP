---
language: "rw"
thumbnail:
pipeline_tag: automatic-speech-recognition
tags:
- Coqui
- Deepspeech
- LSTM
license: "apache-2.0"
datasets:
- commonvoice
metrics:
- wer
---

**Model card - Kinyarwanda coqui STT model**

**Model details**
- Kinyarwanda Speech to text model
- Developed by [Digital Umuganda](digitalumuganda.com)
- Model based from: Baidu Deepspeech end to end RNN model
- paper: [deepspeech end to end STT](https://arxiv.org/pdf/1412.5567.pdf)
- Documentation on model: [deepspeech documentation](https://deepspeech.readthedocs.io/)
- License: Mozilla 2.0 License
- Feedback on the model: samuel@digitalumuganda.com

**Intended use cases**
- Intended to be used for 
  - simple keyword spotting
  - simple transcribing
  - transfer learning for better kinyarwanda and african language models
- Intended to be used by:
  - App developpers
  - various organizations who want to transcribe kinyarwanda recordings
  - ML researchers
  - other researchers in Kinyarwanda and tech usage in kinyarwanda (e.g. Linguists, journalists)
- Not intended to be used as:
  - a fully fledged voice assistant
  - voice recognition application 
  - Multiple languages STT
  - language detection 
  
**Factors**
- Anti-bias: these are bias that can influence the accuracy of the model
  - Gender
  - accents and dialects
  - age
- Voice quality: factors that can influence the accuracy of the model
  - Background noise
  - short sentences
- Voice format: voices must be converted to the wav format
  - wav format
  
**Metrics**
- word error rate on the Common Voice Kinyarwanda test set

|Test Corpus|WER|
|-----------|---|
|Common Voice|39.1\%|

**Training data**
- [common voice crowdsource website](https://commonvoice.mozilla.org/en/datasets)

**Evaluation data**
- [common voice crowdsource website](https://commonvoice.mozilla.org/en/datasets)

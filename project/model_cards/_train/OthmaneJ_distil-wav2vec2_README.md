---
language: en
datasets:
- librispeech_asr
tags:
- speech
- audio
- automatic-speech-recognition
license: apache-2.0
---

# Distil-wav2vec2 
This model is a distilled version of the wav2vec2 model (https://arxiv.org/pdf/2006.11477.pdf). This model is 45% times smaller and twice as fast as the original wav2vec2 base model.

# Evaluation results
This model achieves the following results (speed is mesured for a batch size of 64): 

|Model| Size| WER Librispeech-test-clean |WER Librispeech-test-other|Speed on cpu|speed on gpu| 
|----------| ------------- |-------------|-----------| ------|----|
|Distil-wav2vec2| 197.9 Mb | 0.0983 | 0.2266|0.4006s| 0.0046s|
|wav2vec2-base| 360 Mb | 0.0389 | 0.1047|0.4919s| 0.0082s|


# Usage
notebook (executes seamlessly on google colab) at https://github.com/OthmaneJ/distil-wav2vec2

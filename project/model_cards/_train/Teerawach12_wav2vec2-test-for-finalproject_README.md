---
language: th
datasets:
- common_voice
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: XLSR Wav2Vec2 Large Thai by Sakares
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice th
      type: common_voice
      args: th  
    metrics:
       - name: Test WER
         type: wer
         value: 41.263
---

# Wav2Vec2-Large-XLSR-53-Thai

**Test Result**: 41.263 %

**Datasets**
It is increase new data from The Common Voice V8 dataset to Common Voice V7 dataset or remove all data in Common Voice V7 dataset before split Common Voice V8 then add CommonVoice V7 dataset back to dataset.

It use ekapolc/Thai_commonvoice_split script for split Common Voice dataset.

**Models**
This model was finetune wav2vec2-large-xlsr-53 model with Thai Common Voice V8 dataset and It use pre-tokenize with deepcut.tokenize.

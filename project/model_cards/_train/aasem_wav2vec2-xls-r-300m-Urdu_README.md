--- 
datasets: 
  - 
    common_voice: ~
language: 
  - 
    ur: ~
library_name: 
  transformers: ~
license: 
  mit: ~
metrics: 
  - 
    wer: ~
model-index: 
  - 
    name: 
      wav2vec2-xls-r-300m-Urdu: ~
    results: 
      - 
        task: 
          dataset: 
            args: 
              ur: ~
            name: 
              : "common_voice"
              : ~
            type: 
              common_voice: ~
          metrics: 
            - 
              type: 
                wer: ~
              value: 
                0.2459: ~
            - 
              type: 
                cer: ~
              value: 
                0.0691: ~
          type: 
            automatic-speech-recognition: ~
tags: 
  - 
    audio: ~
  - 
    automatic-speech-recognition: ~
  - 
    speech: ~

Finetuning of [Facebook's 300M model](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on Common Voice 8.0 Urdu dataset
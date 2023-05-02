---
language:
- bn
license: apache-2.0
tags:
- automatic-speech-recognition
- hf-asr-leaderboard
- openslr_SLR53
- robust-speech-event
datasets:
- openslr
- SLR53
- Harveenchadha/indic-text
metrics:
- wer
- cer
model-index:
- name: Tahsin-Mayeesha/wav2vec2-bn-300m
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: openslr
      name: Open SLR
      args: SLR66
    metrics:
    - type: wer
      value: 0.31104373941386626
      name: Test WER
    - type: cer
      value: 0.07263099973420006
      name: Test CER
    - type: wer
      value: 0.17776164652632478
      name: Test WER with lm
    - type: cer
      value: 0.04394092712884769
      name: Test CER with lm
---

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the OPENSLR_SLR53 - bengali dataset.
It achieves the following results on the evaluation set. 

Without language model : 
- Wer: 0.3110
- Cer : 0.072

With 5 gram language model trained on [indic-text](https://huggingface.co/datasets/Harveenchadha/indic-text/tree/main) dataset : 
- Wer: 0.17776
- Cer : 0.04394
  

Note : 10% of a total 218703 samples have been used for evaluation. Evaluation set has 21871 examples. Training was stopped after 30k steps. Output predictions are available under files section.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 16
- eval_batch_size: 16
- gradient_accumulation_steps: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0

Note : Training and evaluation script modified from https://huggingface.co/chmanoj/xls-r-300m-te and https://github.com/huggingface/transformers/tree/master/examples/research_projects/robust-speech-event. 
Bengali speech data was not available from common voice or librispeech multilingual datasets, so OpenSLR53 has been used.

Note 2 : Minimum audio duration of 0.1s has been used to filter the training data which excluded may be 10-20 samples. 
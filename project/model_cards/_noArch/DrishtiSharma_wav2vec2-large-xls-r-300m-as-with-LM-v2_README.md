---
language:
- as
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- as
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-as-with-LM-v2
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: hsb
    metrics:
    - name: Test WER
      type: wer
      value: []
    - name: Test CER
      type: cer
      value: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->



### Note: Files are missing. Probably, didn't get (git)pushed properly.  :(

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1679
- Wer: 0.5761

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000111
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 300
- num_epochs: 200
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 8.3852        | 10.51  | 200  | 3.6402          | 1.0    |
| 3.5374        | 21.05  | 400  | 3.3894          | 1.0    |
| 2.8645        | 31.56  | 600  | 1.3143          | 0.8303 |
| 1.1784        | 42.1   | 800  | 0.9417          | 0.6661 |
| 0.7805        | 52.62  | 1000 | 0.9292          | 0.6237 |
| 0.5973        | 63.15  | 1200 | 0.9489          | 0.6014 |
| 0.4784        | 73.67  | 1400 | 0.9916          | 0.5962 |
| 0.4138        | 84.21  | 1600 | 1.0272          | 0.6121 |
| 0.3491        | 94.72  | 1800 | 1.0412          | 0.5984 |
| 0.3062        | 105.26 | 2000 | 1.0769          | 0.6005 |
| 0.2707        | 115.77 | 2200 | 1.0708          | 0.5752 |
| 0.2459        | 126.31 | 2400 | 1.1285          | 0.6009 |
| 0.2234        | 136.82 | 2600 | 1.1209          | 0.5949 |
| 0.2035        | 147.36 | 2800 | 1.1348          | 0.5842 |
| 0.1876        | 157.87 | 3000 | 1.1480          | 0.5872 |
| 0.1669        | 168.41 | 3200 | 1.1496          | 0.5838 |
| 0.1595        | 178.92 | 3400 | 1.1721          | 0.5778 |
| 0.1505        | 189.46 | 3600 | 1.1654          | 0.5744 |
| 0.1486        | 199.97 | 3800 | 1.1679          | 0.5761 |


### Framework versions

- Transformers 4.16.1
- Pytorch 1.10.0+cu111
- Datasets 1.18.2
- Tokenizers 0.11.0

---
language:
- fi
license: apache-2.0
tags:
- generated_from_trainer
- automatic-speech-recognition
- robust-speech-event
- hf-asr-leaderboard
model-index:
- name: wav2vec2-xlsr-fi-lm-1B
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xlsr-fi-lm-1B

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the common voice train/dev/other datasets.
It achieves the following results on the evaluation set without language model:
- Loss: 0.1853
- Wer: 0.2205

With language model:
- Wer: 0.1026


## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.8158        | 0.67  | 400  | 0.4835          | 0.6310 |
| 0.5679        | 1.33  | 800  | 0.4806          | 0.5538 |
| 0.6055        | 2.0   | 1200 | 0.3888          | 0.5083 |
| 0.5353        | 2.67  | 1600 | 0.3258          | 0.4365 |
| 0.4883        | 3.33  | 2000 | 0.3313          | 0.4204 |
| 0.4513        | 4.0   | 2400 | 0.2924          | 0.3904 |
| 0.3753        | 4.67  | 2800 | 0.2593          | 0.3608 |
| 0.3478        | 5.33  | 3200 | 0.2832          | 0.3551 |
| 0.3796        | 6.0   | 3600 | 0.2495          | 0.3402 |
| 0.2556        | 6.67  | 4000 | 0.2342          | 0.3106 |
| 0.229         | 7.33  | 4400 | 0.2181          | 0.2812 |
| 0.205         | 8.0   | 4800 | 0.2041          | 0.2523 |
| 0.1654        | 8.67  | 5200 | 0.2015          | 0.2416 |
| 0.152         | 9.33  | 5600 | 0.1942          | 0.2294 |
| 0.1569        | 10.0  | 6000 | 0.1853          | 0.2205 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0

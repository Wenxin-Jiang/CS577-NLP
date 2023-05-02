---
tags:
- generated_from_trainer
model-index:
- name: torgo-sentences-TestedSpeakerM01
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# torgo-sentences-TestedSpeakerM01

This model is a fine-tuned version of [yongjian/wav2vec2-large-a](https://huggingface.co/yongjian/wav2vec2-large-a) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4934
- Wer: 0.7531

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 16.1147       | 3.36  | 500  | 0.7890          | 0.9519 |
| 0.6317        | 6.71  | 1000 | 0.5087          | 0.8789 |
| 0.5158        | 10.07 | 1500 | 0.5307          | 0.9519 |
| 0.4783        | 13.42 | 2000 | 0.4320          | 0.9208 |
| 0.5256        | 16.78 | 2500 | 0.3832          | 0.8292 |
| 0.2892        | 20.13 | 3000 | 0.4282          | 0.7531 |
| 0.2733        | 23.49 | 3500 | 0.4369          | 0.7391 |
| 0.2289        | 26.85 | 4000 | 0.4782          | 0.7469 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.2

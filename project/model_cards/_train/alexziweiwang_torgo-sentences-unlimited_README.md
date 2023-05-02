---
tags:
- generated_from_trainer
model-index:
- name: torgo-sentences-unlimited
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# torgo-sentences-unlimited

This model is a fine-tuned version of [yongjian/wav2vec2-large-a](https://huggingface.co/yongjian/wav2vec2-large-a) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4841
- Wer: 0.2696

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
| 19.2722       | 3.65  | 500  | 5.3840          | 0.9950 |
| 3.5604        | 7.3   | 1000 | 3.0665          | 1.0    |
| 2.9063        | 10.95 | 1500 | 2.2699          | 1.0020 |
| 1.1228        | 14.6  | 2000 | 0.5434          | 0.3637 |
| 0.4145        | 18.25 | 2500 | 0.5388          | 0.2934 |
| 0.2217        | 21.9  | 3000 | 0.4926          | 0.2874 |
| 0.1832        | 25.55 | 3500 | 0.4761          | 0.2785 |
| 0.145         | 29.2  | 4000 | 0.4841          | 0.2696 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.2

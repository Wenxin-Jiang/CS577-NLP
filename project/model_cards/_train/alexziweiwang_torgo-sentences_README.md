---
tags:
- generated_from_trainer
model-index:
- name: torgo-sentences
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# torgo-sentences

This model is a fine-tuned version of [yongjian/wav2vec2-large-a](https://huggingface.co/yongjian/wav2vec2-large-a) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4597
- Wer: 0.2763

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
| 7.9559        | 3.68  | 500  | 7.9711          | 1.0    |
| 3.7513        | 7.35  | 1000 | 2.9848          | 1.0    |
| 2.3575        | 11.03 | 1500 | 0.7358          | 0.4943 |
| 0.565         | 14.71 | 2000 | 0.4717          | 0.3160 |
| 0.3093        | 18.38 | 2500 | 0.4621          | 0.3076 |
| 0.2096        | 22.06 | 3000 | 0.4586          | 0.2857 |
| 0.1716        | 25.74 | 3500 | 0.5179          | 0.2805 |
| 0.2116        | 29.41 | 4000 | 0.4597          | 0.2763 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.2

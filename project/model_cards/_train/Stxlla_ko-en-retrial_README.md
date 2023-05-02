---
license: mit
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: ko-en-retrial
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ko-en-retrial

This model is a fine-tuned version of [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4075
- Bleu: 27.1215
- Gen Len: 10.91

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|
| 0.5334        | 1.0   | 16549 | 0.6745          | 14.5544 | 10.4919 |
| 0.4841        | 2.0   | 33098 | 0.6063          | 16.5973 | 10.8128 |
| 0.4308        | 3.0   | 49647 | 0.5447          | 19.1392 | 11.0557 |
| 0.3674        | 4.0   | 66196 | 0.4576          | 23.6457 | 10.8632 |
| 0.306         | 5.0   | 82745 | 0.4075          | 27.1215 | 10.91   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

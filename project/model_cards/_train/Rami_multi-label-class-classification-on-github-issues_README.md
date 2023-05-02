---
tags:
- generated_from_trainer
model-index:
- name: multi-label-class-classification-on-github-issues
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# multi-label-class-classification-on-github-issues

This model is a fine-tuned version of [neuralmagic/oBERT-12-upstream-pruned-unstructured-97](https://huggingface.co/neuralmagic/oBERT-12-upstream-pruned-unstructured-97) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1077
- Micro f1: 0.6520
- Macro f1: 0.0704

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Micro f1 | Macro f1 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| No log        | 1.0   | 49   | 0.2835          | 0.3791   | 0.0172   |
| No log        | 2.0   | 98   | 0.1710          | 0.3791   | 0.0172   |
| No log        | 3.0   | 147  | 0.1433          | 0.3791   | 0.0172   |
| No log        | 4.0   | 196  | 0.1333          | 0.4540   | 0.0291   |
| No log        | 5.0   | 245  | 0.1247          | 0.5206   | 0.0352   |
| No log        | 6.0   | 294  | 0.1173          | 0.6003   | 0.0541   |
| No log        | 7.0   | 343  | 0.1125          | 0.6315   | 0.0671   |
| No log        | 8.0   | 392  | 0.1095          | 0.6439   | 0.0699   |
| No log        | 9.0   | 441  | 0.1072          | 0.6531   | 0.0713   |
| No log        | 10.0  | 490  | 0.1075          | 0.6397   | 0.0695   |
| 0.1605        | 11.0  | 539  | 0.1074          | 0.6591   | 0.0711   |
| 0.1605        | 12.0  | 588  | 0.1043          | 0.6462   | 0.0703   |
| 0.1605        | 13.0  | 637  | 0.1049          | 0.6541   | 0.0709   |
| 0.1605        | 14.0  | 686  | 0.1051          | 0.6524   | 0.0713   |
| 0.1605        | 15.0  | 735  | 0.1061          | 0.6535   | 0.0770   |
| 0.1605        | 16.0  | 784  | 0.1034          | 0.6511   | 0.0708   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

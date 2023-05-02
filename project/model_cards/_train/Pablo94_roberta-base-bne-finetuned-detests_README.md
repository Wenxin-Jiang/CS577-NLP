---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: roberta-base-bne-finetuned-detests
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-bne-finetuned-detests

This model is a fine-tuned version of [BSC-TeMU/roberta-base-bne](https://huggingface.co/BSC-TeMU/roberta-base-bne) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0716
- Accuracy: 0.8396

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2972        | 1.0   | 153  | 0.3359          | 0.8462   |
| 0.2924        | 2.0   | 306  | 0.4509          | 0.8249   |
| 0.0663        | 3.0   | 459  | 0.7186          | 0.8527   |
| 0.0018        | 4.0   | 612  | 0.8081          | 0.8314   |
| 0.0004        | 5.0   | 765  | 0.8861          | 0.8560   |
| 0.0003        | 6.0   | 918  | 0.9940          | 0.8380   |
| 0.0002        | 7.0   | 1071 | 1.0330          | 0.8396   |
| 0.0002        | 8.0   | 1224 | 1.0545          | 0.8396   |
| 0.0002        | 9.0   | 1377 | 1.0673          | 0.8396   |
| 0.0002        | 10.0  | 1530 | 1.0716          | 0.8396   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1

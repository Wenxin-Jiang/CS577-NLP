---
license: cc
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: racism-finetuned-detests-29-10-2022
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# racism-finetuned-detests-29-10-2022

This model is a fine-tuned version of [davidmasip/racism](https://huggingface.co/davidmasip/racism) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0150
- Accuracy: 0.8560

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
| 0.2659        | 1.0   | 153  | 0.3250          | 0.8429   |
| 0.1191        | 2.0   | 306  | 0.5344          | 0.8380   |
| 0.0074        | 3.0   | 459  | 0.8188          | 0.8396   |
| 0.0001        | 4.0   | 612  | 0.9264          | 0.8462   |
| 0.0001        | 5.0   | 765  | 0.9551          | 0.8462   |
| 0.0001        | 6.0   | 918  | 0.9771          | 0.8527   |
| 0.0001        | 7.0   | 1071 | 0.9937          | 0.8527   |
| 0.0001        | 8.0   | 1224 | 1.0054          | 0.8560   |
| 0.0           | 9.0   | 1377 | 1.0126          | 0.8560   |
| 0.0001        | 10.0  | 1530 | 1.0150          | 0.8560   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1

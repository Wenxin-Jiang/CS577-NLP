---
license: other
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: 6.7b-dalio-principles-book-1-epoch-1-gas-6e-6-lr
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 6.7b-dalio-principles-book-1-epoch-1-gas-6e-6-lr

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4121
- Accuracy: 0.3487

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-06
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 32
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.4875        | 0.11  | 1    | 2.5059          | 0.3397   |
| 2.5339        | 0.22  | 2    | 2.5059          | 0.3397   |
| 2.5161        | 0.33  | 3    | 2.5059          | 0.3397   |
| 2.4524        | 0.44  | 4    | 2.5059          | 0.3397   |
| 2.554         | 0.56  | 5    | 2.4785          | 0.3416   |
| 2.4678        | 0.67  | 6    | 2.4785          | 0.3416   |
| 2.4836        | 0.78  | 7    | 2.4473          | 0.3458   |
| 2.4138        | 0.89  | 8    | 2.4297          | 0.3473   |
| 2.4551        | 1.0   | 9    | 2.4121          | 0.3487   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

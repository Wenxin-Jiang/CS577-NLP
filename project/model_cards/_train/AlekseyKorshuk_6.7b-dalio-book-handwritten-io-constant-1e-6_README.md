---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/dalio-book-handwritten-io-sorted
metrics:
- accuracy
model-index:
- name: 6.7b-dalio-book-handwritten-io-constant-1e-6
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/dalio-book-handwritten-io-sorted
      type: AlekseyKorshuk/dalio-book-handwritten-io-sorted
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.3103083378945448
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 6.7b-dalio-book-handwritten-io-constant-1e-6

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the AlekseyKorshuk/dalio-book-handwritten-io-sorted dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3633
- Accuracy: 0.3103

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 8
- total_eval_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.6396        | 0.11  | 6    | 2.5039          | 0.2989   |
| 2.5754        | 0.21  | 12   | 2.4902          | 0.2999   |
| 2.5859        | 0.32  | 18   | 2.4648          | 0.3018   |
| 2.5432        | 0.43  | 24   | 2.4434          | 0.3035   |
| 2.472         | 0.54  | 30   | 2.4238          | 0.3053   |
| 2.5184        | 0.64  | 36   | 2.4082          | 0.3064   |
| 2.4524        | 0.75  | 42   | 2.3926          | 0.3078   |
| 2.3876        | 0.86  | 48   | 2.3789          | 0.3092   |
| 2.4456        | 0.96  | 54   | 2.3633          | 0.3103   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

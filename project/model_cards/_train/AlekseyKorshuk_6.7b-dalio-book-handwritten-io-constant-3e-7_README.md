---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/dalio-book-handwritten-io-sorted
metrics:
- accuracy
model-index:
- name: 6.7b-dalio-book-handwritten-io-constant-3e-7
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
      value: 0.30175150519978106
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 6.7b-dalio-book-handwritten-io-constant-3e-7

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the AlekseyKorshuk/dalio-book-handwritten-io-sorted dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4629
- Accuracy: 0.3018

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-07
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
| 2.6398        | 0.11  | 6    | 2.5059          | 0.2987   |
| 2.5823        | 0.21  | 12   | 2.5039          | 0.2988   |
| 2.6128        | 0.32  | 18   | 2.4980          | 0.2991   |
| 2.5775        | 0.43  | 24   | 2.4922          | 0.2995   |
| 2.527         | 0.54  | 30   | 2.4863          | 0.2999   |
| 2.5752        | 0.64  | 36   | 2.4805          | 0.3003   |
| 2.5131        | 0.75  | 42   | 2.4746          | 0.3008   |
| 2.4436        | 0.86  | 48   | 2.4688          | 0.3014   |
| 2.5114        | 0.96  | 54   | 2.4629          | 0.3018   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

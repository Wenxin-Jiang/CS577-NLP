---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2
metrics:
- accuracy
model-index:
- name: 6.7b-dalio-book-handwritten-io-constant-6e-6-v2
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2
      type: AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.3035631370641431
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 6.7b-dalio-book-handwritten-io-constant-6e-6-v2

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the AlekseyKorshuk/dalio-book-handwritten-io-sorted-v2 dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1504
- Accuracy: 0.3036

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
| 2.5793        | 0.08  | 6    | 2.5723          | 0.2713   |
| 2.5612        | 0.16  | 12   | 2.5             | 0.2750   |
| 2.5235        | 0.24  | 18   | 2.4473          | 0.2784   |
| 2.4961        | 0.32  | 24   | 2.4102          | 0.2818   |
| 2.4488        | 0.4   | 30   | 2.3672          | 0.2849   |
| 2.4121        | 0.48  | 36   | 2.3320          | 0.2878   |
| 2.3901        | 0.56  | 42   | 2.3027          | 0.2903   |
| 2.2845        | 0.64  | 48   | 2.2715          | 0.2927   |
| 2.3032        | 0.72  | 54   | 2.2422          | 0.2955   |
| 2.2954        | 0.8   | 60   | 2.2090          | 0.2985   |
| 2.3908        | 0.88  | 66   | 2.1836          | 0.3009   |
| 2.2676        | 0.96  | 72   | 2.1504          | 0.3036   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

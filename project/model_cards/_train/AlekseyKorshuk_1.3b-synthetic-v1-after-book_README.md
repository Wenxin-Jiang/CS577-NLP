---
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/dalio-synthetic-io
metrics:
- accuracy
model-index:
- name: 1.3b-synthetic-v1-after-book
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/dalio-synthetic-io
      type: AlekseyKorshuk/dalio-synthetic-io
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.07541139670882632
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 1.3b-synthetic-v1-after-book

This model is a fine-tuned version of [/models/1.3b-dalio-principles-book](https://huggingface.co//models/1.3b-dalio-principles-book) on the AlekseyKorshuk/dalio-synthetic-io dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9805
- Accuracy: 0.0754

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 32
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.0841        | 0.1   | 1    | 2.0254          | 0.0759   |
| 2.062         | 0.2   | 2    | 2.0254          | 0.0759   |
| 2.1509        | 0.3   | 3    | 1.9941          | 0.0761   |
| 2.1206        | 0.4   | 4    | 1.9941          | 0.0756   |
| 2.2087        | 0.5   | 5    | 1.9941          | 0.0757   |
| 2.0337        | 0.6   | 6    | 1.9902          | 0.0755   |
| 2.026         | 0.7   | 7    | 1.9854          | 0.0755   |
| 2.1879        | 0.8   | 8    | 1.9834          | 0.0756   |
| 2.1052        | 0.9   | 9    | 1.9824          | 0.0754   |
| 2.046         | 1.0   | 10   | 1.9805          | 0.0754   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

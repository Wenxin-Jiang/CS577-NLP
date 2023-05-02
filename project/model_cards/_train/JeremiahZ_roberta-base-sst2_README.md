---
language:
- en
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: roberta-base-sst2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE SST2
      type: glue
      args: sst2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9357798165137615
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-sst2

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE SST2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2314
- Accuracy: 0.9358

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.2287        | 1.0   | 4210  | 0.2314          | 0.9358   |
| 0.1959        | 2.0   | 8420  | 0.3027          | 0.9266   |
| 0.1635        | 3.0   | 12630 | 0.3022          | 0.9300   |
| 0.1148        | 4.0   | 16840 | 0.3162          | 0.9289   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1

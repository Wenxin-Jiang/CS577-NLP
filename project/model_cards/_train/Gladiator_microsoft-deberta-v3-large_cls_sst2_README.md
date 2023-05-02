---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: microsoft-deberta-v3-large_cls_sst2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# microsoft-deberta-v3-large_cls_sst2

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on [sst2](https://huggingface.co/datasets/sst2) unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2206
- Accuracy: 0.9576

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
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.2
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 433  | 0.2420          | 0.9415   |
| 0.3716        | 2.0   | 866  | 0.2387          | 0.9404   |
| 0.2001        | 3.0   | 1299 | 0.2379          | 0.9461   |
| 0.1187        | 4.0   | 1732 | 0.2007          | 0.9610   |
| 0.0555        | 5.0   | 2165 | 0.2206          | 0.9576   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

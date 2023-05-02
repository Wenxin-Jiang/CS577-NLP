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
- name: roberta-base-wnli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE WNLI
      type: glue
      args: wnli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.5633802816901409
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-wnli

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE WNLI dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6849
- Accuracy: 0.5634

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 40   | 0.6849          | 0.5634   |
| No log        | 2.0   | 80   | 0.6912          | 0.5634   |
| No log        | 3.0   | 120  | 0.6918          | 0.5634   |
| No log        | 4.0   | 160  | 0.6964          | 0.4366   |
| No log        | 5.0   | 200  | 0.6928          | 0.5634   |
| No log        | 6.0   | 240  | 0.7005          | 0.4366   |
| No log        | 7.0   | 280  | 0.6964          | 0.3099   |
| No log        | 8.0   | 320  | 0.6986          | 0.3521   |
| No log        | 9.0   | 360  | 0.6969          | 0.5493   |
| No log        | 10.0  | 400  | 0.6976          | 0.5634   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1

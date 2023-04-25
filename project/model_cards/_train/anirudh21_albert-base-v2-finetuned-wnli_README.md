---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: albert-base-v2-finetuned-wnli
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: wnli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.5633802816901409
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-v2-finetuned-wnli

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6878
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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 40   | 0.6878          | 0.5634   |
| No log        | 2.0   | 80   | 0.6919          | 0.5634   |
| No log        | 3.0   | 120  | 0.6877          | 0.5634   |
| No log        | 4.0   | 160  | 0.6984          | 0.4085   |
| No log        | 5.0   | 200  | 0.6957          | 0.5211   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.0
- Tokenizers 0.10.3

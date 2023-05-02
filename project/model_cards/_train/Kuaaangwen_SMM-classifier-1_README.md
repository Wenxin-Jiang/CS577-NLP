---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: SMM-classifier-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SMM-classifier-1

This model is a fine-tuned version of [Kuaaangwen/bert-base-cased-finetuned-chemistry](https://huggingface.co/Kuaaangwen/bert-base-cased-finetuned-chemistry) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5506
- Accuracy: 0.8333

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 7    | 0.2044          | 0.8333   |
| No log        | 2.0   | 14   | 0.3574          | 0.8333   |
| No log        | 3.0   | 21   | 0.1551          | 0.8333   |
| No log        | 4.0   | 28   | 0.9122          | 0.8333   |
| No log        | 5.0   | 35   | 0.9043          | 0.8333   |
| No log        | 6.0   | 42   | 0.7262          | 0.8333   |
| No log        | 7.0   | 49   | 0.5977          | 0.8333   |
| No log        | 8.0   | 56   | 0.5567          | 0.8333   |
| No log        | 9.0   | 63   | 0.5484          | 0.8333   |
| No log        | 10.0  | 70   | 0.5506          | 0.8333   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

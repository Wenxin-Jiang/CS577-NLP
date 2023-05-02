---
license: mit
tags:
- generated_from_trainer
datasets:
- xtreme
metrics:
- f1
model-index:
- name: xlm-roberta-base-finetuned-panx-it
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: xtreme
      type: xtreme
      config: PAN-X.it
      split: train
      args: PAN-X.it
    metrics:
    - name: F1
      type: f1
      value: 0.7434973989595838
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-panx-it

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the xtreme dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3355
- F1: 0.7435

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
- train_batch_size: 96
- eval_batch_size: 96
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 1.0   | 18   | 0.6871          | 0.4648 |
| No log        | 2.0   | 36   | 0.3901          | 0.6932 |
| No log        | 3.0   | 54   | 0.3355          | 0.7435 |


### Framework versions

- Transformers 4.21.0.dev0
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

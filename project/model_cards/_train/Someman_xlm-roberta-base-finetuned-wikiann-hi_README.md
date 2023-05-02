---
license: mit
tags:
- generated_from_trainer
datasets:
- wikiann
metrics:
- f1
model-index:
- name: xlm-roberta-base-finetuned-wikiann-hi
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikiann
      type: wikiann
      args: hi
    metrics:
    - name: F1
      type: f1
      value: 1.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-wikiann-hi

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3097
- F1: 1.0

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1  |
|:-------------:|:-----:|:----:|:---------------:|:---:|
| 0.5689        | 1.0   | 209  | 0.3179          | 1.0 |
| 0.2718        | 2.0   | 418  | 0.2733          | 1.0 |
| 0.19          | 3.0   | 627  | 0.2560          | 1.0 |
| 0.142         | 4.0   | 836  | 0.2736          | 1.0 |
| 0.0967        | 5.0   | 1045 | 0.2686          | 1.0 |
| 0.0668        | 6.0   | 1254 | 0.2966          | 1.0 |
| 0.052         | 7.0   | 1463 | 0.3194          | 1.0 |
| 0.0369        | 8.0   | 1672 | 0.3034          | 1.0 |
| 0.0236        | 9.0   | 1881 | 0.3174          | 1.0 |
| 0.0135        | 10.0  | 2090 | 0.3097          | 1.0 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

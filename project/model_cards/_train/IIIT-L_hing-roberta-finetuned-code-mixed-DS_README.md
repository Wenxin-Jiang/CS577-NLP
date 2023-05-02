---
license: cc-by-4.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: hing-roberta-finetuned-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-roberta-finetuned-code-mixed-DS

This model is a fine-tuned version of [l3cube-pune/hing-roberta](https://huggingface.co/l3cube-pune/hing-roberta) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8512
- Accuracy: 0.7706
- Precision: 0.7217
- Recall: 0.7233
- F1: 0.7222

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.932923543227153e-05
- train_batch_size: 8
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0216        | 1.0   | 497  | 1.1363          | 0.5392   | 0.4228    | 0.3512 | 0.2876 |
| 0.9085        | 2.0   | 994  | 0.7599          | 0.6761   | 0.6247    | 0.6294 | 0.5902 |
| 0.676         | 3.0   | 1491 | 0.7415          | 0.7505   | 0.6946    | 0.7034 | 0.6983 |
| 0.4404        | 4.0   | 1988 | 0.8512          | 0.7706   | 0.7217    | 0.7233 | 0.7222 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1

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
- name: hing-mbert-finetuned-non-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-mbert-finetuned-non-code-mixed-DS

This model is a fine-tuned version of [l3cube-pune/hing-mbert](https://huggingface.co/l3cube-pune/hing-mbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7369
- Accuracy: 0.6667
- Precision: 0.6553
- Recall: 0.6428
- F1: 0.6459

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
| 0.9413        | 1.0   | 926  | 0.8472          | 0.6354   | 0.6215    | 0.6247 | 0.6225 |
| 0.7278        | 2.0   | 1852 | 0.8966          | 0.6429   | 0.6408    | 0.6094 | 0.6122 |
| 0.4743        | 3.0   | 2778 | 1.2428          | 0.6613   | 0.6502    | 0.6420 | 0.6444 |
| 0.2558        | 4.0   | 3704 | 1.7369          | 0.6667   | 0.6553    | 0.6428 | 0.6459 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1

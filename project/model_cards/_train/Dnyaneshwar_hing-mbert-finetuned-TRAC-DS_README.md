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
- name: hing-mbert-finetuned-TRAC-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-mbert-finetuned-TRAC-DS

This model is a fine-tuned version of [l3cube-pune/hing-mbert](https://huggingface.co/l3cube-pune/hing-mbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9044
- Accuracy: 0.7010
- Precision: 0.6772
- Recall: 0.6723
- F1: 0.6740

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2.824279936868144e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.837         | 1.0   | 1224 | 0.7640          | 0.6422   | 0.6377    | 0.6475 | 0.6277 |
| 0.6164        | 2.0   | 2448 | 0.8456          | 0.6724   | 0.6581    | 0.6623 | 0.6547 |
| 0.434         | 3.0   | 3672 | 1.0284          | 0.6969   | 0.6715    | 0.6771 | 0.6729 |
| 0.267         | 4.0   | 4896 | 1.5533          | 0.6912   | 0.6644    | 0.6675 | 0.6655 |
| 0.1542        | 5.0   | 6120 | 1.9044          | 0.7010   | 0.6772    | 0.6723 | 0.6740 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

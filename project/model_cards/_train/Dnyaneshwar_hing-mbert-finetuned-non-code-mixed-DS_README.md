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
- Loss: 1.6572
- Accuracy: 0.6429
- Precision: 0.6334
- Recall: 0.6231
- F1: 0.6262

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.005         | 0.5   | 926  | 0.9346          | 0.5707   | 0.5844    | 0.5274 | 0.5108 |
| 0.969         | 1.0   | 1852 | 1.0295          | 0.5858   | 0.5893    | 0.5685 | 0.5455 |
| 0.8976        | 1.5   | 2778 | 1.0491          | 0.5739   | 0.5712    | 0.5295 | 0.5152 |
| 0.8578        | 2.0   | 3704 | 0.8577          | 0.6343   | 0.6443    | 0.6379 | 0.6318 |
| 0.7164        | 2.5   | 4630 | 1.3325          | 0.6300   | 0.6219    | 0.5932 | 0.5939 |
| 0.7391        | 3.0   | 5556 | 1.0329          | 0.6537   | 0.6489    | 0.6519 | 0.6467 |
| 0.5454        | 3.5   | 6482 | 1.6031          | 0.6375   | 0.6525    | 0.6188 | 0.6218 |
| 0.4927        | 4.0   | 7408 | 1.6572          | 0.6429   | 0.6334    | 0.6231 | 0.6262 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

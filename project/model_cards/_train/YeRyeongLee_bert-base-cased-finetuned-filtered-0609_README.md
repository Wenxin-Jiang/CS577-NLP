---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: bert-base-cased-finetuned-filtered-0609
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cased-finetuned-filtered-0609

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2410
- Accuracy: 0.9748
- Precision: 0.9751
- Recall: 0.9748
- F1: 0.9749

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
- lr_scheduler_warmup_steps: 1000
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.2028        | 1.0   | 3180  | 0.2405          | 0.9535   | 0.9561    | 0.9535 | 0.9538 |
| 0.1632        | 2.0   | 6360  | 0.1686          | 0.9660   | 0.9664    | 0.9660 | 0.9661 |
| 0.1203        | 3.0   | 9540  | 0.1625          | 0.9648   | 0.9655    | 0.9648 | 0.9648 |
| 0.1233        | 4.0   | 12720 | 0.1510          | 0.9698   | 0.9702    | 0.9698 | 0.9699 |
| 0.0823        | 5.0   | 15900 | 0.1600          | 0.9730   | 0.9732    | 0.9730 | 0.9730 |
| 0.0453        | 6.0   | 19080 | 0.1953          | 0.9723   | 0.9724    | 0.9723 | 0.9723 |
| 0.031         | 7.0   | 22260 | 0.1754          | 0.9755   | 0.9755    | 0.9755 | 0.9755 |
| 0.0166        | 8.0   | 25440 | 0.2155          | 0.9739   | 0.9740    | 0.9739 | 0.9739 |
| 0.0036        | 9.0   | 28620 | 0.2519          | 0.9730   | 0.9733    | 0.9730 | 0.9730 |
| 0.0035        | 10.0  | 31800 | 0.2410          | 0.9748   | 0.9751    | 0.9748 | 0.9749 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.1+cu111
- Datasets 1.16.1
- Tokenizers 0.12.1

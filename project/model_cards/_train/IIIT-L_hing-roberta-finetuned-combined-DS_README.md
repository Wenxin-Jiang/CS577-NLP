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
- name: hing-roberta-finetuned-combined-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-roberta-finetuned-combined-DS

This model is a fine-tuned version of [l3cube-pune/hing-roberta](https://huggingface.co/l3cube-pune/hing-roberta) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0005
- Accuracy: 0.6840
- Precision: 0.6568
- Recall: 0.6579
- F1: 0.6570

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.927975767245621e-05
- train_batch_size: 8
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.8684        | 1.0   | 1423 | 0.8762          | 0.6643   | 0.6561    | 0.6209 | 0.6215 |
| 0.6545        | 2.0   | 2846 | 0.8043          | 0.6805   | 0.6497    | 0.6522 | 0.6502 |
| 0.4267        | 3.0   | 4269 | 1.1337          | 0.6966   | 0.6668    | 0.6699 | 0.6680 |
| 0.2762        | 4.0   | 5692 | 1.6520          | 0.6784   | 0.6558    | 0.6571 | 0.6553 |
| 0.1535        | 5.0   | 7115 | 2.0005          | 0.6840   | 0.6568    | 0.6579 | 0.6570 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1

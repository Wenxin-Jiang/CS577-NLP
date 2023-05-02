---
license: cc-by-4.0
tags:
- generated_from_trainer
model-index:
- name: norbert2-finetuned-comments
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# norbert2-finetuned-comments

This model is a fine-tuned version of [ltgoslo/norbert2](https://huggingface.co/ltgoslo/norbert2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8562

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
- train_batch_size: 17
- eval_batch_size: 17
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 3.7115        | 1.0   | 1030  | 3.2753          |
| 3.248         | 2.0   | 2060  | 3.0974          |
| 3.0825        | 3.0   | 3090  | 3.0759          |
| 2.992         | 4.0   | 4120  | 3.0478          |
| 2.8956        | 5.0   | 5150  | 2.9340          |
| 2.8315        | 6.0   | 6180  | 2.9893          |
| 2.7772        | 7.0   | 7210  | 2.9035          |
| 2.7037        | 8.0   | 8240  | 2.8797          |
| 2.6431        | 9.0   | 9270  | 2.8799          |
| 2.6345        | 10.0  | 10300 | 2.8809          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Tokenizers 0.13.2

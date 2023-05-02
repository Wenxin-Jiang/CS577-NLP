---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-16-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-16-5

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5433
- Accuracy: 0.7924

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6774        | 1.0   | 7    | 0.7450          | 0.2857   |
| 0.7017        | 2.0   | 14   | 0.7552          | 0.2857   |
| 0.6438        | 3.0   | 21   | 0.7140          | 0.4286   |
| 0.3525        | 4.0   | 28   | 0.5570          | 0.7143   |
| 0.2061        | 5.0   | 35   | 0.5303          | 0.8571   |
| 0.0205        | 6.0   | 42   | 0.6706          | 0.8571   |
| 0.0068        | 7.0   | 49   | 0.8284          | 0.8571   |
| 0.0029        | 8.0   | 56   | 0.9281          | 0.8571   |
| 0.0015        | 9.0   | 63   | 0.9871          | 0.8571   |
| 0.0013        | 10.0  | 70   | 1.0208          | 0.8571   |
| 0.0008        | 11.0  | 77   | 1.0329          | 0.8571   |
| 0.0005        | 12.0  | 84   | 1.0348          | 0.8571   |
| 0.0004        | 13.0  | 91   | 1.0437          | 0.8571   |
| 0.0005        | 14.0  | 98   | 1.0512          | 0.8571   |
| 0.0004        | 15.0  | 105  | 1.0639          | 0.8571   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

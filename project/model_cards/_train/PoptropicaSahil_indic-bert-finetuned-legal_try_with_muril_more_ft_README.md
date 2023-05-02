---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: indic-bert-finetuned-legal_try_with_muril_more_ft
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indic-bert-finetuned-legal_try_with_muril_more_ft

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4640
- Accuracy: 0.7865
- F1: 0.7846

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.4266        | 1.0   | 625  | 0.4652          | 0.7925   | 0.7892 |
| 0.4163        | 2.0   | 1250 | 0.4640          | 0.7905   | 0.7868 |
| 0.4085        | 3.0   | 1875 | 0.4640          | 0.788    | 0.7867 |
| 0.4043        | 4.0   | 2500 | 0.4640          | 0.7865   | 0.7846 |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.12.1+cu113
- Datasets 1.16.1
- Tokenizers 0.10.3

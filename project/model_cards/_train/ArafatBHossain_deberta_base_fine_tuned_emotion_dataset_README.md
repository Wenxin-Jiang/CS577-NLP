---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta_base_fine_tuned_emotion_dataset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta_base_fine_tuned_emotion_dataset

This model is a fine-tuned version of [microsoft/deberta-base](https://huggingface.co/microsoft/deberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1992
- Accuracy: 0.944

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
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2485        | 1.0   | 2000 | 0.2500          | 0.929    |
| 0.1541        | 2.0   | 4000 | 0.1512          | 0.9375   |
| 0.1026        | 3.0   | 6000 | 0.1992          | 0.944    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

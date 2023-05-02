---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: phobert-finetuned-sentiment-analysis
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# phobert-finetuned-sentiment-analysis

This model is a fine-tuned version of [vinai/phobert-base](https://huggingface.co/vinai/phobert-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3007
- Accuracy: 0.9431

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.113         | 1.0   | 1429 | 0.3007          | 0.9431   |
| 0.1043        | 2.0   | 2858 | 0.3007          | 0.9431   |
| 0.1135        | 3.0   | 4287 | 0.3007          | 0.9431   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2

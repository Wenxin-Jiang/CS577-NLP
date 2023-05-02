---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: robert_base_fine_tuned_emotion_dataset
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# robert_base_fine_tuned_emotion_dataset

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1996
- Accuracy: 0.936

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
| 0.3438        | 1.0   | 2000 | 0.3140          | 0.921    |
| 0.1911        | 2.0   | 4000 | 0.1947          | 0.9315   |
| 0.1348        | 3.0   | 6000 | 0.1996          | 0.936    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

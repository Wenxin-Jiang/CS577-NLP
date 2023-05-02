---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- accuracy
model-index:
- name: distiled_flip_model_emotion_alpha_0.8_v1
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: emotion
      type: emotion
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9425
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distiled_flip_model_emotion_alpha_0.8_v1

This model is a fine-tuned version of [ArafatBHossain/distill_bert_fine_tuned_emotion_dataset](https://huggingface.co/ArafatBHossain/distill_bert_fine_tuned_emotion_dataset) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1615
- Accuracy: 0.9425

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.1921        | 1.0   | 2000 | 0.2402          | 0.933    |
| 0.129         | 2.0   | 4000 | 0.1789          | 0.94     |
| 0.0869        | 3.0   | 6000 | 0.1615          | 0.9425   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.11.0
- Datasets 2.6.1
- Tokenizers 0.12.1

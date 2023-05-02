---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- accuracy
model-index:
- name: distiled_flip_model_emotion_alpha_0.8_epoch5_v1
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
      value: 0.942
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distiled_flip_model_emotion_alpha_0.8_epoch5_v1

This model is a fine-tuned version of [ArafatBHossain/distill_bert_fine_tuned_emotion_dataset](https://huggingface.co/ArafatBHossain/distill_bert_fine_tuned_emotion_dataset) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1476
- Accuracy: 0.942

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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.1966        | 1.0   | 2000  | 0.2675          | 0.9315   |
| 0.154         | 2.0   | 4000  | 0.2265          | 0.9355   |
| 0.1214        | 3.0   | 6000  | 0.1805          | 0.9375   |
| 0.078         | 4.0   | 8000  | 0.1401          | 0.9385   |
| 0.0652        | 5.0   | 10000 | 0.1476          | 0.942    |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.11.0
- Datasets 2.6.1
- Tokenizers 0.12.1

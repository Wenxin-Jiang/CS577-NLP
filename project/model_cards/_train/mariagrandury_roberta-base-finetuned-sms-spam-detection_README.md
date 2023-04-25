---
license: mit
tags:
- generated_from_trainer
datasets:
- sms_spam
metrics:
- accuracy
model-index:
- name: roberta-base-finetuned-sms-spam-detection
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: sms_spam
      type: sms_spam
      args: plain_text
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.998
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-sms-spam-detection

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the sms_spam dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0133
- Accuracy: 0.998

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0363        | 1.0   | 250  | 0.0156          | 0.996    |
| 0.0147        | 2.0   | 500  | 0.0133          | 0.998    |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0

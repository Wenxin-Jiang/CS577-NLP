---
tags:
- generated_from_trainer
datasets:
- sms_spam
metrics:
- accuracy
model-index:
- name: MiniLMv2-L12-H384-distilled-finetuned-spam-detection
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
      value: 0.9928263988522238
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MiniLMv2-L12-H384-distilled-finetuned-spam-detection

This model is a fine-tuned version of [nreimers/MiniLMv2-L12-H384-distilled-from-RoBERTa-Large](https://huggingface.co/nreimers/MiniLMv2-L12-H384-distilled-from-RoBERTa-Large) on the sms_spam dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0938
- Accuracy: 0.9928

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 33
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.4101        | 1.0   | 131  | 0.4930          | 0.9763   |
| 0.8003        | 2.0   | 262  | 0.3999          | 0.9799   |
| 0.377         | 3.0   | 393  | 0.3196          | 0.9828   |
| 0.302         | 4.0   | 524  | 0.3462          | 0.9828   |
| 0.1945        | 5.0   | 655  | 0.1094          | 0.9928   |
| 0.1393        | 6.0   | 786  | 0.0938          | 0.9928   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4
- Tokenizers 0.12.1

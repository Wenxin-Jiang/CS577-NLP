---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: albert-base-v2-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9301181102362205
    - name: Recall
      type: recall
      value: 0.9376033513394334
    - name: F1
      type: f1
      value: 0.9338457315399397
    - name: Accuracy
      type: accuracy
      value: 0.9851613086447802
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-v2-finetuned-ner

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0700
- Precision: 0.9301
- Recall: 0.9376
- F1: 0.9338
- Accuracy: 0.9852

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.096         | 1.0   | 1756 | 0.0752          | 0.9163    | 0.9201 | 0.9182 | 0.9811   |
| 0.0481        | 2.0   | 3512 | 0.0761          | 0.9169    | 0.9293 | 0.9231 | 0.9830   |
| 0.0251        | 3.0   | 5268 | 0.0700          | 0.9301    | 0.9376 | 0.9338 | 0.9852   |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.1
- Datasets 1.17.0
- Tokenizers 0.10.3

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
- name: roberta-base-bne-finetuned-ner
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
      value: 0.9237957261861645
    - name: Recall
      type: recall
      value: 0.9351077870655521
    - name: F1
      type: f1
      value: 0.9294173377546188
    - name: Accuracy
      type: accuracy
      value: 0.9847536857245595
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-bne-finetuned-ner

This model is a fine-tuned version of [PlanTL-GOB-ES/roberta-base-bne](https://huggingface.co/PlanTL-GOB-ES/roberta-base-bne) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0659
- Precision: 0.9238
- Recall: 0.9351
- F1: 0.9294
- Accuracy: 0.9848

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1931        | 1.0   | 878  | 0.0800          | 0.8892    | 0.8853 | 0.8872 | 0.9770   |
| 0.0409        | 2.0   | 1756 | 0.0655          | 0.9178    | 0.9238 | 0.9208 | 0.9828   |
| 0.0138        | 3.0   | 2634 | 0.0663          | 0.9207    | 0.9276 | 0.9241 | 0.9839   |
| 0.0051        | 4.0   | 3512 | 0.0659          | 0.9238    | 0.9351 | 0.9294 | 0.9848   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.9.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3

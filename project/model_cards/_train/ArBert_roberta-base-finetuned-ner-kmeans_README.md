---
license: mit
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
model-index:
- name: roberta-base-finetuned-ner-kmeans
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
      value: 0.955868544600939
    - name: Recall
      type: recall
      value: 0.9614658103513412
    - name: F1
      type: f1
      value: 0.9586590074394953
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-ner-kmeans

This model is a fine-tuned version of [ArBert/roberta-base-finetuned-ner](https://huggingface.co/ArBert/roberta-base-finetuned-ner) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0592
- Precision: 0.9559
- Recall: 0.9615
- F1: 0.9587

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|
| 0.0248        | 1.0   | 878  | 0.0609          | 0.9507    | 0.9561 | 0.9534 |
| 0.0163        | 2.0   | 1756 | 0.0640          | 0.9515    | 0.9578 | 0.9546 |
| 0.0089        | 3.0   | 2634 | 0.0592          | 0.9559    | 0.9615 | 0.9587 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0

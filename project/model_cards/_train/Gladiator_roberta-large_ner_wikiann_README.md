---
license: mit
tags:
- generated_from_trainer
datasets:
- wikiann
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: roberta-large_ner_wikiann
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikiann
      type: wikiann
      args: en
    metrics:
    - name: Precision
      type: precision
      value: 0.8462551098177787
    - name: Recall
      type: recall
      value: 0.8634242895518167
    - name: F1
      type: f1
      value: 0.8547534903250638
    - name: Accuracy
      type: accuracy
      value: 0.9382388000397338
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large_ner_wikiann

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2783
- Precision: 0.8463
- Recall: 0.8634
- F1: 0.8548
- Accuracy: 0.9382

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
- lr_scheduler_type: cosine
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.3395        | 1.0   | 1250 | 0.2652          | 0.8039    | 0.8308 | 0.8171 | 0.9242   |
| 0.2343        | 2.0   | 2500 | 0.2431          | 0.8354    | 0.8503 | 0.8428 | 0.9329   |
| 0.1721        | 3.0   | 3750 | 0.2315          | 0.8330    | 0.8503 | 0.8416 | 0.9352   |
| 0.1156        | 4.0   | 5000 | 0.2709          | 0.8477    | 0.8634 | 0.8554 | 0.9385   |
| 0.1026        | 5.0   | 6250 | 0.2783          | 0.8463    | 0.8634 | 0.8548 | 0.9382   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

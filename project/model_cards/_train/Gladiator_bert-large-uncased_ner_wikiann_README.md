---
license: apache-2.0
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
- name: bert-large-uncased_ner_wikiann
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
      value: 0.8383588049015558
    - name: Recall
      type: recall
      value: 0.8608794005372543
    - name: F1
      type: f1
      value: 0.8494698660714285
    - name: Accuracy
      type: accuracy
      value: 0.9379407966623622
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-large-uncased_ner_wikiann

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3373
- Precision: 0.8384
- Recall: 0.8609
- F1: 0.8495
- Accuracy: 0.9379

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
| 0.3146        | 1.0   | 1250 | 0.2545          | 0.7956    | 0.8372 | 0.8159 | 0.9285   |
| 0.1973        | 2.0   | 2500 | 0.2438          | 0.8267    | 0.8546 | 0.8404 | 0.9349   |
| 0.1181        | 3.0   | 3750 | 0.2637          | 0.8320    | 0.8588 | 0.8452 | 0.9374   |
| 0.0647        | 4.0   | 5000 | 0.3175          | 0.8389    | 0.8627 | 0.8507 | 0.9387   |
| 0.0443        | 5.0   | 6250 | 0.3373          | 0.8384    | 0.8609 | 0.8495 | 0.9379   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

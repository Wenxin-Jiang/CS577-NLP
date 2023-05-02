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
- name: funnel-transformer-xlarge_ner_wikiann
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
      value: 0.8522084990579862
    - name: Recall
      type: recall
      value: 0.8633535981903011
    - name: F1
      type: f1
      value: 0.8577448467184043
    - name: Accuracy
      type: accuracy
      value: 0.935805105791199
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# funnel-transformer-xlarge_ner_wikiann

This model is a fine-tuned version of [funnel-transformer/xlarge](https://huggingface.co/funnel-transformer/xlarge) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4023
- Precision: 0.8522
- Recall: 0.8634
- F1: 0.8577
- Accuracy: 0.9358

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.3193        | 1.0   | 5000  | 0.3116          | 0.8239    | 0.8296 | 0.8267 | 0.9260   |
| 0.2836        | 2.0   | 10000 | 0.2846          | 0.8446    | 0.8498 | 0.8472 | 0.9325   |
| 0.2237        | 3.0   | 15000 | 0.3258          | 0.8427    | 0.8542 | 0.8484 | 0.9332   |
| 0.1303        | 4.0   | 20000 | 0.3801          | 0.8531    | 0.8634 | 0.8582 | 0.9362   |
| 0.0867        | 5.0   | 25000 | 0.4023          | 0.8522    | 0.8634 | 0.8577 | 0.9358   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

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
- name: distilbert-base-uncased_ner_wikiann
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
      value: 0.8138623392697518
    - name: Recall
      type: recall
      value: 0.8367029548989113
    - name: F1
      type: f1
      value: 0.8251246122207119
    - name: Accuracy
      type: accuracy
      value: 0.9300437071620145
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased_ner_wikiann

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2834
- Precision: 0.8139
- Recall: 0.8367
- F1: 0.8251
- Accuracy: 0.9300

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
| 0.3325        | 1.0   | 1250 | 0.2657          | 0.7732    | 0.8175 | 0.7947 | 0.9214   |
| 0.2242        | 2.0   | 2500 | 0.2505          | 0.7942    | 0.8289 | 0.8111 | 0.9262   |
| 0.158         | 3.0   | 3750 | 0.2539          | 0.8099    | 0.8367 | 0.8231 | 0.9294   |
| 0.1155        | 4.0   | 5000 | 0.2804          | 0.8172    | 0.8373 | 0.8271 | 0.9302   |
| 0.1047        | 5.0   | 6250 | 0.2834          | 0.8139    | 0.8367 | 0.8251 | 0.9300   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

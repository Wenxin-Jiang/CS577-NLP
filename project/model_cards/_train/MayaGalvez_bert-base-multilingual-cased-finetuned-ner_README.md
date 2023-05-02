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
- name: bert-base-multilingual-cased-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikiann
      type: wikiann
      config: en
      split: train
      args: en
    metrics:
    - name: Precision
      type: precision
      value: 0.8326536254925002
    - name: Recall
      type: recall
      value: 0.8515481408171921
    - name: F1
      type: f1
      value: 0.8419948974242476
    - name: Accuracy
      type: accuracy
      value: 0.934650342703884
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-cased-finetuned-ner

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the wikiann dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2299
- Precision: 0.8327
- Recall: 0.8515
- F1: 0.8420
- Accuracy: 0.9347

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.6617        | 0.16  | 100  | 0.3490          | 0.7259    | 0.7730 | 0.7487 | 0.8983   |
| 0.341         | 0.32  | 200  | 0.2942          | 0.7665    | 0.8052 | 0.7854 | 0.9121   |
| 0.3052        | 0.48  | 300  | 0.2821          | 0.7694    | 0.8021 | 0.7854 | 0.9152   |
| 0.2938        | 0.64  | 400  | 0.2700          | 0.7897    | 0.8122 | 0.8008 | 0.9206   |
| 0.2685        | 0.8   | 500  | 0.2482          | 0.7901    | 0.8253 | 0.8073 | 0.9242   |
| 0.2622        | 0.96  | 600  | 0.2478          | 0.7989    | 0.8298 | 0.8141 | 0.9250   |
| 0.2154        | 1.12  | 700  | 0.2456          | 0.8126    | 0.8365 | 0.8244 | 0.9273   |
| 0.2046        | 1.28  | 800  | 0.2429          | 0.8079    | 0.8335 | 0.8205 | 0.9270   |
| 0.2114        | 1.44  | 900  | 0.2377          | 0.8125    | 0.8415 | 0.8268 | 0.9300   |
| 0.2111        | 1.6   | 1000 | 0.2381          | 0.8231    | 0.8397 | 0.8313 | 0.9309   |
| 0.1934        | 1.76  | 1100 | 0.2349          | 0.8179    | 0.8485 | 0.8329 | 0.9308   |
| 0.1972        | 1.92  | 1200 | 0.2293          | 0.8287    | 0.8446 | 0.8366 | 0.9332   |
| 0.1858        | 2.08  | 1300 | 0.2366          | 0.8280    | 0.8463 | 0.8371 | 0.9327   |
| 0.1506        | 2.24  | 1400 | 0.2392          | 0.8255    | 0.8505 | 0.8378 | 0.9332   |
| 0.1508        | 2.4   | 1500 | 0.2346          | 0.8266    | 0.8465 | 0.8364 | 0.9334   |
| 0.1674        | 2.56  | 1600 | 0.2329          | 0.8249    | 0.8487 | 0.8366 | 0.9329   |
| 0.1584        | 2.72  | 1700 | 0.2309          | 0.8316    | 0.8508 | 0.8411 | 0.9341   |
| 0.154         | 2.88  | 1800 | 0.2299          | 0.8327    | 0.8515 | 0.8420 | 0.9347   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1

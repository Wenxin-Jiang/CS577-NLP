---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: xlm-roberta-large-NER-AstrID
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-large-NER-AstrID

This model is a fine-tuned version of [xlm-roberta-large-finetuned-conll03-english](https://huggingface.co/xlm-roberta-large-finetuned-conll03-english) on the [WIESP2022-NER dataset](https://huggingface.co/datasets/fgrezes/WIESP2022-NER/blob/main/ner_tags.json).
It achieves the following results on a sample evaluation set (from the dev set):
- Loss: 0.1950
- Precision: 0.8124
- Recall: 0.8140
- F1: 0.8132
- Accuracy: 0.9473

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
| No log        | 1.0   | 220  | 0.3204          | 0.6974    | 0.7064 | 0.7019 | 0.9229   |
| No log        | 2.0   | 440  | 0.2166          | 0.8083    | 0.8072 | 0.8078 | 0.9462   |
| 0.3277        | 3.0   | 660  | 0.1950          | 0.8124    | 0.8140 | 0.8132 | 0.9473   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

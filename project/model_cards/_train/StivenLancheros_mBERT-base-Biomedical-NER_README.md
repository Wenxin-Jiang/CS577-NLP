---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-base-multilingual-cased-finetuned-ner-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-cased-finetuned-ner-4
#This model is part of a test for creating multilingual BioMedical NER systems. Not intended for proffesional use now.

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the CRAFT+BC4CHEMD+BioNLP09 datasets concatenated.
It achieves the following results on the evaluation set:
- Loss: 0.1027
- Precision: 0.9830
- Recall: 0.9832
- F1: 0.9831
- Accuracy: 0.9799

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0658        | 1.0   | 6128  | 0.0751          | 0.9795    | 0.9795 | 0.9795 | 0.9758   |
| 0.0406        | 2.0   | 12256 | 0.0753          | 0.9827    | 0.9815 | 0.9821 | 0.9786   |
| 0.0182        | 3.0   | 18384 | 0.0934          | 0.9834    | 0.9825 | 0.9829 | 0.9796   |
| 0.011         | 4.0   | 24512 | 0.1027          | 0.9830    | 0.9832 | 0.9831 | 0.9799   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0

---
license: mit
tags:
- generated_from_trainer
model-index:
- name: BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext-ContaminationQAmodel_PubmedBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext-ContaminationQAmodel_PubmedBERT

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7515

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 22   | 3.9518          |
| No log        | 2.0   | 44   | 3.2703          |
| No log        | 3.0   | 66   | 2.9308          |
| No log        | 4.0   | 88   | 2.7806          |
| No log        | 5.0   | 110  | 2.6926          |
| No log        | 6.0   | 132  | 2.7043          |
| No log        | 7.0   | 154  | 2.7113          |
| No log        | 8.0   | 176  | 2.7236          |
| No log        | 9.0   | 198  | 2.7559          |
| No log        | 10.0  | 220  | 2.7515          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3

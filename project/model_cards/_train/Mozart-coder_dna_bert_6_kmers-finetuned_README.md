---
tags:
- generated_from_trainer
model-index:
- name: dna_bert_6_kmers-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dna_bert_6_kmers-finetuned

This model is a fine-tuned version of [armheb/DNA_bert_6](https://huggingface.co/armheb/DNA_bert_6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0034

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0296        | 1.0   | 250  | 0.0058          |
| 0.0025        | 2.0   | 500  | 0.0042          |
| 0.0017        | 3.0   | 750  | 0.0039          |
| 0.0014        | 4.0   | 1000 | 0.0034          |
| 0.0011        | 5.0   | 1250 | 0.0034          |
| 0.0009        | 6.0   | 1500 | 0.0034          |
| 0.0008        | 7.0   | 1750 | 0.0034          |
| 0.0007        | 8.0   | 2000 | 0.0035          |
| 0.0006        | 9.0   | 2250 | 0.0034          |
| 0.0007        | 10.0  | 2500 | 0.0034          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

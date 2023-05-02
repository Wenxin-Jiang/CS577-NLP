---
tags:
- generated_from_trainer
model-index:
- name: BERT_spring-6_tokenized
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_spring-6_tokenized

This model is a fine-tuned version of [armheb/DNA_bert_6](https://huggingface.co/armheb/DNA_bert_6) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0369

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0707        | 1.0   | 187  | 0.0406          |
| 0.0399        | 2.0   | 374  | 0.0389          |
| 0.0385        | 3.0   | 561  | 0.0362          |
| 0.0385        | 4.0   | 748  | 0.0377          |
| 0.0374        | 5.0   | 935  | 0.0358          |
| 0.0375        | 6.0   | 1122 | 0.0357          |
| 0.0375        | 7.0   | 1309 | 0.0377          |
| 0.0368        | 8.0   | 1496 | 0.0382          |
| 0.0372        | 9.0   | 1683 | 0.0363          |
| 0.0355        | 10.0  | 1870 | 0.0335          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1

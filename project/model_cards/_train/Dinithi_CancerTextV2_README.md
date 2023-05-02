---
license: cc0-1.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: CancerTextV2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CancerTextV2

This model is a fine-tuned version of [bionlp/bluebert_pubmed_uncased_L-12_H-768_A-12](https://huggingface.co/bionlp/bluebert_pubmed_uncased_L-12_H-768_A-12) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5913
- Accuracy: 0.8692
- Precision: 0.8666
- Recall: 0.8738
- F1: 0.8701

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.4717        | 1.0   | 600  | 0.3318          | 0.8617   | 0.8562    | 0.8704 | 0.8633 |
| 0.3248        | 2.0   | 1200 | 0.3144          | 0.8658   | 0.8821    | 0.8455 | 0.8634 |
| 0.2653        | 3.0   | 1800 | 0.3519          | 0.8625   | 0.8507    | 0.8804 | 0.8653 |
| 0.2164        | 4.0   | 2400 | 0.4090          | 0.8658   | 0.9002    | 0.8239 | 0.8604 |
| 0.1884        | 5.0   | 3000 | 0.4413          | 0.8667   | 0.8850    | 0.8439 | 0.8639 |
| 0.1582        | 6.0   | 3600 | 0.4415          | 0.865    | 0.8971    | 0.8256 | 0.8599 |
| 0.1377        | 7.0   | 4200 | 0.5165          | 0.8708   | 0.8694    | 0.8738 | 0.8716 |
| 0.1192        | 8.0   | 4800 | 0.5699          | 0.8675   | 0.8826    | 0.8488 | 0.8654 |
| 0.1081        | 9.0   | 5400 | 0.5837          | 0.8692   | 0.8666    | 0.8738 | 0.8701 |
| 0.1018        | 10.0  | 6000 | 0.5913          | 0.8692   | 0.8666    | 0.8738 | 0.8701 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

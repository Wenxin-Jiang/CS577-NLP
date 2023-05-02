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
- name: BlueBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BlueBERT

This model is a fine-tuned version of [bionlp/bluebert_pubmed_uncased_L-12_H-768_A-12](https://huggingface.co/bionlp/bluebert_pubmed_uncased_L-12_H-768_A-12) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6525
- Accuracy: 0.83
- Precision: 0.8767
- Recall: 0.8889
- F1: 0.8828

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.6839        | 1.0   | 50   | 0.7208          | 0.39     | 0.9231    | 0.1667 | 0.2824 |
| 0.6594        | 2.0   | 100  | 0.5862          | 0.6      | 0.9211    | 0.4861 | 0.6364 |
| 0.539         | 3.0   | 150  | 0.5940          | 0.66     | 0.9318    | 0.5694 | 0.7069 |
| 0.4765        | 4.0   | 200  | 0.5675          | 0.65     | 0.9512    | 0.5417 | 0.6903 |
| 0.3805        | 5.0   | 250  | 0.4494          | 0.79     | 0.9322    | 0.7639 | 0.8397 |
| 0.279         | 6.0   | 300  | 0.4760          | 0.84     | 0.8784    | 0.9028 | 0.8904 |
| 0.2016        | 7.0   | 350  | 0.5514          | 0.82     | 0.8553    | 0.9028 | 0.8784 |
| 0.1706        | 8.0   | 400  | 0.5353          | 0.84     | 0.8889    | 0.8889 | 0.8889 |
| 0.1164        | 9.0   | 450  | 0.7676          | 0.82     | 0.8462    | 0.9167 | 0.8800 |
| 0.1054        | 10.0  | 500  | 0.6525          | 0.83     | 0.8767    | 0.8889 | 0.8828 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

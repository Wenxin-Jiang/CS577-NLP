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
- name: correct_BERT_token_itr0_0.0001_essays_01_03_2022-15_48_47
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# correct_BERT_token_itr0_0.0001_essays_01_03_2022-15_48_47

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1801
- Precision: 0.6153
- Recall: 0.7301
- F1: 0.6678
- Accuracy: 0.9346

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 11   | 0.2746          | 0.4586    | 0.5922 | 0.5169 | 0.9031   |
| No log        | 2.0   | 22   | 0.2223          | 0.5233    | 0.6181 | 0.5668 | 0.9148   |
| No log        | 3.0   | 33   | 0.2162          | 0.5335    | 0.6699 | 0.5940 | 0.9274   |
| No log        | 4.0   | 44   | 0.2053          | 0.5989    | 0.7055 | 0.6478 | 0.9237   |
| No log        | 5.0   | 55   | 0.2123          | 0.5671    | 0.7249 | 0.6364 | 0.9267   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
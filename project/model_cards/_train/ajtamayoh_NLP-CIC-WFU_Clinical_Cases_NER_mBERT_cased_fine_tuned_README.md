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
- name: NLP-CIC-WFU_Clinical_Cases_NER_mBERT_cased_fine_tuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NLP-CIC-WFU_Clinical_Cases_NER_mBERT_cased_fine_tuned

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0501
- Precision: 0.8961
- Recall: 0.7009
- F1: 0.7865
- Accuracy: 0.9898

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 94   | 0.0484          | 0.9002    | 0.6340 | 0.7440 | 0.9876   |
| No log        | 2.0   | 188  | 0.0436          | 0.9095    | 0.6599 | 0.7649 | 0.9887   |
| No log        | 3.0   | 282  | 0.0462          | 0.8545    | 0.7043 | 0.7722 | 0.9883   |
| No log        | 4.0   | 376  | 0.0456          | 0.9058    | 0.6761 | 0.7743 | 0.9894   |
| No log        | 5.0   | 470  | 0.0447          | 0.9194    | 0.6836 | 0.7841 | 0.9900   |
| 0.0426        | 6.0   | 564  | 0.0480          | 0.8917    | 0.7026 | 0.7859 | 0.9897   |
| 0.0426        | 7.0   | 658  | 0.0501          | 0.8961    | 0.7009 | 0.7865 | 0.9898   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

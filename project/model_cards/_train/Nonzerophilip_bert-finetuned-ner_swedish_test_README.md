---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-ner_swedish_test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner_swedish_test

This model is a fine-tuned version of [KBLab/bert-base-swedish-cased-ner](https://huggingface.co/KBLab/bert-base-swedish-cased-ner) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0916
- Precision: 0.6835
- Recall: 0.6391
- F1: 0.6606
- Accuracy: 0.9788

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
| No log        | 1.0   | 128  | 0.0980          | 0.6121    | 0.5976 | 0.6048 | 0.9749   |
| No log        | 2.0   | 256  | 0.0914          | 0.7255    | 0.6568 | 0.6894 | 0.9779   |
| No log        | 3.0   | 384  | 0.0916          | 0.6835    | 0.6391 | 0.6606 | 0.9788   |


### Framework versions

- Transformers 4.19.3
- Pytorch 1.7.1
- Datasets 2.2.2
- Tokenizers 0.12.1

---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: camembert-base-wikipedia-4gb-finetuned-job-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# camembert-base-wikipedia-4gb-finetuned-job-ner

This model is a fine-tuned version of [camembert/camembert-base-wikipedia-4gb](https://huggingface.co/camembert/camembert-base-wikipedia-4gb) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0435
- Precision: 0.9134
- Recall: 0.9197
- F1: 0.9165
- Accuracy: 0.9873

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
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0463        | 1.0   | 7543 | 0.0435          | 0.9134    | 0.9197 | 0.9165 | 0.9873   |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3

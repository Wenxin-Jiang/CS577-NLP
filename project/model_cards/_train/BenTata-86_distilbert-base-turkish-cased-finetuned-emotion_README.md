---
license: mit
tags:
- generated_from_trainer
datasets:
- turkish-multiclass-dataset
metrics:
- f1
model-index:
- name: distilbert-base-turkish-cased-finetuned-emotion
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: turkish-multiclass-dataset
      type: turkish-multiclass-dataset
      config: TurkishMulticlassDataset
      split: train
      args: TurkishMulticlassDataset
    metrics:
    - name: F1
      type: f1
      value:
        f1: 0.8276613385259164
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-turkish-cased-finetuned-emotion

This model is a fine-tuned version of [dbmdz/distilbert-base-turkish-cased](https://huggingface.co/dbmdz/distilbert-base-turkish-cased) on the turkish-multiclass-dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4861
- F1: {'f1': 0.8276613385259164}

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1                         |
|:-------------:|:-----:|:----:|:---------------:|:--------------------------:|
| 0.2578        | 1.0   | 313  | 0.5459          | {'f1': 0.8212239281513611} |
| 0.381         | 2.0   | 626  | 0.4861          | {'f1': 0.8276613385259164} |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

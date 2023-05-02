---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- accuracy
- f1
model-index:
- name: distilbert-base-uncased-finetuned-emotion
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: emotion
      type: emotion
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9275
    - name: F1
      type: f1
      value: 0.9272701341146076
---


# distilbert-base-uncased-finetuned-emotion

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the [emotion]( dataset(https://huggingface.co/datasets/emotion) dataset for in the dataset in HG.  It achieves the following results on the evaluation set:
- Loss: 0.2033
- Accuracy: 0.9275
- F1: 0.9273

## Model description

This model is a copy of the model found in the book [Natural Language Processing with Transformers](https://github.com/nlp-with-transformers/notebooks/blob/main/02_classification.ipynb).

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.806         | 1.0   | 250  | 0.2954          | 0.908    | 0.9062 |
| 0.2361        | 2.0   | 500  | 0.2033          | 0.9275   | 0.9273 |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.12.1+cu113
- Datasets 1.16.1
- Tokenizers 0.10.3

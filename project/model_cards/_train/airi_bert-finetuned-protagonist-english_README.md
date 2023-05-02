---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-protagonist-english
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-protagonist-english

This model is a fine-tuned version of [Jean-Baptiste/roberta-large-ner-english](https://huggingface.co/Jean-Baptiste/roberta-large-ner-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0630
- Precision: 0.8646
- Recall: 0.8839
- F1: 0.8742
- Accuracy: 0.9876

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 25   | 0.0659          | 0.8860    | 0.9018 | 0.8938 | 0.9862   |
| No log        | 2.0   | 50   | 0.0583          | 0.8553    | 0.8705 | 0.8628 | 0.9860   |
| No log        | 3.0   | 75   | 0.0593          | 0.8728    | 0.8884 | 0.8805 | 0.9876   |
| No log        | 4.0   | 100  | 0.0622          | 0.8559    | 0.875  | 0.8653 | 0.9871   |
| No log        | 5.0   | 125  | 0.0630          | 0.8646    | 0.8839 | 0.8742 | 0.9876   |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.2+cu102
- Datasets 2.2.1
- Tokenizers 0.11.0

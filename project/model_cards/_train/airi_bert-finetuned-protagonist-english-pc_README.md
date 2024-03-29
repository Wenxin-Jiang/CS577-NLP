---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-protagonist-english-pc
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-protagonist-english-pc

This model is a fine-tuned version of [Jean-Baptiste/roberta-large-ner-english](https://huggingface.co/Jean-Baptiste/roberta-large-ner-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0351
- Precision: 0.9513
- Recall: 0.9598
- F1: 0.9556
- Accuracy: 0.9919

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 100  | 0.0407          | 0.9254    | 0.9420 | 0.9336 | 0.9908   |
| No log        | 2.0   | 200  | 0.0351          | 0.9513    | 0.9598 | 0.9556 | 0.9919   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.10.1+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1

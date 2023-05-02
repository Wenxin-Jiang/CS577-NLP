---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: banglabert-bert-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# banglabert-bert-finetuned-ner

This model is a fine-tuned version of [csebuetnlp/banglabert](https://huggingface.co/csebuetnlp/banglabert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9526
- Precision: 0.0143
- Recall: 0.0769
- F1: 0.0241
- Accuracy: 0.0143

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
| No log        | 1.0   | 1    | 2.0085          | 0.0143    | 0.0769 | 0.0241 | 0.0143   |
| No log        | 2.0   | 2    | 1.9711          | 0.0143    | 0.0769 | 0.0241 | 0.0143   |
| No log        | 3.0   | 3    | 1.9526          | 0.0143    | 0.0769 | 0.0241 | 0.0143   |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

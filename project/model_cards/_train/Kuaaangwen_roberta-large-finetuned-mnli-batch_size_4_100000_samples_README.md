---
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: roberta-large-finetuned-mnli-batch_size_4_100000_samples
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      config: mnli
      split: train
      args: mnli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.3544574630667346
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-finetuned-mnli-batch_size_4_100000_samples

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0980
- Accuracy: 0.3545

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 1.1026        | 1.0   | 25000 | 1.0980          | 0.3545   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2

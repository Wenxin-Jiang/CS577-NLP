---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- financial_phrasebank
metrics:
- recall
- accuracy
- precision
model-index:
- name: TOMFINSEN
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: financial_phrasebank
      type: financial_phrasebank
      args: sentences_50agree
    metrics:
    - name: Recall
      type: recall
      value: 0.8985861629736692
    - name: Accuracy
      type: accuracy
      value: 0.8742268041237113
    - name: Precision
      type: precision
      value: 0.8509995913451198
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# TOMFINSEN

This model is a fine-tuned version of [deepmind/language-perceiver](https://huggingface.co/deepmind/language-perceiver) on the financial_phrasebank dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3642
- Recall: 0.8986
- Accuracy: 0.8742
- Precision: 0.8510

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
- distributed_type: tpu
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Recall | Accuracy | Precision |
|:-------------:|:-----:|:----:|:---------------:|:------:|:--------:|:---------:|
| 0.5403        | 1.0   | 273  | 0.4207          | 0.8358 | 0.8619   | 0.8534    |
| 0.3939        | 2.0   | 546  | 0.3750          | 0.8943 | 0.8577   | 0.8225    |
| 0.1993        | 3.0   | 819  | 0.3113          | 0.8882 | 0.8660   | 0.8367    |
| 0.301         | 4.0   | 1092 | 0.3642          | 0.8986 | 0.8742   | 0.8510    |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.9.0+cu102
- Datasets 1.17.0
- Tokenizers 0.10.3

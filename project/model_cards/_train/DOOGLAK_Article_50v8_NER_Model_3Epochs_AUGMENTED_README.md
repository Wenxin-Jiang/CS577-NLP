---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article50v8_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_50v8_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article50v8_wikigold_split
      type: article50v8_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.2690246516613076
    - name: Recall
      type: recall
      value: 0.12291870714985309
    - name: F1
      type: f1
      value: 0.16873949579831934
    - name: Accuracy
      type: accuracy
      value: 0.8202619500727639
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_50v8_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article50v8_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4522
- Precision: 0.2690
- Recall: 0.1229
- F1: 0.1687
- Accuracy: 0.8203

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
| No log        | 1.0   | 21   | 0.6437          | 0.5       | 0.0002 | 0.0005 | 0.7791   |
| No log        | 2.0   | 42   | 0.4851          | 0.2420    | 0.0737 | 0.1130 | 0.8050   |
| No log        | 3.0   | 63   | 0.4522          | 0.2690    | 0.1229 | 0.1687 | 0.8203   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

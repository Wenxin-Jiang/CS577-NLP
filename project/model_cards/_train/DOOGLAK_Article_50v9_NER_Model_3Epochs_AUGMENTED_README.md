---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article50v9_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_50v9_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article50v9_wikigold_split
      type: article50v9_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.28292682926829266
    - name: Recall
      type: recall
      value: 0.04238733252131547
    - name: F1
      type: f1
      value: 0.07372881355932202
    - name: Accuracy
      type: accuracy
      value: 0.7937647190759224
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_50v9_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article50v9_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5331
- Precision: 0.2829
- Recall: 0.0424
- F1: 0.0737
- Accuracy: 0.7938

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
| No log        | 1.0   | 18   | 0.7018          | 0.6       | 0.0007 | 0.0015 | 0.7808   |
| No log        | 2.0   | 36   | 0.5626          | 0.3850    | 0.0339 | 0.0622 | 0.7900   |
| No log        | 3.0   | 54   | 0.5331          | 0.2829    | 0.0424 | 0.0737 | 0.7938   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v3_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v3_NER_Model_3Epochs_UNAUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v3_wikigold_split
      type: article250v3_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.46615905245346867
    - name: Recall
      type: recall
      value: 0.47094017094017093
    - name: F1
      type: f1
      value: 0.4685374149659864
    - name: Accuracy
      type: accuracy
      value: 0.8992223869340199
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v3_NER_Model_3Epochs_UNAUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v3_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2795
- Precision: 0.4662
- Recall: 0.4709
- F1: 0.4685
- Accuracy: 0.8992

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
| No log        | 1.0   | 33   | 0.4736          | 0.1634    | 0.0755 | 0.1033 | 0.8223   |
| No log        | 2.0   | 66   | 0.3129          | 0.3483    | 0.3276 | 0.3376 | 0.8831   |
| No log        | 3.0   | 99   | 0.2795          | 0.4662    | 0.4709 | 0.4685 | 0.8992   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

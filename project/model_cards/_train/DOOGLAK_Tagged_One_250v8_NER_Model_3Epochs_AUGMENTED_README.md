---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one250v8_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_250v8_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one250v8_wikigold_split
      type: tagged_one250v8_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.5351851851851852
    - name: Recall
      type: recall
      value: 0.4795353982300885
    - name: F1
      type: f1
      value: 0.5058343057176197
    - name: Accuracy
      type: accuracy
      value: 0.8947195053970506
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_250v8_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one250v8_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3389
- Precision: 0.5352
- Recall: 0.4795
- F1: 0.5058
- Accuracy: 0.8947

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
| No log        | 1.0   | 95   | 0.4305          | 0.3497    | 0.1814 | 0.2389 | 0.8488   |
| No log        | 2.0   | 190  | 0.3469          | 0.4995    | 0.4281 | 0.4611 | 0.8875   |
| No log        | 3.0   | 285  | 0.3389          | 0.5352    | 0.4795 | 0.5058 | 0.8947   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one250v0_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_250v0_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one250v0_wikigold_split
      type: tagged_one250v0_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.5125421190565331
    - name: Recall
      type: recall
      value: 0.3694009713977334
    - name: F1
      type: f1
      value: 0.4293554963148816
    - name: Accuracy
      type: accuracy
      value: 0.8786972744569918
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_250v0_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one250v0_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4287
- Precision: 0.5125
- Recall: 0.3694
- F1: 0.4294
- Accuracy: 0.8787

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
| No log        | 1.0   | 96   | 0.4352          | 0.3056    | 0.1692 | 0.2178 | 0.8448   |
| No log        | 2.0   | 192  | 0.3881          | 0.4394    | 0.3295 | 0.3766 | 0.8773   |
| No log        | 3.0   | 288  | 0.4287          | 0.5125    | 0.3694 | 0.4294 | 0.8787   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

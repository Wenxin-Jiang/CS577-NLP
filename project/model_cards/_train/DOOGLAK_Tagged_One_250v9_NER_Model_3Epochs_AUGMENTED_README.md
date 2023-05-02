---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one250v9_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_250v9_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one250v9_wikigold_split
      type: tagged_one250v9_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.5794920037629351
    - name: Recall
      type: recall
      value: 0.5334872979214781
    - name: F1
      type: f1
      value: 0.5555388546520367
    - name: Accuracy
      type: accuracy
      value: 0.9034831230122089
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_250v9_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one250v9_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3012
- Precision: 0.5795
- Recall: 0.5335
- F1: 0.5555
- Accuracy: 0.9035

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
| No log        | 1.0   | 90   | 0.3614          | 0.2860    | 0.1969 | 0.2332 | 0.8576   |
| No log        | 2.0   | 180  | 0.3317          | 0.5186    | 0.4596 | 0.4873 | 0.8924   |
| No log        | 3.0   | 270  | 0.3012          | 0.5795    | 0.5335 | 0.5555 | 0.9035   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

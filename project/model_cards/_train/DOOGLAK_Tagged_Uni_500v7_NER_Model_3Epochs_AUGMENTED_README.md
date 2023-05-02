---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni500v7_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_500v7_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni500v7_wikigold_split
      type: tagged_uni500v7_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.7087020648967551
    - name: Recall
      type: recall
      value: 0.7068775285031261
    - name: F1
      type: f1
      value: 0.7077886208801325
    - name: Accuracy
      type: accuracy
      value: 0.9310942373735782
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_500v7_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni500v7_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2465
- Precision: 0.7087
- Recall: 0.7069
- F1: 0.7078
- Accuracy: 0.9311

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
| No log        | 1.0   | 154  | 0.3027          | 0.5778    | 0.4917 | 0.5313 | 0.9053   |
| No log        | 2.0   | 308  | 0.2317          | 0.6818    | 0.6973 | 0.6895 | 0.9293   |
| No log        | 3.0   | 462  | 0.2465          | 0.7087    | 0.7069 | 0.7078 | 0.9311   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

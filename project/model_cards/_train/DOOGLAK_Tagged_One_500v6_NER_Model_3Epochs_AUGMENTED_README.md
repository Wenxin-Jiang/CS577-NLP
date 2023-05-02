---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one500v6_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_500v6_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one500v6_wikigold_split
      type: tagged_one500v6_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6866690621631333
    - name: Recall
      type: recall
      value: 0.6719409282700421
    - name: F1
      type: f1
      value: 0.679225164385996
    - name: Accuracy
      type: accuracy
      value: 0.9239838169290094
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_500v6_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one500v6_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2690
- Precision: 0.6867
- Recall: 0.6719
- F1: 0.6792
- Accuracy: 0.9240

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
| No log        | 1.0   | 189  | 0.2819          | 0.6009    | 0.5352 | 0.5661 | 0.9105   |
| No log        | 2.0   | 378  | 0.2614          | 0.6743    | 0.6406 | 0.6571 | 0.9201   |
| 0.11          | 3.0   | 567  | 0.2690          | 0.6867    | 0.6719 | 0.6792 | 0.9240   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

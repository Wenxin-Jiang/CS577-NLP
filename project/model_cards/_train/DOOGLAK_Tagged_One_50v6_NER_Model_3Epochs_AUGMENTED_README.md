---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one50v6_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_50v6_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one50v6_wikigold_split
      type: tagged_one50v6_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.0625
    - name: Recall
      type: recall
      value: 0.0004854368932038835
    - name: F1
      type: f1
      value: 0.0009633911368015415
    - name: Accuracy
      type: accuracy
      value: 0.7775310137514861
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_50v6_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one50v6_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6728
- Precision: 0.0625
- Recall: 0.0005
- F1: 0.0010
- Accuracy: 0.7775

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
| No log        | 1.0   | 16   | 0.7728          | 0.0       | 0.0    | 0.0    | 0.7773   |
| No log        | 2.0   | 32   | 0.6898          | 0.04      | 0.0002 | 0.0005 | 0.7774   |
| No log        | 3.0   | 48   | 0.6728          | 0.0625    | 0.0005 | 0.0010 | 0.7775   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

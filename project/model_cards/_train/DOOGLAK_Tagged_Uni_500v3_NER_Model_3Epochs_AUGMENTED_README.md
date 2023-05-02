---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni500v3_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_500v3_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni500v3_wikigold_split
      type: tagged_uni500v3_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.7143812709030101
    - name: Recall
      type: recall
      value: 0.7115256495669554
    - name: F1
      type: f1
      value: 0.7129506008010682
    - name: Accuracy
      type: accuracy
      value: 0.9340035371870055
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_500v3_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni500v3_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2350
- Precision: 0.7144
- Recall: 0.7115
- F1: 0.7130
- Accuracy: 0.9340

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
| No log        | 1.0   | 172  | 0.2361          | 0.6056    | 0.5596 | 0.5817 | 0.9194   |
| No log        | 2.0   | 344  | 0.2236          | 0.6872    | 0.6922 | 0.6897 | 0.9315   |
| 0.1011        | 3.0   | 516  | 0.2350          | 0.7144    | 0.7115 | 0.7130 | 0.9340   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

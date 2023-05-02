---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni250v8_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_250v8_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni250v8_wikigold_split
      type: tagged_uni250v8_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.5548306927617273
    - name: Recall
      type: recall
      value: 0.4939159292035398
    - name: F1
      type: f1
      value: 0.5226042428675933
    - name: Accuracy
      type: accuracy
      value: 0.8976334059696954
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_250v8_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni250v8_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3186
- Precision: 0.5548
- Recall: 0.4939
- F1: 0.5226
- Accuracy: 0.8976

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
| No log        | 1.0   | 95   | 0.4132          | 0.3646    | 0.2008 | 0.2590 | 0.8504   |
| No log        | 2.0   | 190  | 0.2983          | 0.5077    | 0.4552 | 0.4800 | 0.8977   |
| No log        | 3.0   | 285  | 0.3186          | 0.5548    | 0.4939 | 0.5226 | 0.8976   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one250v2_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_250v2_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one250v2_wikigold_split
      type: tagged_one250v2_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.5859220092531394
    - name: Recall
      type: recall
      value: 0.5074413279908414
    - name: F1
      type: f1
      value: 0.5438650306748466
    - name: Accuracy
      type: accuracy
      value: 0.8979617609173338
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_250v2_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one250v2_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3573
- Precision: 0.5859
- Recall: 0.5074
- F1: 0.5439
- Accuracy: 0.8980

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
| No log        | 1.0   | 93   | 0.3884          | 0.2899    | 0.2006 | 0.2371 | 0.8583   |
| No log        | 2.0   | 186  | 0.3502          | 0.5467    | 0.4705 | 0.5058 | 0.8937   |
| No log        | 3.0   | 279  | 0.3573          | 0.5859    | 0.5074 | 0.5439 | 0.8980   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

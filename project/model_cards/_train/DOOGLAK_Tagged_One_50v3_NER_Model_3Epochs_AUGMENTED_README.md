---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one50v3_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_50v3_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one50v3_wikigold_split
      type: tagged_one50v3_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.13106796116504854
    - name: Recall
      type: recall
      value: 0.006622516556291391
    - name: F1
      type: f1
      value: 0.012607985057202896
    - name: Accuracy
      type: accuracy
      value: 0.7834701450579107
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_50v3_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one50v3_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6197
- Precision: 0.1311
- Recall: 0.0066
- F1: 0.0126
- Accuracy: 0.7835

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
| No log        | 1.0   | 14   | 0.7544          | 0.0       | 0.0    | 0.0    | 0.7789   |
| No log        | 2.0   | 28   | 0.6444          | 0.0746    | 0.0025 | 0.0047 | 0.7818   |
| No log        | 3.0   | 42   | 0.6197          | 0.1311    | 0.0066 | 0.0126 | 0.7835   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

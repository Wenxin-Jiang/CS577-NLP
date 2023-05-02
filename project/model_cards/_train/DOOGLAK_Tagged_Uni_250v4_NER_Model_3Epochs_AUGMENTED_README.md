---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni250v4_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_250v4_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni250v4_wikigold_split
      type: tagged_uni250v4_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.5477564102564103
    - name: Recall
      type: recall
      value: 0.4741953385127636
    - name: F1
      type: f1
      value: 0.5083283759666866
    - name: Accuracy
      type: accuracy
      value: 0.8982782455699384
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_250v4_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni250v4_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2997
- Precision: 0.5478
- Recall: 0.4742
- F1: 0.5083
- Accuracy: 0.8983

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
| No log        | 1.0   | 86   | 0.3911          | 0.3370    | 0.1792 | 0.2340 | 0.8515   |
| No log        | 2.0   | 172  | 0.3347          | 0.4754    | 0.3760 | 0.4199 | 0.8836   |
| No log        | 3.0   | 258  | 0.2997          | 0.5478    | 0.4742 | 0.5083 | 0.8983   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

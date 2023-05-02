---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: albert-large-v2_ner_conll2003
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9396018069265518
    - name: Recall
      type: recall
      value: 0.9451363177381353
    - name: F1
      type: f1
      value: 0.9423609363201612
    - name: Accuracy
      type: accuracy
      value: 0.9874810170943499
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-large-v2_ner_conll2003

This model is a fine-tuned version of [albert-large-v2](https://huggingface.co/albert-large-v2) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0584
- Precision: 0.9396
- Recall: 0.9451
- F1: 0.9424
- Accuracy: 0.9875

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2034        | 1.0   | 878  | 0.0653          | 0.9114    | 0.9278 | 0.9195 | 0.9837   |
| 0.0561        | 2.0   | 1756 | 0.0602          | 0.9316    | 0.9280 | 0.9298 | 0.9845   |
| 0.0303        | 3.0   | 2634 | 0.0536          | 0.9380    | 0.9424 | 0.9402 | 0.9872   |
| 0.0177        | 4.0   | 3512 | 0.0535          | 0.9393    | 0.9456 | 0.9425 | 0.9877   |
| 0.011         | 5.0   | 4390 | 0.0584          | 0.9396    | 0.9451 | 0.9424 | 0.9875   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

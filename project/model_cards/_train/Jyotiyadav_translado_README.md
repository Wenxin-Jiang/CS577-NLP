---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- sroie
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Translado
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: sroie
      type: sroie
      config: discharge
      split: test
      args: discharge
    metrics:
    - name: Precision
      type: precision
      value: 0.9483568075117371
    - name: Recall
      type: recall
      value: 0.9950738916256158
    - name: F1
      type: f1
      value: 0.9711538461538461
    - name: Accuracy
      type: accuracy
      value: 0.9977316915100454
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Translado

This model is a fine-tuned version of [microsoft/layoutlmv3-large](https://huggingface.co/microsoft/layoutlmv3-large) on the sroie dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0307
- Precision: 0.9484
- Recall: 0.9951
- F1: 0.9712
- Accuracy: 0.9977

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 1000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 4.17  | 100  | 0.0244          | 0.9484    | 0.9951 | 0.9712 | 0.9977   |
| No log        | 8.33  | 200  | 0.0265          | 0.9484    | 0.9951 | 0.9712 | 0.9977   |
| No log        | 12.5  | 300  | 0.0277          | 0.9484    | 0.9951 | 0.9712 | 0.9977   |
| No log        | 16.67 | 400  | 0.0286          | 0.9484    | 0.9951 | 0.9712 | 0.9977   |
| 0.0134        | 20.83 | 500  | 0.0293          | 0.9484    | 0.9951 | 0.9712 | 0.9977   |
| 0.0134        | 25.0  | 600  | 0.0298          | 0.9484    | 0.9951 | 0.9712 | 0.9977   |
| 0.0134        | 29.17 | 700  | 0.0302          | 0.9484    | 0.9951 | 0.9712 | 0.9977   |
| 0.0134        | 33.33 | 800  | 0.0305          | 0.9484    | 0.9951 | 0.9712 | 0.9977   |
| 0.0134        | 37.5  | 900  | 0.0306          | 0.9484    | 0.9951 | 0.9712 | 0.9977   |
| 0.0           | 41.67 | 1000 | 0.0307          | 0.9484    | 0.9951 | 0.9712 | 0.9977   |


### Framework versions

- Transformers 4.27.0.dev0
- Pytorch 1.13.1+cu116
- Datasets 2.2.2
- Tokenizers 0.13.2

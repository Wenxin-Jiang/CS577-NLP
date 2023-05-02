---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- cord-layoutlmv3
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: layoutlmv3-finetuned-cord_100
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: cord-layoutlmv3
      type: cord-layoutlmv3
      config: cord
      split: train
      args: cord
    metrics:
    - name: Precision
      type: precision
      value: 0.9022777369581191
    - name: Recall
      type: recall
      value: 0.9191616766467066
    - name: F1
      type: f1
      value: 0.9106414534668149
    - name: Accuracy
      type: accuracy
      value: 0.9202037351443124
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-cord_100

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the cord-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3848
- Precision: 0.9023
- Recall: 0.9192
- F1: 0.9106
- Accuracy: 0.9202

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
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 2500

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 6.25  | 250  | 0.9576          | 0.7878    | 0.8196 | 0.8034 | 0.8166   |
| 1.3167        | 12.5  | 500  | 0.5210          | 0.8536    | 0.8772 | 0.8653 | 0.8846   |
| 1.3167        | 18.75 | 750  | 0.4077          | 0.8798    | 0.9042 | 0.8918 | 0.9113   |
| 0.2603        | 25.0  | 1000 | 0.3943          | 0.8902    | 0.9102 | 0.9001 | 0.9147   |
| 0.2603        | 31.25 | 1250 | 0.3691          | 0.8980    | 0.9162 | 0.9070 | 0.9194   |
| 0.1009        | 37.5  | 1500 | 0.3496          | 0.9130    | 0.9274 | 0.9202 | 0.9266   |
| 0.1009        | 43.75 | 1750 | 0.3700          | 0.9078    | 0.9214 | 0.9146 | 0.9266   |
| 0.056         | 50.0  | 2000 | 0.3724          | 0.9065    | 0.9214 | 0.9139 | 0.9215   |
| 0.056         | 56.25 | 2250 | 0.3773          | 0.9051    | 0.9207 | 0.9128 | 0.9202   |
| 0.0413        | 62.5  | 2500 | 0.3848          | 0.9023    | 0.9192 | 0.9106 | 0.9202   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

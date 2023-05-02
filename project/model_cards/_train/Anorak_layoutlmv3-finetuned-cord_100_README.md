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
      value: 0.917960088691796
    - name: Recall
      type: recall
      value: 0.9296407185628742
    - name: F1
      type: f1
      value: 0.9237634808478989
    - name: Accuracy
      type: accuracy
      value: 0.9303904923599321
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-cord_100

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the cord-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2854
- Precision: 0.9180
- Recall: 0.9296
- F1: 0.9238
- Accuracy: 0.9304

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
- training_steps: 2500

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 0.62  | 250  | 1.2967          | 0.6175    | 0.7021 | 0.6571 | 0.7296   |
| 1.6872        | 1.25  | 500  | 0.7576          | 0.8140    | 0.8383 | 0.8260 | 0.8383   |
| 1.6872        | 1.88  | 750  | 0.5695          | 0.8301    | 0.8518 | 0.8408 | 0.8544   |
| 0.6109        | 2.5   | 1000 | 0.4778          | 0.8564    | 0.875  | 0.8656 | 0.8812   |
| 0.6109        | 3.12  | 1250 | 0.3825          | 0.8694    | 0.8922 | 0.8807 | 0.8986   |
| 0.3905        | 3.75  | 1500 | 0.3546          | 0.8831    | 0.9049 | 0.8939 | 0.9143   |
| 0.3905        | 4.38  | 1750 | 0.3153          | 0.8998    | 0.9207 | 0.9101 | 0.9223   |
| 0.275         | 5.0   | 2000 | 0.3065          | 0.8926    | 0.9147 | 0.9035 | 0.9202   |
| 0.275         | 5.62  | 2250 | 0.2872          | 0.9131    | 0.9281 | 0.9206 | 0.9291   |
| 0.2275        | 6.25  | 2500 | 0.2854          | 0.9180    | 0.9296 | 0.9238 | 0.9304   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cpu
- Datasets 2.8.0
- Tokenizers 0.13.2

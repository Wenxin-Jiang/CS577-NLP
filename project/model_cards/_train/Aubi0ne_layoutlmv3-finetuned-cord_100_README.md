---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- cord
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
      name: cord
      type: cord
      args: cord
    metrics:
    - name: Precision
      type: precision
      value: 0.9174649963154016
    - name: Recall
      type: recall
      value: 0.9318862275449101
    - name: F1
      type: f1
      value: 0.9246193835870776
    - name: Accuracy
      type: accuracy
      value: 0.9405772495755518
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-cord_100

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the cord dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2834
- Precision: 0.9175
- Recall: 0.9319
- F1: 0.9246
- Accuracy: 0.9406

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
| No log        | 4.17  | 250  | 1.0175          | 0.7358    | 0.7882 | 0.7611 | 0.8014   |
| 1.406         | 8.33  | 500  | 0.5646          | 0.8444    | 0.8735 | 0.8587 | 0.8671   |
| 1.406         | 12.5  | 750  | 0.3943          | 0.8950    | 0.9184 | 0.9065 | 0.9189   |
| 0.3467        | 16.67 | 1000 | 0.3379          | 0.9138    | 0.9289 | 0.9213 | 0.9291   |
| 0.3467        | 20.83 | 1250 | 0.2842          | 0.9189    | 0.9334 | 0.9261 | 0.9419   |
| 0.1484        | 25.0  | 1500 | 0.2822          | 0.9233    | 0.9371 | 0.9302 | 0.9427   |
| 0.1484        | 29.17 | 1750 | 0.2906          | 0.9168    | 0.9319 | 0.9243 | 0.9372   |
| 0.0825        | 33.33 | 2000 | 0.2922          | 0.9183    | 0.9334 | 0.9258 | 0.9410   |
| 0.0825        | 37.5  | 2250 | 0.2842          | 0.9154    | 0.9319 | 0.9236 | 0.9397   |
| 0.0596        | 41.67 | 2500 | 0.2834          | 0.9175    | 0.9319 | 0.9246 | 0.9406   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

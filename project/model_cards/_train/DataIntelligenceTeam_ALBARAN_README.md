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
- name: ALBARAN
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: sroie
      type: sroie
      config: discharge
      split: train
      args: discharge
    metrics:
    - name: Precision
      type: precision
      value: 0.9253731343283582
    - name: Recall
      type: recall
      value: 0.9253731343283582
    - name: F1
      type: f1
      value: 0.9253731343283582
    - name: Accuracy
      type: accuracy
      value: 0.9877488514548239
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ALBARAN

This model is a fine-tuned version of [microsoft/layoutlmv3-large](https://huggingface.co/microsoft/layoutlmv3-large) on the ALBARAN dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1056
- Precision: 0.9254
- Recall: 0.9254
- F1: 0.9254
- Accuracy: 0.9877

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
| No log        | 8.33  | 100  | 0.0782          | 0.9403    | 0.9403 | 0.9403 | 0.9893   |
| No log        | 16.67 | 200  | 0.0650          | 0.9403    | 0.9403 | 0.9403 | 0.9908   |
| No log        | 25.0  | 300  | 0.0960          | 0.9104    | 0.9104 | 0.9104 | 0.9862   |
| No log        | 33.33 | 400  | 0.1052          | 0.9104    | 0.9104 | 0.9104 | 0.9862   |
| 0.0746        | 41.67 | 500  | 0.1007          | 0.9254    | 0.9254 | 0.9254 | 0.9877   |
| 0.0746        | 50.0  | 600  | 0.1033          | 0.9254    | 0.9254 | 0.9254 | 0.9877   |
| 0.0746        | 58.33 | 700  | 0.1047          | 0.9254    | 0.9254 | 0.9254 | 0.9877   |
| 0.0746        | 66.67 | 800  | 0.1049          | 0.9254    | 0.9254 | 0.9254 | 0.9877   |
| 0.0746        | 75.0  | 900  | 0.1053          | 0.9254    | 0.9254 | 0.9254 | 0.9877   |
| 0.0007        | 83.33 | 1000 | 0.1056          | 0.9254    | 0.9254 | 0.9254 | 0.9877   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.2.2
- Tokenizers 0.13.2

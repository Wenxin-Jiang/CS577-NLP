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
      value: 0.9415680473372781
    - name: Recall
      type: recall
      value: 0.9528443113772455
    - name: F1
      type: f1
      value: 0.947172619047619
    - name: Accuracy
      type: accuracy
      value: 0.9592529711375212
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-cord_100

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the cord-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2132
- Precision: 0.9416
- Recall: 0.9528
- F1: 0.9472
- Accuracy: 0.9593

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
| No log        | 1.56  | 250  | 1.0604          | 0.7085    | 0.7732 | 0.7394 | 0.7806   |
| 1.4262        | 3.12  | 500  | 0.5754          | 0.8504    | 0.8683 | 0.8593 | 0.8705   |
| 1.4262        | 4.69  | 750  | 0.4026          | 0.8949    | 0.9109 | 0.9028 | 0.9189   |
| 0.4088        | 6.25  | 1000 | 0.3129          | 0.9232    | 0.9356 | 0.9294 | 0.9406   |
| 0.4088        | 7.81  | 1250 | 0.2691          | 0.9290    | 0.9401 | 0.9345 | 0.9452   |
| 0.2193        | 9.38  | 1500 | 0.2260          | 0.9278    | 0.9431 | 0.9354 | 0.9499   |
| 0.2193        | 10.94 | 1750 | 0.2447          | 0.9260    | 0.9371 | 0.9315 | 0.9469   |
| 0.1547        | 12.5  | 2000 | 0.2113          | 0.9394    | 0.9521 | 0.9457 | 0.9601   |
| 0.1547        | 14.06 | 2250 | 0.2138          | 0.9430    | 0.9543 | 0.9487 | 0.9605   |
| 0.1163        | 15.62 | 2500 | 0.2132          | 0.9416    | 0.9528 | 0.9472 | 0.9593   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

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
- name: LayoutLMv3-Finetuned-CORD_100
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
      value: 0.9524870081662955
    - name: Recall
      type: recall
      value: 0.9603293413173652
    - name: F1
      type: f1
      value: 0.9563920983973164
    - name: Accuracy
      type: accuracy
      value: 0.9647707979626485
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# LayoutLMv3-Finetuned-CORD_100

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the cord-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1948
- Precision: 0.9525
- Recall: 0.9603
- F1: 0.9564
- Accuracy: 0.9648

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1.1e-05
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.56  | 250  | 0.9568          | 0.7298    | 0.7844 | 0.7561 | 0.7992   |
| 1.3271        | 3.12  | 500  | 0.5239          | 0.8398    | 0.8713 | 0.8553 | 0.8858   |
| 1.3271        | 4.69  | 750  | 0.3586          | 0.8945    | 0.9207 | 0.9074 | 0.9300   |
| 0.3495        | 6.25  | 1000 | 0.2716          | 0.9298    | 0.9416 | 0.9357 | 0.9410   |
| 0.3495        | 7.81  | 1250 | 0.2331          | 0.9198    | 0.9356 | 0.9276 | 0.9474   |
| 0.1725        | 9.38  | 1500 | 0.2134          | 0.9379    | 0.9499 | 0.9438 | 0.9529   |
| 0.1725        | 10.94 | 1750 | 0.2079          | 0.9401    | 0.9513 | 0.9457 | 0.9605   |
| 0.1116        | 12.5  | 2000 | 0.1992          | 0.9554    | 0.9618 | 0.9586 | 0.9656   |
| 0.1116        | 14.06 | 2250 | 0.1941          | 0.9517    | 0.9588 | 0.9553 | 0.9631   |
| 0.0762        | 15.62 | 2500 | 0.1966          | 0.9503    | 0.9588 | 0.9545 | 0.9639   |
| 0.0762        | 17.19 | 2750 | 0.1951          | 0.9510    | 0.9588 | 0.9549 | 0.9626   |
| 0.0636        | 18.75 | 3000 | 0.1948          | 0.9525    | 0.9603 | 0.9564 | 0.9648   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

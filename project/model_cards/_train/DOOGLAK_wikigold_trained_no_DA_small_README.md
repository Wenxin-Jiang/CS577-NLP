---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikigold_splits
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: wikigold_trained_no_DA_small
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wikigold_splits
      type: wikigold_splits
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.34285714285714286
    - name: Recall
      type: recall
      value: 0.5454545454545454
    - name: F1
      type: f1
      value: 0.42105263157894735
    - name: Accuracy
      type: accuracy
      value: 0.853035143769968
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wikigold_trained_no_DA_small

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the wikigold_splits dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6066
- Precision: 0.3429
- Recall: 0.5455
- F1: 0.4211
- Accuracy: 0.8530

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
- num_epochs: 32

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 9    | 0.8525          | 0.0       | 0.0    | 0.0    | 0.7604   |
| No log        | 2.0   | 18   | 0.7135          | 0.0       | 0.0    | 0.0    | 0.7604   |
| No log        | 3.0   | 27   | 0.5972          | 0.1579    | 0.1364 | 0.1463 | 0.7923   |
| No log        | 4.0   | 36   | 0.5108          | 0.0769    | 0.0909 | 0.0833 | 0.8083   |
| No log        | 5.0   | 45   | 0.4725          | 0.2333    | 0.3182 | 0.2692 | 0.8466   |
| No log        | 6.0   | 54   | 0.4569          | 0.2333    | 0.3182 | 0.2692 | 0.8339   |
| No log        | 7.0   | 63   | 0.4428          | 0.2258    | 0.3182 | 0.2642 | 0.8371   |
| No log        | 8.0   | 72   | 0.4362          | 0.2121    | 0.3182 | 0.2545 | 0.8435   |
| No log        | 9.0   | 81   | 0.4509          | 0.2258    | 0.3182 | 0.2642 | 0.8403   |
| No log        | 10.0  | 90   | 0.4614          | 0.2121    | 0.3182 | 0.2545 | 0.8466   |
| No log        | 11.0  | 99   | 0.4546          | 0.2188    | 0.3182 | 0.2593 | 0.8435   |
| No log        | 12.0  | 108  | 0.4734          | 0.2188    | 0.3182 | 0.2593 | 0.8435   |
| No log        | 13.0  | 117  | 0.5098          | 0.2581    | 0.3636 | 0.3019 | 0.8466   |
| No log        | 14.0  | 126  | 0.5280          | 0.2258    | 0.3182 | 0.2642 | 0.8435   |
| No log        | 15.0  | 135  | 0.5264          | 0.2188    | 0.3182 | 0.2593 | 0.8435   |
| No log        | 16.0  | 144  | 0.5317          | 0.2727    | 0.4091 | 0.3273 | 0.8498   |
| No log        | 17.0  | 153  | 0.5414          | 0.2581    | 0.3636 | 0.3019 | 0.8466   |
| No log        | 18.0  | 162  | 0.5505          | 0.2581    | 0.3636 | 0.3019 | 0.8466   |
| No log        | 19.0  | 171  | 0.5521          | 0.2581    | 0.3636 | 0.3019 | 0.8466   |
| No log        | 20.0  | 180  | 0.5627          | 0.2581    | 0.3636 | 0.3019 | 0.8466   |
| No log        | 21.0  | 189  | 0.5687          | 0.2581    | 0.3636 | 0.3019 | 0.8466   |
| No log        | 22.0  | 198  | 0.5751          | 0.2581    | 0.3636 | 0.3019 | 0.8466   |
| No log        | 23.0  | 207  | 0.5825          | 0.2727    | 0.4091 | 0.3273 | 0.8498   |
| No log        | 24.0  | 216  | 0.5881          | 0.2727    | 0.4091 | 0.3273 | 0.8498   |
| No log        | 25.0  | 225  | 0.5930          | 0.2727    | 0.4091 | 0.3273 | 0.8498   |
| No log        | 26.0  | 234  | 0.5969          | 0.2727    | 0.4091 | 0.3273 | 0.8498   |
| No log        | 27.0  | 243  | 0.5995          | 0.3429    | 0.5455 | 0.4211 | 0.8530   |
| No log        | 28.0  | 252  | 0.6017          | 0.3429    | 0.5455 | 0.4211 | 0.8530   |
| No log        | 29.0  | 261  | 0.6035          | 0.3429    | 0.5455 | 0.4211 | 0.8530   |
| No log        | 30.0  | 270  | 0.6053          | 0.3429    | 0.5455 | 0.4211 | 0.8530   |
| No log        | 31.0  | 279  | 0.6063          | 0.3429    | 0.5455 | 0.4211 | 0.8530   |
| No log        | 32.0  | 288  | 0.6066          | 0.3429    | 0.5455 | 0.4211 | 0.8530   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6

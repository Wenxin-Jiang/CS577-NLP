---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- wildreceipt
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: layoutlmv3-finetuned-wildreceipt
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wildreceipt
      type: wildreceipt
      config: WildReceipt
      split: train
      args: WildReceipt
    metrics:
    - name: Precision
      type: precision
      value: 0.8693453601202679
    - name: Recall
      type: recall
      value: 0.8753268198706481
    - name: F1
      type: f1
      value: 0.872325836533187
    - name: Accuracy
      type: accuracy
      value: 0.9240429965997587
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-wildreceipt

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the wildreceipt dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3154
- Precision: 0.8693
- Recall: 0.8753
- F1: 0.8723
- Accuracy: 0.9240

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 4000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 0.32  | 100  | 1.3618          | 0.6375    | 0.3049 | 0.4125 | 0.6708   |
| No log        | 0.63  | 200  | 0.9129          | 0.6662    | 0.4897 | 0.5645 | 0.7631   |
| No log        | 0.95  | 300  | 0.6800          | 0.7273    | 0.6375 | 0.6795 | 0.8274   |
| No log        | 1.26  | 400  | 0.5733          | 0.7579    | 0.6926 | 0.7238 | 0.8501   |
| 1.0638        | 1.58  | 500  | 0.5015          | 0.7854    | 0.7383 | 0.7611 | 0.8667   |
| 1.0638        | 1.89  | 600  | 0.4501          | 0.7916    | 0.7680 | 0.7796 | 0.8770   |
| 1.0638        | 2.21  | 700  | 0.4145          | 0.8177    | 0.8053 | 0.8114 | 0.8917   |
| 1.0638        | 2.52  | 800  | 0.3835          | 0.8214    | 0.8210 | 0.8212 | 0.8961   |
| 1.0638        | 2.84  | 900  | 0.3666          | 0.8251    | 0.8338 | 0.8294 | 0.9009   |
| 0.423         | 3.15  | 1000 | 0.3524          | 0.8485    | 0.8217 | 0.8349 | 0.9026   |
| 0.423         | 3.47  | 1100 | 0.3451          | 0.8430    | 0.8327 | 0.8378 | 0.9060   |
| 0.423         | 3.79  | 1200 | 0.3348          | 0.8347    | 0.8504 | 0.8425 | 0.9092   |
| 0.423         | 4.1   | 1300 | 0.3331          | 0.8368    | 0.8448 | 0.8408 | 0.9079   |
| 0.423         | 4.42  | 1400 | 0.3163          | 0.8503    | 0.8519 | 0.8511 | 0.9138   |
| 0.2822        | 4.73  | 1500 | 0.3168          | 0.8531    | 0.8504 | 0.8518 | 0.9133   |
| 0.2822        | 5.05  | 1600 | 0.3013          | 0.8629    | 0.8577 | 0.8603 | 0.9183   |
| 0.2822        | 5.36  | 1700 | 0.3146          | 0.8619    | 0.8528 | 0.8573 | 0.9160   |
| 0.2822        | 5.68  | 1800 | 0.3121          | 0.8474    | 0.8638 | 0.8555 | 0.9159   |
| 0.2822        | 5.99  | 1900 | 0.3054          | 0.8537    | 0.8667 | 0.8601 | 0.9166   |
| 0.2176        | 6.31  | 2000 | 0.3127          | 0.8556    | 0.8592 | 0.8574 | 0.9167   |
| 0.2176        | 6.62  | 2100 | 0.3072          | 0.8568    | 0.8667 | 0.8617 | 0.9194   |
| 0.2176        | 6.94  | 2200 | 0.2989          | 0.8617    | 0.8660 | 0.8638 | 0.9209   |
| 0.2176        | 7.26  | 2300 | 0.2997          | 0.8616    | 0.8682 | 0.8649 | 0.9199   |
| 0.2176        | 7.57  | 2400 | 0.3100          | 0.8538    | 0.8689 | 0.8613 | 0.9191   |
| 0.1777        | 7.89  | 2500 | 0.3022          | 0.8649    | 0.8695 | 0.8672 | 0.9228   |
| 0.1777        | 8.2   | 2600 | 0.2990          | 0.8631    | 0.8740 | 0.8685 | 0.9224   |
| 0.1777        | 8.52  | 2700 | 0.3072          | 0.8669    | 0.8697 | 0.8683 | 0.9228   |
| 0.1777        | 8.83  | 2800 | 0.3038          | 0.8689    | 0.8720 | 0.8705 | 0.9238   |
| 0.1777        | 9.15  | 2900 | 0.3138          | 0.8726    | 0.8673 | 0.8700 | 0.9216   |
| 0.1434        | 9.46  | 3000 | 0.3150          | 0.8610    | 0.8740 | 0.8674 | 0.9221   |
| 0.1434        | 9.78  | 3100 | 0.3055          | 0.8674    | 0.8742 | 0.8708 | 0.9239   |
| 0.1434        | 10.09 | 3200 | 0.3182          | 0.8618    | 0.8724 | 0.8671 | 0.9215   |
| 0.1434        | 10.41 | 3300 | 0.3175          | 0.8633    | 0.8727 | 0.8680 | 0.9223   |
| 0.1434        | 10.73 | 3400 | 0.3146          | 0.8685    | 0.8717 | 0.8701 | 0.9234   |
| 0.1282        | 11.04 | 3500 | 0.3136          | 0.8671    | 0.8757 | 0.8714 | 0.9233   |
| 0.1282        | 11.36 | 3600 | 0.3186          | 0.8679    | 0.8734 | 0.8706 | 0.9225   |
| 0.1282        | 11.67 | 3700 | 0.3147          | 0.8701    | 0.8745 | 0.8723 | 0.9238   |
| 0.1282        | 11.99 | 3800 | 0.3159          | 0.8705    | 0.8759 | 0.8732 | 0.9244   |
| 0.1282        | 12.3  | 3900 | 0.3147          | 0.8699    | 0.8748 | 0.8723 | 0.9246   |
| 0.1121        | 12.62 | 4000 | 0.3154          | 0.8693    | 0.8753 | 0.8723 | 0.9240   |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

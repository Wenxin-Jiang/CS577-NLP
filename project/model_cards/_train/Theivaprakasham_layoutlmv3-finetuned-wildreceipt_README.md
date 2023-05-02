---
tags:
- generated_from_trainer
datasets:
- wild_receipt
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
      name: wild_receipt
      type: wild_receipt
      args: WildReceipt
    metrics:
    - name: Precision
      type: precision
      value: 0.877212237618329
    - name: Recall
      type: recall
      value: 0.8798678959680749
    - name: F1
      type: f1
      value: 0.8785380599065679
    - name: Accuracy
      type: accuracy
      value: 0.9249204782274871
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-wildreceipt

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the wild_receipt dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3108
- Precision: 0.8772
- Recall: 0.8799
- F1: 0.8785
- Accuracy: 0.9249

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

The WildReceipt dataset consists of 1740 receipt images, and contains 25 key information categories, and a total of about 69000 text boxes. 1268 and 472 images are used for training and testing respectively to train the LayoutLMv3 model for Key Information Extraction.

## Training procedure

The training code: https://github.com/Theivaprakasham/layoutlmv3/blob/main/training_codes/LayoutLMv3_training_WildReceipts_dataset.ipynb

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
| No log        | 0.32  | 100  | 1.3143          | 0.6709    | 0.2679 | 0.3829 | 0.6700   |
| No log        | 0.63  | 200  | 0.8814          | 0.6478    | 0.5195 | 0.5766 | 0.7786   |
| No log        | 0.95  | 300  | 0.6568          | 0.7205    | 0.6491 | 0.6829 | 0.8303   |
| No log        | 1.26  | 400  | 0.5618          | 0.7544    | 0.7072 | 0.7300 | 0.8519   |
| 1.0284        | 1.58  | 500  | 0.5003          | 0.7802    | 0.7566 | 0.7682 | 0.8687   |
| 1.0284        | 1.89  | 600  | 0.4454          | 0.7941    | 0.7679 | 0.7807 | 0.8748   |
| 1.0284        | 2.21  | 700  | 0.4314          | 0.8142    | 0.7928 | 0.8033 | 0.8852   |
| 1.0284        | 2.52  | 800  | 0.3870          | 0.8172    | 0.8200 | 0.8186 | 0.8953   |
| 1.0284        | 2.84  | 900  | 0.3629          | 0.8288    | 0.8369 | 0.8329 | 0.9025   |
| 0.4167        | 3.15  | 1000 | 0.3537          | 0.8540    | 0.8200 | 0.8366 | 0.9052   |
| 0.4167        | 3.47  | 1100 | 0.3383          | 0.8438    | 0.8285 | 0.8361 | 0.9063   |
| 0.4167        | 3.79  | 1200 | 0.3403          | 0.8297    | 0.8493 | 0.8394 | 0.9062   |
| 0.4167        | 4.1   | 1300 | 0.3271          | 0.8428    | 0.8545 | 0.8487 | 0.9110   |
| 0.4167        | 4.42  | 1400 | 0.3182          | 0.8491    | 0.8518 | 0.8504 | 0.9131   |
| 0.2766        | 4.73  | 1500 | 0.3111          | 0.8491    | 0.8539 | 0.8515 | 0.9129   |
| 0.2766        | 5.05  | 1600 | 0.3177          | 0.8397    | 0.8620 | 0.8507 | 0.9124   |
| 0.2766        | 5.36  | 1700 | 0.3091          | 0.8676    | 0.8548 | 0.8612 | 0.9191   |
| 0.2766        | 5.68  | 1800 | 0.3080          | 0.8508    | 0.8645 | 0.8576 | 0.9162   |
| 0.2766        | 5.99  | 1900 | 0.3059          | 0.8492    | 0.8662 | 0.8576 | 0.9163   |
| 0.2114        | 6.31  | 2000 | 0.3184          | 0.8536    | 0.8657 | 0.8596 | 0.9147   |
| 0.2114        | 6.62  | 2100 | 0.3161          | 0.8583    | 0.8713 | 0.8648 | 0.9184   |
| 0.2114        | 6.94  | 2200 | 0.3055          | 0.8707    | 0.8682 | 0.8694 | 0.9220   |
| 0.2114        | 7.26  | 2300 | 0.3004          | 0.8689    | 0.8745 | 0.8717 | 0.9219   |
| 0.2114        | 7.57  | 2400 | 0.3111          | 0.8701    | 0.8720 | 0.8711 | 0.9211   |
| 0.174         | 7.89  | 2500 | 0.3130          | 0.8599    | 0.8741 | 0.8669 | 0.9198   |
| 0.174         | 8.2   | 2600 | 0.3034          | 0.8661    | 0.8748 | 0.8704 | 0.9219   |
| 0.174         | 8.52  | 2700 | 0.3005          | 0.8799    | 0.8673 | 0.8736 | 0.9225   |
| 0.174         | 8.83  | 2800 | 0.3043          | 0.8687    | 0.8804 | 0.8745 | 0.9240   |
| 0.174         | 9.15  | 2900 | 0.3121          | 0.8776    | 0.8704 | 0.8740 | 0.9242   |
| 0.1412        | 9.46  | 3000 | 0.3131          | 0.8631    | 0.8755 | 0.8692 | 0.9204   |
| 0.1412        | 9.78  | 3100 | 0.3067          | 0.8715    | 0.8773 | 0.8744 | 0.9233   |
| 0.1412        | 10.09 | 3200 | 0.3021          | 0.8751    | 0.8812 | 0.8782 | 0.9248   |
| 0.1412        | 10.41 | 3300 | 0.3092          | 0.8651    | 0.8808 | 0.8729 | 0.9228   |
| 0.1412        | 10.73 | 3400 | 0.3084          | 0.8776    | 0.8749 | 0.8762 | 0.9237   |
| 0.1254        | 11.04 | 3500 | 0.3156          | 0.8738    | 0.8785 | 0.8761 | 0.9237   |
| 0.1254        | 11.36 | 3600 | 0.3131          | 0.8723    | 0.8818 | 0.8770 | 0.9244   |
| 0.1254        | 11.67 | 3700 | 0.3108          | 0.8778    | 0.8781 | 0.8780 | 0.9250   |
| 0.1254        | 11.99 | 3800 | 0.3097          | 0.8778    | 0.8771 | 0.8775 | 0.9239   |
| 0.1254        | 12.3  | 3900 | 0.3115          | 0.8785    | 0.8801 | 0.8793 | 0.9251   |
| 0.111         | 12.62 | 4000 | 0.3108          | 0.8772    | 0.8799 | 0.8785 | 0.9249   |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

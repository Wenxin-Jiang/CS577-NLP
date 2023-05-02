---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__subj__train-8-8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__subj__train-8-8

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3160
- Accuracy: 0.8735

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7187        | 1.0   | 3    | 0.6776          | 1.0      |
| 0.684         | 2.0   | 6    | 0.6608          | 1.0      |
| 0.6532        | 3.0   | 9    | 0.6364          | 1.0      |
| 0.5996        | 4.0   | 12   | 0.6119          | 1.0      |
| 0.5242        | 5.0   | 15   | 0.5806          | 1.0      |
| 0.4612        | 6.0   | 18   | 0.5320          | 1.0      |
| 0.4192        | 7.0   | 21   | 0.4714          | 1.0      |
| 0.3274        | 8.0   | 24   | 0.4071          | 1.0      |
| 0.2871        | 9.0   | 27   | 0.3378          | 1.0      |
| 0.2082        | 10.0  | 30   | 0.2822          | 1.0      |
| 0.1692        | 11.0  | 33   | 0.2271          | 1.0      |
| 0.1242        | 12.0  | 36   | 0.1793          | 1.0      |
| 0.0977        | 13.0  | 39   | 0.1417          | 1.0      |
| 0.0776        | 14.0  | 42   | 0.1117          | 1.0      |
| 0.0631        | 15.0  | 45   | 0.0894          | 1.0      |
| 0.0453        | 16.0  | 48   | 0.0733          | 1.0      |
| 0.0399        | 17.0  | 51   | 0.0617          | 1.0      |
| 0.0333        | 18.0  | 54   | 0.0528          | 1.0      |
| 0.0266        | 19.0  | 57   | 0.0454          | 1.0      |
| 0.0234        | 20.0  | 60   | 0.0393          | 1.0      |
| 0.0223        | 21.0  | 63   | 0.0345          | 1.0      |
| 0.0195        | 22.0  | 66   | 0.0309          | 1.0      |
| 0.0161        | 23.0  | 69   | 0.0281          | 1.0      |
| 0.0167        | 24.0  | 72   | 0.0260          | 1.0      |
| 0.0163        | 25.0  | 75   | 0.0242          | 1.0      |
| 0.0134        | 26.0  | 78   | 0.0227          | 1.0      |
| 0.0128        | 27.0  | 81   | 0.0214          | 1.0      |
| 0.0101        | 28.0  | 84   | 0.0204          | 1.0      |
| 0.0109        | 29.0  | 87   | 0.0194          | 1.0      |
| 0.0112        | 30.0  | 90   | 0.0186          | 1.0      |
| 0.0108        | 31.0  | 93   | 0.0179          | 1.0      |
| 0.011         | 32.0  | 96   | 0.0174          | 1.0      |
| 0.0099        | 33.0  | 99   | 0.0169          | 1.0      |
| 0.0083        | 34.0  | 102  | 0.0164          | 1.0      |
| 0.0096        | 35.0  | 105  | 0.0160          | 1.0      |
| 0.01          | 36.0  | 108  | 0.0156          | 1.0      |
| 0.0084        | 37.0  | 111  | 0.0152          | 1.0      |
| 0.0089        | 38.0  | 114  | 0.0149          | 1.0      |
| 0.0073        | 39.0  | 117  | 0.0146          | 1.0      |
| 0.0082        | 40.0  | 120  | 0.0143          | 1.0      |
| 0.008         | 41.0  | 123  | 0.0141          | 1.0      |
| 0.0093        | 42.0  | 126  | 0.0139          | 1.0      |
| 0.0078        | 43.0  | 129  | 0.0138          | 1.0      |
| 0.0086        | 44.0  | 132  | 0.0136          | 1.0      |
| 0.009         | 45.0  | 135  | 0.0135          | 1.0      |
| 0.0072        | 46.0  | 138  | 0.0134          | 1.0      |
| 0.0075        | 47.0  | 141  | 0.0133          | 1.0      |
| 0.0082        | 48.0  | 144  | 0.0133          | 1.0      |
| 0.0068        | 49.0  | 147  | 0.0132          | 1.0      |
| 0.0074        | 50.0  | 150  | 0.0132          | 1.0      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__subj__train-8-7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__subj__train-8-7

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2766
- Accuracy: 0.8845

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
| 0.7044        | 1.0   | 3    | 0.6909          | 0.5      |
| 0.6678        | 2.0   | 6    | 0.6901          | 0.5      |
| 0.6336        | 3.0   | 9    | 0.6807          | 0.5      |
| 0.5926        | 4.0   | 12   | 0.6726          | 0.5      |
| 0.5221        | 5.0   | 15   | 0.6648          | 0.5      |
| 0.4573        | 6.0   | 18   | 0.6470          | 0.5      |
| 0.4177        | 7.0   | 21   | 0.6251          | 0.5      |
| 0.3252        | 8.0   | 24   | 0.5994          | 0.5      |
| 0.2831        | 9.0   | 27   | 0.5529          | 0.5      |
| 0.213         | 10.0  | 30   | 0.5078          | 0.75     |
| 0.1808        | 11.0  | 33   | 0.4521          | 1.0      |
| 0.1355        | 12.0  | 36   | 0.3996          | 1.0      |
| 0.1027        | 13.0  | 39   | 0.3557          | 1.0      |
| 0.0862        | 14.0  | 42   | 0.3121          | 1.0      |
| 0.0682        | 15.0  | 45   | 0.2828          | 1.0      |
| 0.0517        | 16.0  | 48   | 0.2603          | 1.0      |
| 0.0466        | 17.0  | 51   | 0.2412          | 1.0      |
| 0.038         | 18.0  | 54   | 0.2241          | 1.0      |
| 0.0276        | 19.0  | 57   | 0.2096          | 1.0      |
| 0.0246        | 20.0  | 60   | 0.1969          | 1.0      |
| 0.0249        | 21.0  | 63   | 0.1859          | 1.0      |
| 0.0201        | 22.0  | 66   | 0.1770          | 1.0      |
| 0.018         | 23.0  | 69   | 0.1703          | 1.0      |
| 0.0164        | 24.0  | 72   | 0.1670          | 1.0      |
| 0.0172        | 25.0  | 75   | 0.1639          | 1.0      |
| 0.0135        | 26.0  | 78   | 0.1604          | 1.0      |
| 0.014         | 27.0  | 81   | 0.1585          | 1.0      |
| 0.0108        | 28.0  | 84   | 0.1569          | 1.0      |
| 0.0116        | 29.0  | 87   | 0.1549          | 1.0      |
| 0.0111        | 30.0  | 90   | 0.1532          | 1.0      |
| 0.0113        | 31.0  | 93   | 0.1513          | 1.0      |
| 0.0104        | 32.0  | 96   | 0.1503          | 1.0      |
| 0.01          | 33.0  | 99   | 0.1490          | 1.0      |
| 0.0079        | 34.0  | 102  | 0.1479          | 1.0      |
| 0.0097        | 35.0  | 105  | 0.1466          | 1.0      |
| 0.0112        | 36.0  | 108  | 0.1458          | 1.0      |
| 0.0091        | 37.0  | 111  | 0.1457          | 1.0      |
| 0.0098        | 38.0  | 114  | 0.1454          | 1.0      |
| 0.0076        | 39.0  | 117  | 0.1451          | 1.0      |
| 0.0085        | 40.0  | 120  | 0.1448          | 1.0      |
| 0.0079        | 41.0  | 123  | 0.1445          | 1.0      |
| 0.0096        | 42.0  | 126  | 0.1440          | 1.0      |
| 0.0081        | 43.0  | 129  | 0.1430          | 1.0      |
| 0.0083        | 44.0  | 132  | 0.1424          | 1.0      |
| 0.0088        | 45.0  | 135  | 0.1418          | 1.0      |
| 0.0077        | 46.0  | 138  | 0.1414          | 1.0      |
| 0.0073        | 47.0  | 141  | 0.1413          | 1.0      |
| 0.0084        | 48.0  | 144  | 0.1412          | 1.0      |
| 0.0072        | 49.0  | 147  | 0.1411          | 1.0      |
| 0.0077        | 50.0  | 150  | 0.1411          | 1.0      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

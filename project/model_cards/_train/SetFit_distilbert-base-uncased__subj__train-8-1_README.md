---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__subj__train-8-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__subj__train-8-1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5488
- Accuracy: 0.791

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
| 0.703         | 1.0   | 3    | 0.6906          | 0.5      |
| 0.666         | 2.0   | 6    | 0.6945          | 0.25     |
| 0.63          | 3.0   | 9    | 0.6885          | 0.5      |
| 0.588         | 4.0   | 12   | 0.6888          | 0.25     |
| 0.5181        | 5.0   | 15   | 0.6899          | 0.25     |
| 0.4508        | 6.0   | 18   | 0.6770          | 0.5      |
| 0.4025        | 7.0   | 21   | 0.6579          | 0.5      |
| 0.3361        | 8.0   | 24   | 0.6392          | 0.5      |
| 0.2919        | 9.0   | 27   | 0.6113          | 0.5      |
| 0.2151        | 10.0  | 30   | 0.5774          | 0.75     |
| 0.1728        | 11.0  | 33   | 0.5248          | 0.75     |
| 0.1313        | 12.0  | 36   | 0.4824          | 0.75     |
| 0.1046        | 13.0  | 39   | 0.4456          | 0.75     |
| 0.0858        | 14.0  | 42   | 0.4076          | 0.75     |
| 0.0679        | 15.0  | 45   | 0.3755          | 0.75     |
| 0.0485        | 16.0  | 48   | 0.3422          | 0.75     |
| 0.0416        | 17.0  | 51   | 0.3055          | 0.75     |
| 0.0358        | 18.0  | 54   | 0.2731          | 1.0      |
| 0.0277        | 19.0  | 57   | 0.2443          | 1.0      |
| 0.0234        | 20.0  | 60   | 0.2187          | 1.0      |
| 0.0223        | 21.0  | 63   | 0.1960          | 1.0      |
| 0.0187        | 22.0  | 66   | 0.1762          | 1.0      |
| 0.017         | 23.0  | 69   | 0.1629          | 1.0      |
| 0.0154        | 24.0  | 72   | 0.1543          | 1.0      |
| 0.0164        | 25.0  | 75   | 0.1476          | 1.0      |
| 0.0131        | 26.0  | 78   | 0.1423          | 1.0      |
| 0.0139        | 27.0  | 81   | 0.1387          | 1.0      |
| 0.0107        | 28.0  | 84   | 0.1360          | 1.0      |
| 0.0108        | 29.0  | 87   | 0.1331          | 1.0      |
| 0.0105        | 30.0  | 90   | 0.1308          | 1.0      |
| 0.0106        | 31.0  | 93   | 0.1276          | 1.0      |
| 0.0104        | 32.0  | 96   | 0.1267          | 1.0      |
| 0.0095        | 33.0  | 99   | 0.1255          | 1.0      |
| 0.0076        | 34.0  | 102  | 0.1243          | 1.0      |
| 0.0094        | 35.0  | 105  | 0.1235          | 1.0      |
| 0.0103        | 36.0  | 108  | 0.1228          | 1.0      |
| 0.0086        | 37.0  | 111  | 0.1231          | 1.0      |
| 0.0094        | 38.0  | 114  | 0.1236          | 1.0      |
| 0.0074        | 39.0  | 117  | 0.1240          | 1.0      |
| 0.0085        | 40.0  | 120  | 0.1246          | 1.0      |
| 0.0079        | 41.0  | 123  | 0.1253          | 1.0      |
| 0.0088        | 42.0  | 126  | 0.1248          | 1.0      |
| 0.0082        | 43.0  | 129  | 0.1244          | 1.0      |
| 0.0082        | 44.0  | 132  | 0.1234          | 1.0      |
| 0.0082        | 45.0  | 135  | 0.1223          | 1.0      |
| 0.0071        | 46.0  | 138  | 0.1212          | 1.0      |
| 0.0073        | 47.0  | 141  | 0.1208          | 1.0      |
| 0.0081        | 48.0  | 144  | 0.1205          | 1.0      |
| 0.0067        | 49.0  | 147  | 0.1202          | 1.0      |
| 0.0077        | 50.0  | 150  | 0.1202          | 1.0      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

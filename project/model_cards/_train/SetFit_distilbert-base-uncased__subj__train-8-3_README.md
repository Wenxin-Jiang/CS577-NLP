---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__subj__train-8-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__subj__train-8-3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3496
- Accuracy: 0.859

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
| 0.7136        | 1.0   | 3    | 0.6875          | 0.75     |
| 0.6702        | 2.0   | 6    | 0.6824          | 0.75     |
| 0.6456        | 3.0   | 9    | 0.6687          | 0.75     |
| 0.5934        | 4.0   | 12   | 0.6564          | 0.75     |
| 0.537         | 5.0   | 15   | 0.6428          | 0.75     |
| 0.4812        | 6.0   | 18   | 0.6180          | 0.75     |
| 0.4279        | 7.0   | 21   | 0.5864          | 0.75     |
| 0.3608        | 8.0   | 24   | 0.5540          | 0.75     |
| 0.3076        | 9.0   | 27   | 0.5012          | 1.0      |
| 0.2292        | 10.0  | 30   | 0.4497          | 1.0      |
| 0.1991        | 11.0  | 33   | 0.3945          | 1.0      |
| 0.1495        | 12.0  | 36   | 0.3483          | 1.0      |
| 0.1176        | 13.0  | 39   | 0.3061          | 1.0      |
| 0.0947        | 14.0  | 42   | 0.2683          | 1.0      |
| 0.0761        | 15.0  | 45   | 0.2295          | 1.0      |
| 0.0584        | 16.0  | 48   | 0.1996          | 1.0      |
| 0.0451        | 17.0  | 51   | 0.1739          | 1.0      |
| 0.0387        | 18.0  | 54   | 0.1521          | 1.0      |
| 0.0272        | 19.0  | 57   | 0.1333          | 1.0      |
| 0.0247        | 20.0  | 60   | 0.1171          | 1.0      |
| 0.0243        | 21.0  | 63   | 0.1044          | 1.0      |
| 0.0206        | 22.0  | 66   | 0.0943          | 1.0      |
| 0.0175        | 23.0  | 69   | 0.0859          | 1.0      |
| 0.0169        | 24.0  | 72   | 0.0799          | 1.0      |
| 0.0162        | 25.0  | 75   | 0.0746          | 1.0      |
| 0.0137        | 26.0  | 78   | 0.0705          | 1.0      |
| 0.0141        | 27.0  | 81   | 0.0674          | 1.0      |
| 0.0107        | 28.0  | 84   | 0.0654          | 1.0      |
| 0.0117        | 29.0  | 87   | 0.0634          | 1.0      |
| 0.0113        | 30.0  | 90   | 0.0617          | 1.0      |
| 0.0107        | 31.0  | 93   | 0.0599          | 1.0      |
| 0.0106        | 32.0  | 96   | 0.0585          | 1.0      |
| 0.0101        | 33.0  | 99   | 0.0568          | 1.0      |
| 0.0084        | 34.0  | 102  | 0.0553          | 1.0      |
| 0.0101        | 35.0  | 105  | 0.0539          | 1.0      |
| 0.0102        | 36.0  | 108  | 0.0529          | 1.0      |
| 0.009         | 37.0  | 111  | 0.0520          | 1.0      |
| 0.0092        | 38.0  | 114  | 0.0511          | 1.0      |
| 0.0073        | 39.0  | 117  | 0.0504          | 1.0      |
| 0.0081        | 40.0  | 120  | 0.0497          | 1.0      |
| 0.0079        | 41.0  | 123  | 0.0492          | 1.0      |
| 0.0092        | 42.0  | 126  | 0.0488          | 1.0      |
| 0.008         | 43.0  | 129  | 0.0483          | 1.0      |
| 0.0087        | 44.0  | 132  | 0.0479          | 1.0      |
| 0.009         | 45.0  | 135  | 0.0474          | 1.0      |
| 0.0076        | 46.0  | 138  | 0.0470          | 1.0      |
| 0.0075        | 47.0  | 141  | 0.0467          | 1.0      |
| 0.008         | 48.0  | 144  | 0.0465          | 1.0      |
| 0.0069        | 49.0  | 147  | 0.0464          | 1.0      |
| 0.0077        | 50.0  | 150  | 0.0464          | 1.0      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

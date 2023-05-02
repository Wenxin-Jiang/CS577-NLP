---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__subj__train-8-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__subj__train-8-6

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6075
- Accuracy: 0.7485

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
| 0.7163        | 1.0   | 3    | 0.6923          | 0.5      |
| 0.6648        | 2.0   | 6    | 0.6838          | 0.5      |
| 0.6329        | 3.0   | 9    | 0.6747          | 0.75     |
| 0.5836        | 4.0   | 12   | 0.6693          | 0.5      |
| 0.5287        | 5.0   | 15   | 0.6670          | 0.25     |
| 0.4585        | 6.0   | 18   | 0.6517          | 0.5      |
| 0.415         | 7.0   | 21   | 0.6290          | 0.5      |
| 0.3353        | 8.0   | 24   | 0.6019          | 0.5      |
| 0.2841        | 9.0   | 27   | 0.5613          | 0.75     |
| 0.2203        | 10.0  | 30   | 0.5222          | 1.0      |
| 0.1743        | 11.0  | 33   | 0.4769          | 1.0      |
| 0.1444        | 12.0  | 36   | 0.4597          | 1.0      |
| 0.1079        | 13.0  | 39   | 0.4462          | 1.0      |
| 0.0891        | 14.0  | 42   | 0.4216          | 1.0      |
| 0.0704        | 15.0  | 45   | 0.3880          | 1.0      |
| 0.0505        | 16.0  | 48   | 0.3663          | 1.0      |
| 0.0428        | 17.0  | 51   | 0.3536          | 1.0      |
| 0.0356        | 18.0  | 54   | 0.3490          | 1.0      |
| 0.0283        | 19.0  | 57   | 0.3531          | 1.0      |
| 0.025         | 20.0  | 60   | 0.3595          | 1.0      |
| 0.0239        | 21.0  | 63   | 0.3594          | 1.0      |
| 0.0202        | 22.0  | 66   | 0.3521          | 1.0      |
| 0.0168        | 23.0  | 69   | 0.3475          | 1.0      |
| 0.0159        | 24.0  | 72   | 0.3458          | 1.0      |
| 0.0164        | 25.0  | 75   | 0.3409          | 1.0      |
| 0.0132        | 26.0  | 78   | 0.3360          | 1.0      |
| 0.0137        | 27.0  | 81   | 0.3302          | 1.0      |
| 0.0112        | 28.0  | 84   | 0.3235          | 1.0      |
| 0.0113        | 29.0  | 87   | 0.3178          | 1.0      |
| 0.0111        | 30.0  | 90   | 0.3159          | 1.0      |
| 0.0113        | 31.0  | 93   | 0.3108          | 1.0      |
| 0.0107        | 32.0  | 96   | 0.3101          | 1.0      |
| 0.0101        | 33.0  | 99   | 0.3100          | 1.0      |
| 0.0083        | 34.0  | 102  | 0.3110          | 1.0      |
| 0.0092        | 35.0  | 105  | 0.3117          | 1.0      |
| 0.0102        | 36.0  | 108  | 0.3104          | 1.0      |
| 0.0086        | 37.0  | 111  | 0.3086          | 1.0      |
| 0.0092        | 38.0  | 114  | 0.3047          | 1.0      |
| 0.0072        | 39.0  | 117  | 0.3024          | 1.0      |
| 0.0079        | 40.0  | 120  | 0.3014          | 1.0      |
| 0.0079        | 41.0  | 123  | 0.2983          | 1.0      |
| 0.0091        | 42.0  | 126  | 0.2948          | 1.0      |
| 0.0077        | 43.0  | 129  | 0.2915          | 1.0      |
| 0.0085        | 44.0  | 132  | 0.2890          | 1.0      |
| 0.009         | 45.0  | 135  | 0.2870          | 1.0      |
| 0.0073        | 46.0  | 138  | 0.2856          | 1.0      |
| 0.0073        | 47.0  | 141  | 0.2844          | 1.0      |
| 0.0076        | 48.0  | 144  | 0.2841          | 1.0      |
| 0.0065        | 49.0  | 147  | 0.2836          | 1.0      |
| 0.0081        | 50.0  | 150  | 0.2835          | 1.0      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

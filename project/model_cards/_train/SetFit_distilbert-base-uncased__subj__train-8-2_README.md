---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__subj__train-8-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__subj__train-8-2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3081
- Accuracy: 0.8755

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
| 0.7146        | 1.0   | 3    | 0.6798          | 0.75     |
| 0.6737        | 2.0   | 6    | 0.6847          | 0.75     |
| 0.6519        | 3.0   | 9    | 0.6783          | 0.75     |
| 0.6105        | 4.0   | 12   | 0.6812          | 0.25     |
| 0.5463        | 5.0   | 15   | 0.6869          | 0.25     |
| 0.4922        | 6.0   | 18   | 0.6837          | 0.5      |
| 0.4543        | 7.0   | 21   | 0.6716          | 0.5      |
| 0.3856        | 8.0   | 24   | 0.6613          | 0.75     |
| 0.3475        | 9.0   | 27   | 0.6282          | 0.75     |
| 0.2717        | 10.0  | 30   | 0.6045          | 0.75     |
| 0.2347        | 11.0  | 33   | 0.5620          | 0.75     |
| 0.1979        | 12.0  | 36   | 0.5234          | 1.0      |
| 0.1535        | 13.0  | 39   | 0.4771          | 1.0      |
| 0.1332        | 14.0  | 42   | 0.4277          | 1.0      |
| 0.1041        | 15.0  | 45   | 0.3785          | 1.0      |
| 0.082         | 16.0  | 48   | 0.3318          | 1.0      |
| 0.0672        | 17.0  | 51   | 0.2885          | 1.0      |
| 0.0538        | 18.0  | 54   | 0.2568          | 1.0      |
| 0.0412        | 19.0  | 57   | 0.2356          | 1.0      |
| 0.0361        | 20.0  | 60   | 0.2217          | 1.0      |
| 0.0303        | 21.0  | 63   | 0.2125          | 1.0      |
| 0.0268        | 22.0  | 66   | 0.2060          | 1.0      |
| 0.0229        | 23.0  | 69   | 0.2015          | 1.0      |
| 0.0215        | 24.0  | 72   | 0.1989          | 1.0      |
| 0.0211        | 25.0  | 75   | 0.1969          | 1.0      |
| 0.0172        | 26.0  | 78   | 0.1953          | 1.0      |
| 0.0165        | 27.0  | 81   | 0.1935          | 1.0      |
| 0.0132        | 28.0  | 84   | 0.1923          | 1.0      |
| 0.0146        | 29.0  | 87   | 0.1914          | 1.0      |
| 0.0125        | 30.0  | 90   | 0.1904          | 1.0      |
| 0.0119        | 31.0  | 93   | 0.1897          | 1.0      |
| 0.0122        | 32.0  | 96   | 0.1886          | 1.0      |
| 0.0118        | 33.0  | 99   | 0.1875          | 1.0      |
| 0.0097        | 34.0  | 102  | 0.1866          | 1.0      |
| 0.0111        | 35.0  | 105  | 0.1861          | 1.0      |
| 0.0111        | 36.0  | 108  | 0.1855          | 1.0      |
| 0.0102        | 37.0  | 111  | 0.1851          | 1.0      |
| 0.0109        | 38.0  | 114  | 0.1851          | 1.0      |
| 0.0085        | 39.0  | 117  | 0.1854          | 1.0      |
| 0.0089        | 40.0  | 120  | 0.1855          | 1.0      |
| 0.0092        | 41.0  | 123  | 0.1863          | 1.0      |
| 0.0105        | 42.0  | 126  | 0.1868          | 1.0      |
| 0.0089        | 43.0  | 129  | 0.1874          | 1.0      |
| 0.0091        | 44.0  | 132  | 0.1877          | 1.0      |
| 0.0096        | 45.0  | 135  | 0.1881          | 1.0      |
| 0.0081        | 46.0  | 138  | 0.1881          | 1.0      |
| 0.0086        | 47.0  | 141  | 0.1883          | 1.0      |
| 0.009         | 48.0  | 144  | 0.1884          | 1.0      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

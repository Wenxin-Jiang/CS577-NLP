---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-8-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-8-6

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5336
- Accuracy: 0.7523

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
| 0.7161        | 1.0   | 3    | 0.6941          | 0.5      |
| 0.6786        | 2.0   | 6    | 0.7039          | 0.25     |
| 0.6586        | 3.0   | 9    | 0.7090          | 0.25     |
| 0.6121        | 4.0   | 12   | 0.7183          | 0.25     |
| 0.5696        | 5.0   | 15   | 0.7266          | 0.25     |
| 0.522         | 6.0   | 18   | 0.7305          | 0.25     |
| 0.4899        | 7.0   | 21   | 0.7339          | 0.25     |
| 0.3985        | 8.0   | 24   | 0.7429          | 0.25     |
| 0.3758        | 9.0   | 27   | 0.7224          | 0.25     |
| 0.2876        | 10.0  | 30   | 0.7068          | 0.5      |
| 0.2498        | 11.0  | 33   | 0.6751          | 0.75     |
| 0.1921        | 12.0  | 36   | 0.6487          | 0.75     |
| 0.1491        | 13.0  | 39   | 0.6261          | 0.75     |
| 0.1276        | 14.0  | 42   | 0.6102          | 0.75     |
| 0.0996        | 15.0  | 45   | 0.5964          | 0.75     |
| 0.073         | 16.0  | 48   | 0.6019          | 0.75     |
| 0.0627        | 17.0  | 51   | 0.5933          | 0.75     |
| 0.053         | 18.0  | 54   | 0.5768          | 0.75     |
| 0.0403        | 19.0  | 57   | 0.5698          | 0.75     |
| 0.0328        | 20.0  | 60   | 0.5656          | 0.75     |
| 0.03          | 21.0  | 63   | 0.5634          | 0.75     |
| 0.025         | 22.0  | 66   | 0.5620          | 0.75     |
| 0.0209        | 23.0  | 69   | 0.5623          | 0.75     |
| 0.0214        | 24.0  | 72   | 0.5606          | 0.75     |
| 0.0191        | 25.0  | 75   | 0.5565          | 0.75     |
| 0.0173        | 26.0  | 78   | 0.5485          | 0.75     |
| 0.0175        | 27.0  | 81   | 0.5397          | 0.75     |
| 0.0132        | 28.0  | 84   | 0.5322          | 0.75     |
| 0.0138        | 29.0  | 87   | 0.5241          | 0.75     |
| 0.0128        | 30.0  | 90   | 0.5235          | 0.75     |
| 0.0126        | 31.0  | 93   | 0.5253          | 0.75     |
| 0.012         | 32.0  | 96   | 0.5317          | 0.75     |
| 0.0118        | 33.0  | 99   | 0.5342          | 0.75     |
| 0.0092        | 34.0  | 102  | 0.5388          | 0.75     |
| 0.0117        | 35.0  | 105  | 0.5414          | 0.75     |
| 0.0124        | 36.0  | 108  | 0.5453          | 0.75     |
| 0.0109        | 37.0  | 111  | 0.5506          | 0.75     |
| 0.0112        | 38.0  | 114  | 0.5555          | 0.75     |
| 0.0087        | 39.0  | 117  | 0.5597          | 0.75     |
| 0.01          | 40.0  | 120  | 0.5640          | 0.75     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

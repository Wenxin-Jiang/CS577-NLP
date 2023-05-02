---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-16-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-16-4

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1501
- Accuracy: 0.6387

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
| 0.7043        | 1.0   | 7    | 0.7139          | 0.2857   |
| 0.68          | 2.0   | 14   | 0.7398          | 0.2857   |
| 0.641         | 3.0   | 21   | 0.7723          | 0.2857   |
| 0.5424        | 4.0   | 28   | 0.8391          | 0.2857   |
| 0.5988        | 5.0   | 35   | 0.7761          | 0.2857   |
| 0.3698        | 6.0   | 42   | 0.7707          | 0.4286   |
| 0.3204        | 7.0   | 49   | 0.8290          | 0.4286   |
| 0.2882        | 8.0   | 56   | 0.6551          | 0.5714   |
| 0.1512        | 9.0   | 63   | 0.5652          | 0.5714   |
| 0.1302        | 10.0  | 70   | 0.5278          | 0.5714   |
| 0.1043        | 11.0  | 77   | 0.4987          | 0.7143   |
| 0.0272        | 12.0  | 84   | 0.5278          | 0.5714   |
| 0.0201        | 13.0  | 91   | 0.5307          | 0.5714   |
| 0.0129        | 14.0  | 98   | 0.5382          | 0.5714   |
| 0.0117        | 15.0  | 105  | 0.5227          | 0.5714   |
| 0.0094        | 16.0  | 112  | 0.5066          | 0.7143   |
| 0.0104        | 17.0  | 119  | 0.4869          | 0.7143   |
| 0.0069        | 18.0  | 126  | 0.4786          | 0.7143   |
| 0.0062        | 19.0  | 133  | 0.4707          | 0.7143   |
| 0.0065        | 20.0  | 140  | 0.4669          | 0.7143   |
| 0.0051        | 21.0  | 147  | 0.4686          | 0.7143   |
| 0.0049        | 22.0  | 154  | 0.4784          | 0.7143   |
| 0.0046        | 23.0  | 161  | 0.4839          | 0.7143   |
| 0.0039        | 24.0  | 168  | 0.4823          | 0.7143   |
| 0.0044        | 25.0  | 175  | 0.4791          | 0.7143   |
| 0.0037        | 26.0  | 182  | 0.4778          | 0.7143   |
| 0.0038        | 27.0  | 189  | 0.4770          | 0.7143   |
| 0.0036        | 28.0  | 196  | 0.4750          | 0.7143   |
| 0.0031        | 29.0  | 203  | 0.4766          | 0.7143   |
| 0.0031        | 30.0  | 210  | 0.4754          | 0.7143   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3

---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: poem-gen-t5-small_v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# poem-gen-t5-small_v1

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7290

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 3.5397        | 0.32  | 5000   | 3.3474          |
| 3.4107        | 0.63  | 10000  | 3.2260          |
| 3.3236        | 0.95  | 15000  | 3.1414          |
| 3.25          | 1.26  | 20000  | 3.0884          |
| 3.2055        | 1.58  | 25000  | 3.0461          |
| 3.1677        | 1.89  | 30000  | 3.0057          |
| 3.1189        | 2.21  | 35000  | 2.9786          |
| 3.0972        | 2.53  | 40000  | 2.9533          |
| 3.0855        | 2.84  | 45000  | 2.9318          |
| 3.0364        | 3.16  | 50000  | 2.9124          |
| 3.0125        | 3.47  | 55000  | 2.8962          |
| 2.9987        | 3.79  | 60000  | 2.8812          |
| 2.9734        | 4.1   | 65000  | 2.8675          |
| 2.9782        | 4.42  | 70000  | 2.8563          |
| 2.9492        | 4.74  | 75000  | 2.8446          |
| 2.9383        | 5.05  | 80000  | 2.8360          |
| 2.9322        | 5.37  | 85000  | 2.8250          |
| 2.9193        | 5.68  | 90000  | 2.8159          |
| 2.9119        | 6.0   | 95000  | 2.8095          |
| 2.8893        | 6.31  | 100000 | 2.8046          |
| 2.8927        | 6.63  | 105000 | 2.7975          |
| 2.8944        | 6.95  | 110000 | 2.7879          |
| 2.8568        | 7.26  | 115000 | 2.7856          |
| 2.8648        | 7.58  | 120000 | 2.7808          |
| 2.8534        | 7.89  | 125000 | 2.7737          |
| 2.8563        | 8.21  | 130000 | 2.7696          |
| 2.8387        | 8.52  | 135000 | 2.7664          |
| 2.8328        | 8.84  | 140000 | 2.7643          |
| 2.8137        | 9.16  | 145000 | 2.7615          |
| 2.8058        | 9.47  | 150000 | 2.7548          |
| 2.8138        | 9.79  | 155000 | 2.7547          |
| 2.8098        | 10.1  | 160000 | 2.7506          |
| 2.7944        | 10.42 | 165000 | 2.7479          |
| 2.809         | 10.73 | 170000 | 2.7443          |
| 2.7897        | 11.05 | 175000 | 2.7431          |
| 2.7955        | 11.37 | 180000 | 2.7403          |
| 2.793         | 11.68 | 185000 | 2.7403          |
| 2.798         | 12.0  | 190000 | 2.7351          |
| 2.7955        | 12.31 | 195000 | 2.7351          |
| 2.785         | 12.63 | 200000 | 2.7329          |
| 2.7701        | 12.94 | 205000 | 2.7329          |
| 2.7744        | 13.26 | 210000 | 2.7317          |
| 2.7827        | 13.58 | 215000 | 2.7295          |
| 2.7793        | 13.89 | 220000 | 2.7303          |
| 2.7782        | 14.21 | 225000 | 2.7298          |
| 2.7762        | 14.52 | 230000 | 2.7289          |
| 2.7719        | 14.84 | 235000 | 2.7292          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

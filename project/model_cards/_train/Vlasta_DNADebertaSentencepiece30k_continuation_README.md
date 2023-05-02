---
tags:
- generated_from_trainer
model-index:
- name: DNADebertaSentencepiece30k_continuation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DNADebertaSentencepiece30k_continuation

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 6.0813

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 6.4099        | 0.41  | 5000   | 6.3686          |
| 6.4014        | 0.81  | 10000  | 6.3544          |
| 6.3816        | 1.22  | 15000  | 6.3338          |
| 6.3652        | 1.62  | 20000  | 6.3161          |
| 6.3477        | 2.03  | 25000  | 6.2981          |
| 6.3305        | 2.44  | 30000  | 6.2851          |
| 6.3173        | 2.84  | 35000  | 6.2725          |
| 6.306         | 3.25  | 40000  | 6.2559          |
| 6.2903        | 3.66  | 45000  | 6.2447          |
| 6.2806        | 4.06  | 50000  | 6.2342          |
| 6.2654        | 4.47  | 55000  | 6.2213          |
| 6.2592        | 4.87  | 60000  | 6.2101          |
| 6.2481        | 5.28  | 65000  | 6.2023          |
| 6.2394        | 5.69  | 70000  | 6.1929          |
| 6.2295        | 6.09  | 75000  | 6.1833          |
| 6.219         | 6.5   | 80000  | 6.1800          |
| 6.2143        | 6.91  | 85000  | 6.1698          |
| 6.2031        | 7.31  | 90000  | 6.1629          |
| 6.2036        | 7.72  | 95000  | 6.1523          |
| 6.1923        | 8.12  | 100000 | 6.1522          |
| 6.1868        | 8.53  | 105000 | 6.1426          |
| 6.1827        | 8.94  | 110000 | 6.1356          |
| 6.1767        | 9.34  | 115000 | 6.1322          |
| 6.1717        | 9.75  | 120000 | 6.1255          |
| 6.1649        | 10.16 | 125000 | 6.1221          |
| 6.1591        | 10.56 | 130000 | 6.1176          |
| 6.1562        | 10.97 | 135000 | 6.1111          |
| 6.15          | 11.37 | 140000 | 6.1063          |
| 6.1488        | 11.78 | 145000 | 6.1046          |
| 6.1449        | 12.19 | 150000 | 6.1023          |
| 6.1397        | 12.59 | 155000 | 6.0961          |
| 6.135         | 13.0  | 160000 | 6.0938          |
| 6.1315        | 13.41 | 165000 | 6.0891          |
| 6.1302        | 13.81 | 170000 | 6.0853          |
| 6.1295        | 14.22 | 175000 | 6.0838          |
| 6.1276        | 14.62 | 180000 | 6.0834          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0
- Datasets 2.2.2
- Tokenizers 0.12.1

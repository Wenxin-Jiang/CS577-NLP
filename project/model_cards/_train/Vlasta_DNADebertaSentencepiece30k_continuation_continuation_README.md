---
tags:
- generated_from_trainer
model-index:
- name: DNADebertaSentencepiece30k_continuation_continuation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DNADebertaSentencepiece30k_continuation_continuation

This model is a fine-tuned version of [Vlasta/DNADebertaSentencepiece30k_continuation](https://huggingface.co/Vlasta/DNADebertaSentencepiece30k_continuation) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 5.9867

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
| 6.1786        | 0.41  | 5000   | 6.1475          |
| 6.1856        | 0.81  | 10000  | 6.1490          |
| 6.1769        | 1.22  | 15000  | 6.1370          |
| 6.1714        | 1.62  | 20000  | 6.1330          |
| 6.1633        | 2.03  | 25000  | 6.1221          |
| 6.1548        | 2.44  | 30000  | 6.1180          |
| 6.1495        | 2.84  | 35000  | 6.1141          |
| 6.1453        | 3.25  | 40000  | 6.1026          |
| 6.1362        | 3.66  | 45000  | 6.0984          |
| 6.1325        | 4.06  | 50000  | 6.0961          |
| 6.1227        | 4.47  | 55000  | 6.0874          |
| 6.1215        | 4.87  | 60000  | 6.0806          |
| 6.1149        | 5.28  | 65000  | 6.0779          |
| 6.1099        | 5.69  | 70000  | 6.0701          |
| 6.104         | 6.09  | 75000  | 6.0633          |
| 6.0963        | 6.5   | 80000  | 6.0628          |
| 6.095         | 6.91  | 85000  | 6.0572          |
| 6.0858        | 7.31  | 90000  | 6.0525          |
| 6.0895        | 7.72  | 95000  | 6.0430          |
| 6.0804        | 8.12  | 100000 | 6.0437          |
| 6.0767        | 8.53  | 105000 | 6.0371          |
| 6.0748        | 8.94  | 110000 | 6.0312          |
| 6.0702        | 9.34  | 115000 | 6.0293          |
| 6.0668        | 9.75  | 120000 | 6.0242          |
| 6.0615        | 10.16 | 125000 | 6.0213          |
| 6.0568        | 10.56 | 130000 | 6.0183          |
| 6.0552        | 10.97 | 135000 | 6.0125          |
| 6.0496        | 11.37 | 140000 | 6.0087          |
| 6.0493        | 11.78 | 145000 | 6.0084          |
| 6.0466        | 12.19 | 150000 | 6.0060          |
| 6.042         | 12.59 | 155000 | 6.0008          |
| 6.0375        | 13.0  | 160000 | 5.9986          |
| 6.0345        | 13.41 | 165000 | 5.9940          |
| 6.0336        | 13.81 | 170000 | 5.9905          |
| 6.0334        | 14.22 | 175000 | 5.9891          |
| 6.0313        | 14.62 | 180000 | 5.9887          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0
- Datasets 2.2.2
- Tokenizers 0.12.1

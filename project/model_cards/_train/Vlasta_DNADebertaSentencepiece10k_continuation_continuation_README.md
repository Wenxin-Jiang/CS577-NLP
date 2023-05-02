---
tags:
- generated_from_trainer
model-index:
- name: DNADebertaSentencepiece10k_continuation_continuation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DNADebertaSentencepiece10k_continuation_continuation

This model is a fine-tuned version of [Vlasta/DNADebertaSentencepiece10k_continuation](https://huggingface.co/Vlasta/DNADebertaSentencepiece10k_continuation) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 5.3056

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
| 5.4806        | 0.36  | 5000   | 5.4385          |
| 5.4848        | 0.72  | 10000  | 5.4333          |
| 5.4803        | 1.08  | 15000  | 5.4312          |
| 5.4759        | 1.45  | 20000  | 5.4223          |
| 5.4703        | 1.81  | 25000  | 5.4199          |
| 5.4626        | 2.17  | 30000  | 5.4147          |
| 5.4596        | 2.53  | 35000  | 5.4094          |
| 5.4534        | 2.89  | 40000  | 5.4014          |
| 5.4466        | 3.25  | 45000  | 5.4017          |
| 5.445         | 3.61  | 50000  | 5.3954          |
| 5.4446        | 3.97  | 55000  | 5.3916          |
| 5.4359        | 4.34  | 60000  | 5.3809          |
| 5.4327        | 4.7   | 65000  | 5.3846          |
| 5.4281        | 5.06  | 70000  | 5.3765          |
| 5.4207        | 5.42  | 75000  | 5.3744          |
| 5.4207        | 5.78  | 80000  | 5.3704          |
| 5.4167        | 6.14  | 85000  | 5.3685          |
| 5.41          | 6.5   | 90000  | 5.3641          |
| 5.4117        | 6.86  | 95000  | 5.3582          |
| 5.4075        | 7.23  | 100000 | 5.3568          |
| 5.4017        | 7.59  | 105000 | 5.3547          |
| 5.4006        | 7.95  | 110000 | 5.3494          |
| 5.3969        | 8.31  | 115000 | 5.3475          |
| 5.3935        | 8.67  | 120000 | 5.3453          |
| 5.3926        | 9.03  | 125000 | 5.3422          |
| 5.3895        | 9.39  | 130000 | 5.3351          |
| 5.3813        | 9.75  | 135000 | 5.3326          |
| 5.3841        | 10.12 | 140000 | 5.3340          |
| 5.3787        | 10.48 | 145000 | 5.3301          |
| 5.3781        | 10.84 | 150000 | 5.3280          |
| 5.3769        | 11.2  | 155000 | 5.3258          |
| 5.3733        | 11.56 | 160000 | 5.3198          |
| 5.3683        | 11.92 | 165000 | 5.3180          |
| 5.3682        | 12.28 | 170000 | 5.3181          |
| 5.3673        | 12.64 | 175000 | 5.3167          |
| 5.3623        | 13.01 | 180000 | 5.3116          |
| 5.3602        | 13.37 | 185000 | 5.3109          |
| 5.361         | 13.73 | 190000 | 5.3071          |
| 5.3573        | 14.09 | 195000 | 5.3078          |
| 5.3575        | 14.45 | 200000 | 5.3051          |
| 5.3544        | 14.81 | 205000 | 5.3038          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0
- Datasets 2.2.2
- Tokenizers 0.12.1

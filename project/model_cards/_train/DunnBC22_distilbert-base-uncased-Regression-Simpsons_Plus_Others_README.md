---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-Regression-Simpsons_Plus_Others
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-Regression-Simpsons_Plus_Others

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3754
- Mse: 0.3754
- Rmse: 0.6127
- Mae: 0.4651

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 25

### Training results

| Training Loss | Epoch | Step | Validation Loss | Mse    | Rmse   | Mae    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|
| 29.5977       | 1.0   | 51   | 7.9215          | 7.9215 | 2.8145 | 2.7032 |
| 4.4551        | 2.0   | 102  | 0.6728          | 0.6728 | 0.8202 | 0.6039 |
| 2.0068        | 3.0   | 153  | 0.6034          | 0.6034 | 0.7768 | 0.5882 |
| 1.8734        | 4.0   | 204  | 0.4423          | 0.4423 | 0.6651 | 0.4975 |
| 1.7607        | 5.0   | 255  | 0.3971          | 0.3971 | 0.6302 | 0.4725 |
| 1.6901        | 6.0   | 306  | 0.4005          | 0.4005 | 0.6328 | 0.4751 |
| 1.6525        | 7.0   | 357  | 0.4001          | 0.4001 | 0.6325 | 0.4766 |
| 1.6103        | 8.0   | 408  | 0.4278          | 0.4278 | 0.6541 | 0.4954 |
| 1.5659        | 9.0   | 459  | 0.3903          | 0.3903 | 0.6247 | 0.4618 |
| 1.4968        | 10.0  | 510  | 0.3987          | 0.3987 | 0.6314 | 0.4670 |
| 1.4983        | 11.0  | 561  | 0.4764          | 0.4764 | 0.6902 | 0.5324 |
| 1.4659        | 12.0  | 612  | 0.3913          | 0.3913 | 0.6256 | 0.4616 |
| 1.4532        | 13.0  | 663  | 0.4511          | 0.4511 | 0.6716 | 0.5153 |
| 1.4515        | 14.0  | 714  | 0.4009          | 0.4009 | 0.6332 | 0.4768 |
| 1.4506        | 15.0  | 765  | 0.4588          | 0.4588 | 0.6773 | 0.5160 |
| 1.4249        | 16.0  | 816  | 0.3940          | 0.3940 | 0.6277 | 0.4630 |
| 1.4254        | 17.0  | 867  | 0.4456          | 0.4456 | 0.6675 | 0.5084 |
| 1.4023        | 18.0  | 918  | 0.4517          | 0.4517 | 0.6721 | 0.5096 |
| 1.3754        | 19.0  | 969  | 0.4210          | 0.4210 | 0.6489 | 0.4869 |
| 1.3865        | 20.0  | 1020 | 0.4163          | 0.4163 | 0.6452 | 0.4830 |
| 1.3802        | 21.0  | 1071 | 0.4290          | 0.4290 | 0.6550 | 0.4904 |
| 1.4087        | 22.0  | 1122 | 0.4097          | 0.4097 | 0.6401 | 0.4745 |
| 1.3855        | 23.0  | 1173 | 0.4438          | 0.4438 | 0.6662 | 0.5027 |
| 1.3911        | 24.0  | 1224 | 0.4302          | 0.4302 | 0.6559 | 0.4906 |
| 1.3877        | 25.0  | 1275 | 0.4287          | 0.4287 | 0.6547 | 0.4887 |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1

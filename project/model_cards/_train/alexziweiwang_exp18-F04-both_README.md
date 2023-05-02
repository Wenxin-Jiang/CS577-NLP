---
tags:
- generated_from_trainer
model-index:
- name: exp18-F04-both
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# exp18-F04-both

This model is a fine-tuned version of [yongjian/wav2vec2-large-a](https://huggingface.co/yongjian/wav2vec2-large-a) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4137
- Wer: 0.4647

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 41.5777       | 0.34  | 500   | 3.0940          | 1.0188 |
| 3.2064        | 0.68  | 1000  | 2.8577          | 1.0157 |
| 2.997         | 1.02  | 1500  | 2.7604          | 1.0126 |
| 2.8537        | 1.36  | 2000  | 2.7305          | 1.0    |
| 2.6677        | 1.7   | 2500  | 2.3201          | 1.2512 |
| 2.4414        | 2.04  | 3000  | 2.1550          | 1.2575 |
| 2.2113        | 2.38  | 3500  | 2.0825          | 1.2433 |
| 2.0619        | 2.72  | 4000  | 2.0245          | 1.2245 |
| 1.921         | 3.07  | 4500  | 1.6541          | 1.2057 |
| 1.8182        | 3.41  | 5000  | 1.3678          | 1.1962 |
| 1.759         | 3.75  | 5500  | 1.1805          | 1.2214 |
| 1.6229        | 4.09  | 6000  | 1.0100          | 1.1695 |
| 1.4557        | 4.43  | 6500  | 0.8956          | 1.1287 |
| 1.4799        | 4.77  | 7000  | 0.7858          | 1.0801 |
| 1.3277        | 5.11  | 7500  | 0.7306          | 1.0267 |
| 1.2419        | 5.45  | 8000  | 0.6326          | 0.9262 |
| 1.1537        | 5.79  | 8500  | 0.6280          | 0.8901 |
| 1.0972        | 6.13  | 9000  | 0.5639          | 0.9027 |
| 1.0375        | 6.47  | 9500  | 0.7219          | 0.8352 |
| 0.9301        | 6.81  | 10000 | 0.4786          | 0.7881 |
| 0.9423        | 7.15  | 10500 | 0.4969          | 0.7441 |
| 0.8276        | 7.49  | 11000 | 0.4640          | 0.7551 |
| 0.8674        | 7.83  | 11500 | 0.5401          | 0.7582 |
| 0.7633        | 8.17  | 12000 | 0.4610          | 0.6970 |
| 0.7314        | 8.51  | 12500 | 0.4026          | 0.6923 |
| 0.7259        | 8.86  | 13000 | 0.4874          | 0.6970 |
| 0.6591        | 9.2   | 13500 | 0.4701          | 0.6546 |
| 0.615         | 9.54  | 14000 | 0.4259          | 0.6421 |
| 0.6098        | 9.88  | 14500 | 0.4206          | 0.6122 |
| 0.554         | 10.22 | 15000 | 0.4550          | 0.6201 |
| 0.5521        | 10.56 | 15500 | 0.4777          | 0.6154 |
| 0.5726        | 10.9  | 16000 | 0.3307          | 0.5997 |
| 0.5301        | 11.24 | 16500 | 0.4095          | 0.5777 |
| 0.5098        | 11.58 | 17000 | 0.4914          | 0.5934 |
| 0.5174        | 11.92 | 17500 | 0.4223          | 0.5981 |
| 0.4674        | 12.26 | 18000 | 0.3593          | 0.5651 |
| 0.4574        | 12.6  | 18500 | 0.3951          | 0.5651 |
| 0.4182        | 12.94 | 19000 | 0.4727          | 0.5808 |
| 0.388         | 13.28 | 19500 | 0.4737          | 0.5447 |
| 0.3924        | 13.62 | 20000 | 0.4047          | 0.5322 |
| 0.3752        | 13.96 | 20500 | 0.3499          | 0.5306 |
| 0.3374        | 14.31 | 21000 | 0.2930          | 0.5243 |
| 0.3239        | 14.65 | 21500 | 0.4708          | 0.5338 |
| 0.3609        | 14.99 | 22000 | 0.3415          | 0.5118 |
| 0.309         | 15.33 | 22500 | 0.4738          | 0.5149 |
| 0.2987        | 15.67 | 23000 | 0.4351          | 0.5275 |
| 0.3726        | 16.01 | 23500 | 0.4305          | 0.5306 |
| 0.3075        | 16.35 | 24000 | 0.3290          | 0.5212 |
| 0.2995        | 16.69 | 24500 | 0.3386          | 0.4976 |
| 0.3262        | 17.03 | 25000 | 0.5279          | 0.5165 |
| 0.2607        | 17.37 | 25500 | 0.3836          | 0.5008 |
| 0.2664        | 17.71 | 26000 | 0.4128          | 0.4961 |
| 0.2578        | 18.05 | 26500 | 0.3517          | 0.4945 |
| 0.2443        | 18.39 | 27000 | 0.3126          | 0.4804 |
| 0.2488        | 18.73 | 27500 | 0.3895          | 0.4976 |
| 0.2382        | 19.07 | 28000 | 0.5097          | 0.5055 |
| 0.2684        | 19.41 | 28500 | 0.4171          | 0.5071 |
| 0.2038        | 19.75 | 29000 | 0.4126          | 0.4851 |
| 0.2273        | 20.1  | 29500 | 0.4142          | 0.4898 |
| 0.2144        | 20.44 | 30000 | 0.5022          | 0.4961 |
| 0.2274        | 20.78 | 30500 | 0.4640          | 0.4819 |
| 0.2055        | 21.12 | 31000 | 0.5124          | 0.4851 |
| 0.1814        | 21.46 | 31500 | 0.4745          | 0.4804 |
| 0.201         | 21.8  | 32000 | 0.4669          | 0.4835 |
| 0.1788        | 22.14 | 32500 | 0.5168          | 0.4851 |
| 0.2206        | 22.48 | 33000 | 0.4279          | 0.4772 |
| 0.1847        | 22.82 | 33500 | 0.3862          | 0.4772 |
| 0.1875        | 23.16 | 34000 | 0.4506          | 0.4851 |
| 0.1546        | 23.5  | 34500 | 0.4411          | 0.4867 |
| 0.1768        | 23.84 | 35000 | 0.3386          | 0.4584 |
| 0.1601        | 24.18 | 35500 | 0.3914          | 0.4678 |
| 0.1815        | 24.52 | 36000 | 0.3449          | 0.4600 |
| 0.1495        | 24.86 | 36500 | 0.4789          | 0.4819 |
| 0.1347        | 25.2  | 37000 | 0.4584          | 0.4741 |
| 0.1516        | 25.54 | 37500 | 0.3993          | 0.4678 |
| 0.1514        | 25.89 | 38000 | 0.3898          | 0.4662 |
| 0.1288        | 26.23 | 38500 | 0.4486          | 0.4819 |
| 0.1414        | 26.57 | 39000 | 0.4233          | 0.4835 |
| 0.1407        | 26.91 | 39500 | 0.4119          | 0.4710 |
| 0.1383        | 27.25 | 40000 | 0.4084          | 0.4788 |
| 0.1391        | 27.59 | 40500 | 0.4254          | 0.4757 |
| 0.1302        | 27.93 | 41000 | 0.4208          | 0.4741 |
| 0.1335        | 28.27 | 41500 | 0.3952          | 0.4662 |
| 0.1426        | 28.61 | 42000 | 0.4086          | 0.4647 |
| 0.1303        | 28.95 | 42500 | 0.4071          | 0.4615 |
| 0.1148        | 29.29 | 43000 | 0.4220          | 0.4662 |
| 0.1131        | 29.63 | 43500 | 0.4170          | 0.4662 |
| 0.0998        | 29.97 | 44000 | 0.4137          | 0.4647 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.2
---
tags:
- generated_from_trainer
model-index:
- name: combined-MTL9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# combined-MTL9

This model is a fine-tuned version of [yongjian/wav2vec2-large-a](https://huggingface.co/yongjian/wav2vec2-large-a) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3413
- Wer: 0.8603

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
| 76.4918       | 0.35  | 500   | 3.4171          | 1.0    |
| 2.9927        | 0.69  | 1000  | 2.4743          | 1.0667 |
| 2.2033        | 1.04  | 1500  | 1.6693          | 1.25   |
| 1.6165        | 1.39  | 2000  | 1.5341          | 1.1808 |
| 1.4208        | 1.74  | 2500  | 1.3148          | 1.1179 |
| 1.2858        | 2.08  | 3000  | 1.2272          | 1.0872 |
| 1.1317        | 2.43  | 3500  | 1.0865          | 1.0731 |
| 1.0668        | 2.78  | 4000  | 1.0798          | 1.0474 |
| 1.0429        | 3.12  | 4500  | 1.4627          | 1.0936 |
| 0.9615        | 3.47  | 5000  | 1.2540          | 1.0090 |
| 0.975         | 3.82  | 5500  | 0.9936          | 0.9679 |
| 0.8517        | 4.17  | 6000  | 1.1039          | 1.0282 |
| 0.8281        | 4.51  | 6500  | 1.0609          | 0.9897 |
| 0.8413        | 4.86  | 7000  | 0.9513          | 0.9397 |
| 0.7618        | 5.21  | 7500  | 1.1656          | 0.9718 |
| 0.7173        | 5.56  | 8000  | 1.1974          | 0.9603 |
| 0.7449        | 5.9   | 8500  | 1.0144          | 0.9731 |
| 0.6762        | 6.25  | 9000  | 1.1774          | 0.9231 |
| 0.6749        | 6.6   | 9500  | 1.1823          | 0.9205 |
| 0.6776        | 6.94  | 10000 | 0.9167          | 0.9244 |
| 0.5937        | 7.29  | 10500 | 1.3344          | 0.9769 |
| 0.6488        | 7.64  | 11000 | 1.0245          | 0.9692 |
| 0.6116        | 7.99  | 11500 | 0.9444          | 0.9141 |
| 0.5497        | 8.33  | 12000 | 0.9499          | 0.9692 |
| 0.5937        | 8.68  | 12500 | 1.1087          | 0.9231 |
| 0.5268        | 9.03  | 13000 | 1.3408          | 0.9269 |
| 0.5078        | 9.38  | 13500 | 1.1737          | 0.9038 |
| 0.497         | 9.72  | 14000 | 0.9963          | 0.8987 |
| 0.5231        | 10.07 | 14500 | 1.3247          | 0.9590 |
| 0.4651        | 10.42 | 15000 | 1.1988          | 0.9308 |
| 0.481         | 10.76 | 15500 | 1.0034          | 0.9308 |
| 0.481         | 11.11 | 16000 | 1.0040          | 0.8782 |
| 0.4751        | 11.46 | 16500 | 0.8824          | 0.8538 |
| 0.4554        | 11.81 | 17000 | 0.9741          | 0.8821 |
| 0.426         | 12.15 | 17500 | 0.8552          | 0.8615 |
| 0.4186        | 12.5  | 18000 | 1.0646          | 0.8833 |
| 0.4154        | 12.85 | 18500 | 0.9618          | 0.8936 |
| 0.5115        | 13.19 | 19000 | 1.0312          | 0.8910 |
| 0.3564        | 13.54 | 19500 | 1.0686          | 0.8769 |
| 0.3927        | 13.89 | 20000 | 1.2533          | 0.9103 |
| 0.3628        | 14.24 | 20500 | 1.2945          | 0.8872 |
| 0.3808        | 14.58 | 21000 | 1.0195          | 0.8538 |
| 0.3981        | 14.93 | 21500 | 1.0388          | 0.8808 |
| 0.3337        | 15.28 | 22000 | 1.0464          | 0.8923 |
| 0.3092        | 15.62 | 22500 | 1.0843          | 0.8705 |
| 0.378         | 15.97 | 23000 | 1.0880          | 0.8859 |
| 0.3231        | 16.32 | 23500 | 0.9205          | 0.8782 |
| 0.3588        | 16.67 | 24000 | 1.0064          | 0.8962 |
| 0.3048        | 17.01 | 24500 | 0.9130          | 0.8705 |
| 0.3           | 17.36 | 25000 | 1.0100          | 0.9077 |
| 0.3045        | 17.71 | 25500 | 1.0559          | 0.9077 |
| 0.3024        | 18.06 | 26000 | 1.1225          | 0.9026 |
| 0.2614        | 18.4  | 26500 | 1.0911          | 0.8897 |
| 0.2755        | 18.75 | 27000 | 1.0872          | 0.8808 |
| 0.2798        | 19.1  | 27500 | 1.2911          | 0.9154 |
| 0.2455        | 19.44 | 28000 | 1.0646          | 0.8821 |
| 0.2524        | 19.79 | 28500 | 1.3356          | 0.9154 |
| 0.2435        | 20.14 | 29000 | 1.1257          | 0.8641 |
| 0.2458        | 20.49 | 29500 | 1.2221          | 0.8667 |
| 0.2216        | 20.83 | 30000 | 1.1364          | 0.8769 |
| 0.234         | 21.18 | 30500 | 1.2094          | 0.8808 |
| 0.233         | 21.53 | 31000 | 1.1604          | 0.8910 |
| 0.2536        | 21.88 | 31500 | 1.0934          | 0.8808 |
| 0.1885        | 22.22 | 32000 | 1.2177          | 0.8718 |
| 0.2186        | 22.57 | 32500 | 1.0539          | 0.8667 |
| 0.1991        | 22.92 | 33000 | 1.2222          | 0.8641 |
| 0.2027        | 23.26 | 33500 | 1.3863          | 0.8577 |
| 0.193         | 23.61 | 34000 | 1.2293          | 0.8705 |
| 0.2054        | 23.96 | 34500 | 1.3398          | 0.8769 |
| 0.2197        | 24.31 | 35000 | 1.3138          | 0.8705 |
| 0.1898        | 24.65 | 35500 | 1.2897          | 0.8679 |
| 0.1933        | 25.0  | 36000 | 1.2666          | 0.8769 |
| 0.1632        | 25.35 | 36500 | 1.2758          | 0.8756 |
| 0.1869        | 25.69 | 37000 | 1.1811          | 0.8603 |
| 0.1731        | 26.04 | 37500 | 1.2511          | 0.8679 |
| 0.1821        | 26.39 | 38000 | 1.3391          | 0.8718 |
| 0.1648        | 26.74 | 38500 | 1.2505          | 0.8628 |
| 0.1909        | 27.08 | 39000 | 1.2984          | 0.85   |
| 0.1902        | 27.43 | 39500 | 1.2261          | 0.8487 |
| 0.1449        | 27.78 | 40000 | 1.2853          | 0.8487 |
| 0.1583        | 28.12 | 40500 | 1.3361          | 0.8628 |
| 0.148         | 28.47 | 41000 | 1.3638          | 0.8654 |
| 0.1648        | 28.82 | 41500 | 1.3380          | 0.8603 |
| 0.1461        | 29.17 | 42000 | 1.3561          | 0.8603 |
| 0.1565        | 29.51 | 42500 | 1.3489          | 0.8615 |
| 0.16          | 29.86 | 43000 | 1.3413          | 0.8603 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.2
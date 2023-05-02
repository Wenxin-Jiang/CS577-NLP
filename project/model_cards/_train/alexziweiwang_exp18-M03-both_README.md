---
tags:
- generated_from_trainer
model-index:
- name: exp18-M03-both
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# exp18-M03-both

This model is a fine-tuned version of [yongjian/wav2vec2-large-a](https://huggingface.co/yongjian/wav2vec2-large-a) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4134
- Wer: 0.8533

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
| 44.7613       | 0.35  | 500   | 3.3891          | 1.0525 |
| 3.1954        | 0.7   | 1000  | 2.8766          | 1.0    |
| 2.9522        | 1.05  | 1500  | 2.7578          | 1.0    |
| 2.843         | 1.4   | 2000  | 2.5628          | 1.1318 |
| 2.6645        | 1.75  | 2500  | 2.1406          | 1.2864 |
| 2.3587        | 2.1   | 3000  | 1.8164          | 1.2934 |
| 2.1731        | 2.45  | 3500  | 1.5732          | 1.2775 |
| 2.0242        | 2.8   | 4000  | 1.4249          | 1.2666 |
| 1.9453        | 3.15  | 4500  | 1.3079          | 1.2220 |
| 1.7871        | 3.5   | 5000  | 1.2389          | 1.2081 |
| 1.7147        | 3.85  | 5500  | 1.1724          | 1.2101 |
| 1.5729        | 4.2   | 6000  | 1.1638          | 1.1982 |
| 1.4966        | 4.55  | 6500  | 1.0529          | 1.1497 |
| 1.3898        | 4.9   | 7000  | 1.0808          | 1.1506 |
| 1.3447        | 5.25  | 7500  | 0.9702          | 1.1229 |
| 1.2342        | 5.6   | 8000  | 0.8994          | 1.1219 |
| 1.1918        | 5.95  | 8500  | 0.9212          | 1.1169 |
| 1.1037        | 6.3   | 9000  | 0.9057          | 1.1080 |
| 1.0661        | 6.65  | 9500  | 0.8231          | 1.1110 |
| 1.0501        | 7.0   | 10000 | 0.8291          | 1.0912 |
| 0.9069        | 7.35  | 10500 | 0.8360          | 1.0902 |
| 0.8959        | 7.7   | 11000 | 0.7961          | 1.0684 |
| 0.9256        | 8.05  | 11500 | 0.7459          | 1.0684 |
| 0.8686        | 8.4   | 12000 | 0.7276          | 1.0456 |
| 0.7998        | 8.75  | 12500 | 0.7195          | 1.0525 |
| 0.7406        | 9.1   | 13000 | 0.7471          | 1.0515 |
| 0.7646        | 9.45  | 13500 | 0.7716          | 1.0624 |
| 0.7018        | 9.8   | 14000 | 0.7262          | 1.0446 |
| 0.7114        | 10.15 | 14500 | 0.6795          | 1.0327 |
| 0.6498        | 10.5  | 15000 | 0.6724          | 1.0347 |
| 0.6652        | 10.85 | 15500 | 0.6994          | 1.0347 |
| 0.638         | 11.2  | 16000 | 0.6565          | 1.0159 |
| 0.6078        | 11.55 | 16500 | 0.6695          | 1.0575 |
| 0.588         | 11.9  | 17000 | 0.6391          | 1.0149 |
| 0.5722        | 12.25 | 17500 | 0.6321          | 1.0188 |
| 0.5505        | 12.6  | 18000 | 0.6306          | 1.0089 |
| 0.5297        | 12.95 | 18500 | 0.6100          | 1.0139 |
| 0.5188        | 13.3  | 19000 | 0.5426          | 0.9931 |
| 0.4865        | 13.65 | 19500 | 0.5410          | 0.9881 |
| 0.5132        | 14.0  | 20000 | 0.5095          | 0.9792 |
| 0.4782        | 14.35 | 20500 | 0.4962          | 0.9901 |
| 0.4627        | 14.7  | 21000 | 0.5277          | 0.9871 |
| 0.4568        | 15.05 | 21500 | 0.4958          | 0.9683 |
| 0.4312        | 15.4  | 22000 | 0.5146          | 0.9752 |
| 0.4286        | 15.75 | 22500 | 0.4682          | 0.9693 |
| 0.428         | 16.1  | 23000 | 0.5121          | 0.9851 |
| 0.3656        | 16.45 | 23500 | 0.4894          | 0.9485 |
| 0.3884        | 16.79 | 24000 | 0.4832          | 0.9465 |
| 0.3835        | 17.14 | 24500 | 0.4925          | 0.9841 |
| 0.3584        | 17.49 | 25000 | 0.5503          | 0.9782 |
| 0.3719        | 17.84 | 25500 | 0.4960          | 0.9415 |
| 0.3555        | 18.19 | 26000 | 0.4238          | 0.9594 |
| 0.3196        | 18.54 | 26500 | 0.4501          | 0.9495 |
| 0.3288        | 18.89 | 27000 | 0.5292          | 0.9564 |
| 0.3402        | 19.24 | 27500 | 0.4156          | 0.9475 |
| 0.2889        | 19.59 | 28000 | 0.4056          | 0.9633 |
| 0.3562        | 19.94 | 28500 | 0.3972          | 0.9504 |
| 0.336         | 20.29 | 29000 | 0.4021          | 0.9257 |
| 0.2952        | 20.64 | 29500 | 0.3920          | 0.9167 |
| 0.2678        | 20.99 | 30000 | 0.3610          | 0.9049 |
| 0.2816        | 21.34 | 30500 | 0.3782          | 0.9267 |
| 0.2718        | 21.69 | 31000 | 0.3502          | 0.9068 |
| 0.2948        | 22.04 | 31500 | 0.3412          | 0.9078 |
| 0.2782        | 22.39 | 32000 | 0.3799          | 0.9039 |
| 0.2668        | 22.74 | 32500 | 0.3725          | 0.9058 |
| 0.2685        | 23.09 | 33000 | 0.3825          | 0.8880 |
| 0.2514        | 23.44 | 33500 | 0.3618          | 0.8791 |
| 0.2305        | 23.79 | 34000 | 0.4211          | 0.8870 |
| 0.2671        | 24.14 | 34500 | 0.4126          | 0.8900 |
| 0.2153        | 24.49 | 35000 | 0.4106          | 0.8801 |
| 0.2323        | 24.84 | 35500 | 0.3845          | 0.8751 |
| 0.2208        | 25.19 | 36000 | 0.4017          | 0.8741 |
| 0.2023        | 25.54 | 36500 | 0.4451          | 0.8662 |
| 0.232         | 25.89 | 37000 | 0.4133          | 0.8583 |
| 0.2101        | 26.24 | 37500 | 0.4118          | 0.8662 |
| 0.2139        | 26.59 | 38000 | 0.3937          | 0.8682 |
| 0.1917        | 26.94 | 38500 | 0.4015          | 0.8603 |
| 0.1904        | 27.29 | 39000 | 0.4018          | 0.8622 |
| 0.2265        | 27.64 | 39500 | 0.3983          | 0.8573 |
| 0.2081        | 27.99 | 40000 | 0.4027          | 0.8563 |
| 0.2124        | 28.34 | 40500 | 0.4172          | 0.8523 |
| 0.191         | 28.69 | 41000 | 0.4018          | 0.8444 |
| 0.1906        | 29.04 | 41500 | 0.4148          | 0.8494 |
| 0.1613        | 29.39 | 42000 | 0.4195          | 0.8543 |
| 0.1864        | 29.74 | 42500 | 0.4134          | 0.8533 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.13.2
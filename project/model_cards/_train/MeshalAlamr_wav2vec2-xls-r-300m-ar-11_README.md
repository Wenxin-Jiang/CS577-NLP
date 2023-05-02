---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-xls-r-300m-ar-11
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-ar-11

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 60.5659
- Wer: 0.2144

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 16849.2529    | 1.0   | 85   | 1458.4645       | 1.0    |
| 4474.9085     | 2.0   | 170  | 687.2793        | 1.0    |
| 2937.0309     | 3.0   | 255  | 632.0456        | 1.0    |
| 2853.7682     | 4.0   | 340  | 621.7872        | 1.0    |
| 2786.243      | 5.0   | 425  | 611.4717        | 1.0    |
| 2738.1844     | 6.0   | 510  | 578.0577        | 1.0    |
| 2118.4608     | 7.0   | 595  | 253.0534        | 0.9927 |
| 1026.4239     | 8.0   | 680  | 140.3523        | 0.6430 |
| 682.4369      | 9.0   | 765  | 106.5226        | 0.4990 |
| 516.4381      | 10.0  | 850  | 85.3184         | 0.4126 |
| 434.9369      | 11.0  | 935  | 79.4750         | 0.3683 |
| 369.3786      | 12.0  | 1020 | 73.2318         | 0.3290 |
| 324.2687      | 13.0  | 1105 | 69.6444         | 0.3160 |
| 292.8527      | 14.0  | 1190 | 66.7714         | 0.2922 |
| 266.229       | 15.0  | 1275 | 68.2237         | 0.2839 |
| 242.3606      | 16.0  | 1360 | 66.0233         | 0.2745 |
| 227.9846      | 17.0  | 1445 | 66.8503         | 0.2668 |
| 210.1087      | 18.0  | 1530 | 63.1035         | 0.2539 |
| 201.326       | 19.0  | 1615 | 63.9665         | 0.2481 |
| 189.019       | 20.0  | 1700 | 60.9628         | 0.2418 |
| 181.3091      | 21.0  | 1785 | 62.5716         | 0.2387 |
| 168.631       | 22.0  | 1870 | 62.4718         | 0.2342 |
| 165.8396      | 23.0  | 1955 | 61.0784         | 0.2287 |
| 161.4992      | 24.0  | 2040 | 62.2299         | 0.2257 |
| 153.6809      | 25.0  | 2125 | 60.4889         | 0.2235 |
| 145.4282      | 26.0  | 2210 | 60.8189         | 0.2208 |
| 144.6855      | 27.0  | 2295 | 61.8122         | 0.2203 |
| 138.6269      | 28.0  | 2380 | 60.4600         | 0.2172 |
| 137.6246      | 29.0  | 2465 | 61.4417         | 0.2167 |
| 134.6211      | 30.0  | 2550 | 60.5659         | 0.2144 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0
- Datasets 1.18.4
- Tokenizers 0.11.6

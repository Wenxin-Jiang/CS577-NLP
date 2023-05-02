---
tags:
- generated_from_trainer
model-index:
- name: from_scratch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# from_scratch

This model is a fine-tuned version of [tokenizer/config.json](https://huggingface.co/tokenizer/config.json) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4744

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
- train_batch_size: 360
- eval_batch_size: 360
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-06
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10000
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step    | Validation Loss |
|:-------------:|:-----:|:-------:|:---------------:|
| 1.0952        | 0.05  | 20000   | 1.0383          |
| 0.936         | 0.1   | 40000   | 0.8852          |
| 0.8679        | 0.14  | 60000   | 0.8207          |
| 0.8276        | 0.19  | 80000   | 0.7796          |
| 0.796         | 0.24  | 100000  | 0.7519          |
| 0.7756        | 0.29  | 120000  | 0.7299          |
| 0.7545        | 0.33  | 140000  | 0.7103          |
| 0.7395        | 0.38  | 160000  | 0.6947          |
| 0.7236        | 0.43  | 180000  | 0.6809          |
| 0.7143        | 0.48  | 200000  | 0.6705          |
| 0.705         | 0.52  | 220000  | 0.6585          |
| 0.6904        | 0.57  | 240000  | 0.6479          |
| 0.6835        | 0.62  | 260000  | 0.6388          |
| 0.672         | 0.67  | 280000  | 0.6290          |
| 0.665         | 0.72  | 300000  | 0.6217          |
| 0.6581        | 0.76  | 320000  | 0.6136          |
| 0.6466        | 0.81  | 340000  | 0.6071          |
| 0.6396        | 0.86  | 360000  | 0.6000          |
| 0.6343        | 0.91  | 380000  | 0.5940          |
| 0.6286        | 0.95  | 400000  | 0.5880          |
| 0.6183        | 1.0   | 420000  | 0.5809          |
| 0.6134        | 1.05  | 440000  | 0.5757          |
| 0.6094        | 1.1   | 460000  | 0.5693          |
| 0.6032        | 1.15  | 480000  | 0.5641          |
| 0.5954        | 1.19  | 500000  | 0.5596          |
| 0.5915        | 1.24  | 520000  | 0.5532          |
| 0.5845        | 1.29  | 540000  | 0.5489          |
| 0.5823        | 1.34  | 560000  | 0.5437          |
| 0.5754        | 1.38  | 580000  | 0.5393          |
| 0.573         | 1.43  | 600000  | 0.5345          |
| 0.5643        | 1.48  | 620000  | 0.5309          |
| 0.5627        | 1.53  | 640000  | 0.5262          |
| 0.56          | 1.57  | 660000  | 0.5220          |
| 0.5554        | 1.62  | 680000  | 0.5186          |
| 0.5507        | 1.67  | 700000  | 0.5152          |
| 0.5494        | 1.72  | 720000  | 0.5117          |
| 0.5445        | 1.77  | 740000  | 0.5076          |
| 0.5396        | 1.81  | 760000  | 0.5051          |
| 0.5363        | 1.86  | 780000  | 0.5026          |
| 0.5356        | 1.91  | 800000  | 0.4998          |
| 0.5303        | 1.96  | 820000  | 0.4982          |
| 0.5583        | 2.0   | 840000  | 0.5195          |
| 0.5565        | 2.05  | 860000  | 0.5180          |
| 0.5535        | 2.1   | 880000  | 0.5158          |
| 0.5497        | 2.15  | 900000  | 0.5133          |
| 0.5511        | 2.19  | 920000  | 0.5110          |
| 0.5439        | 2.24  | 940000  | 0.5085          |
| 0.5413        | 2.29  | 960000  | 0.5060          |
| 0.5376        | 2.34  | 980000  | 0.5023          |
| 0.5333        | 2.39  | 1000000 | 0.5004          |
| 0.5322        | 2.43  | 1020000 | 0.4973          |
| 0.5312        | 2.48  | 1040000 | 0.4941          |
| 0.5281        | 2.53  | 1060000 | 0.4921          |
| 0.5267        | 2.58  | 1080000 | 0.4902          |
| 0.5257        | 2.62  | 1100000 | 0.4871          |
| 0.5174        | 2.67  | 1120000 | 0.4849          |
| 0.5183        | 2.72  | 1140000 | 0.4825          |
| 0.5181        | 2.77  | 1160000 | 0.4807          |
| 0.5116        | 2.81  | 1180000 | 0.4784          |
| 0.5092        | 2.86  | 1200000 | 0.4769          |
| 0.5109        | 2.91  | 1220000 | 0.4757          |
| 0.5102        | 2.96  | 1240000 | 0.4739          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu117
- Datasets 2.8.0
- Tokenizers 0.13.2

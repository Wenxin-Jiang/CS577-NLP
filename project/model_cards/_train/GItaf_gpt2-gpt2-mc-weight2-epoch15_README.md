---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-mc-weight2-epoch15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-mc-weight2-epoch15

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 11.3067
- Cls loss: 3.6680
- Lm loss: 3.9663
- Cls Accuracy: 0.6069
- Cls F1: 0.6023
- Cls Precision: 0.6050
- Cls Recall: 0.6069
- Perplexity: 52.79

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:-------:|:------------:|:------:|:-------------:|:----------:|:----------:|
| 8.1971        | 1.0   | 3470  | 7.6018          | 1.7777   | 4.0471  | 0.5251       | 0.4892 | 0.5282        | 0.5251     | 57.23      |
| 7.0508        | 2.0   | 6940  | 7.2679          | 1.6195   | 4.0269  | 0.6058       | 0.6001 | 0.6226        | 0.6058     | 56.08      |
| 6.5979        | 3.0   | 10410 | 7.4637          | 1.7253   | 4.0112  | 0.6184       | 0.6109 | 0.6367        | 0.6184     | 55.21      |
| 6.1811        | 4.0   | 13880 | 7.8253          | 1.9084   | 4.0063  | 0.6121       | 0.6074 | 0.6207        | 0.6121     | 54.94      |
| 5.7242        | 5.0   | 17350 | 8.1576          | 2.0824   | 3.9903  | 0.6219       | 0.6166 | 0.6195        | 0.6219     | 54.07      |
| 5.2588        | 6.0   | 20820 | 8.9472          | 2.4785   | 3.9872  | 0.6006       | 0.5942 | 0.6169        | 0.6006     | 53.90      |
| 4.8854        | 7.0   | 24290 | 9.2399          | 2.6264   | 3.9840  | 0.6063       | 0.5988 | 0.6123        | 0.6063     | 53.73      |
| 4.5785        | 8.0   | 27760 | 9.7123          | 2.8660   | 3.9768  | 0.6121       | 0.6076 | 0.6124        | 0.6121     | 53.35      |
| 4.3508        | 9.0   | 31230 | 10.2550         | 3.1400   | 3.9712  | 0.6086       | 0.6017 | 0.6121        | 0.6086     | 53.05      |
| 4.1817        | 10.0  | 34700 | 10.3110         | 3.1681   | 3.9711  | 0.6058       | 0.5990 | 0.6047        | 0.6058     | 53.04      |
| 4.0546        | 11.0  | 38170 | 11.0526         | 3.5396   | 3.9693  | 0.5988       | 0.5929 | 0.5997        | 0.5988     | 52.95      |
| 3.9481        | 12.0  | 41640 | 11.0193         | 3.5238   | 3.9675  | 0.6086       | 0.6038 | 0.6049        | 0.6086     | 52.85      |
| 3.9008        | 13.0  | 45110 | 11.2499         | 3.6394   | 3.9669  | 0.6121       | 0.6073 | 0.6090        | 0.6121     | 52.82      |
| 3.8558        | 14.0  | 48580 | 11.3606         | 3.6948   | 3.9666  | 0.6063       | 0.6000 | 0.6034        | 0.6063     | 52.81      |
| 3.8297        | 15.0  | 52050 | 11.3067         | 3.6680   | 3.9663  | 0.6069       | 0.6023 | 0.6050        | 0.6069     | 52.79      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
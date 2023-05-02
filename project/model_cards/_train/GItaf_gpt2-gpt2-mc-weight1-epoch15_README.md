---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-mc-weight1-epoch15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-mc-weight1-epoch15

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 7.6876
- Cls loss: 3.7214
- Lm loss: 3.9640
- Cls Accuracy: 0.6040
- Cls F1: 0.5981
- Cls Precision: 0.6050
- Cls Recall: 0.6040
- Perplexity: 52.67

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
| 6.3006        | 1.0   | 3470  | 5.7550          | 1.7137   | 4.0417  | 0.5326       | 0.4990 | 0.4983        | 0.5326     | 56.92      |
| 5.5103        | 2.0   | 6940  | 5.5608          | 1.5450   | 4.0149  | 0.6075       | 0.6009 | 0.6160        | 0.6075     | 55.42      |
| 5.2167        | 3.0   | 10410 | 5.7608          | 1.7609   | 3.9988  | 0.5977       | 0.5917 | 0.6161        | 0.5977     | 54.53      |
| 4.9916        | 4.0   | 13880 | 5.8042          | 1.8106   | 3.9925  | 0.6035       | 0.5979 | 0.6063        | 0.6035     | 54.19      |
| 4.7224        | 5.0   | 17350 | 6.0519          | 2.0699   | 3.9807  | 0.6144       | 0.6100 | 0.6152        | 0.6144     | 53.56      |
| 4.4802        | 6.0   | 20820 | 6.3862          | 2.4050   | 3.9798  | 0.5948       | 0.5883 | 0.6071        | 0.5948     | 53.51      |
| 4.2926        | 7.0   | 24290 | 6.5793          | 2.6045   | 3.9733  | 0.5890       | 0.5819 | 0.5940        | 0.5890     | 53.16      |
| 4.1321        | 8.0   | 27760 | 6.8574          | 2.8865   | 3.9692  | 0.5977       | 0.5937 | 0.6047        | 0.5977     | 52.94      |
| 4.022         | 9.0   | 31230 | 7.1316          | 3.1624   | 3.9673  | 0.5948       | 0.5882 | 0.5980        | 0.5948     | 52.84      |
| 3.9255        | 10.0  | 34700 | 7.1732          | 3.2049   | 3.9664  | 0.6017       | 0.5985 | 0.6009        | 0.6017     | 52.79      |
| 3.8619        | 11.0  | 38170 | 7.3778          | 3.4104   | 3.9653  | 0.5994       | 0.5929 | 0.5994        | 0.5994     | 52.74      |
| 3.8141        | 12.0  | 41640 | 7.5111          | 3.5452   | 3.9638  | 0.5873       | 0.5834 | 0.5916        | 0.5873     | 52.66      |
| 3.7859        | 13.0  | 45110 | 7.6660          | 3.6998   | 3.9640  | 0.5960       | 0.5889 | 0.5976        | 0.5960     | 52.67      |
| 3.7628        | 14.0  | 48580 | 7.6558          | 3.6900   | 3.9636  | 0.5954       | 0.5899 | 0.5969        | 0.5954     | 52.65      |
| 3.7539        | 15.0  | 52050 | 7.6876          | 3.7214   | 3.9640  | 0.6040       | 0.5981 | 0.6050        | 0.6040     | 52.67      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
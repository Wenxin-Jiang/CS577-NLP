---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-mc-weight0.25-epoch15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-mc-weight0.25-epoch15

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.8155
- Cls loss: 3.4105
- Lm loss: 3.9623
- Cls Accuracy: 0.6104
- Cls F1: 0.6054
- Cls Precision: 0.6110
- Cls Recall: 0.6104
- Perplexity: 52.58

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
| 4.6818        | 1.0   | 3470  | 4.4437          | 1.6250   | 4.0374  | 0.5274       | 0.4958 | 0.5329        | 0.5274     | 56.68      |
| 4.3828        | 2.0   | 6940  | 4.3628          | 1.4528   | 3.9994  | 0.6144       | 0.6088 | 0.6345        | 0.6144     | 54.56      |
| 4.2523        | 3.0   | 10410 | 4.3820          | 1.5899   | 3.9842  | 0.6092       | 0.6025 | 0.6382        | 0.6092     | 53.74      |
| 4.1442        | 4.0   | 13880 | 4.3954          | 1.6755   | 3.9763  | 0.6063       | 0.6010 | 0.6121        | 0.6063     | 53.32      |
| 4.0385        | 5.0   | 17350 | 4.4675          | 2.0051   | 3.9659  | 0.6150       | 0.6105 | 0.6194        | 0.6150     | 52.77      |
| 3.9513        | 6.0   | 20820 | 4.5223          | 2.2257   | 3.9654  | 0.6115       | 0.6049 | 0.6233        | 0.6115     | 52.74      |
| 3.8877        | 7.0   | 24290 | 4.5904          | 2.5003   | 3.9649  | 0.6012       | 0.5956 | 0.6049        | 0.6012     | 52.71      |
| 3.8367        | 8.0   | 27760 | 4.6320          | 2.6812   | 3.9612  | 0.6121       | 0.6061 | 0.6154        | 0.6121     | 52.52      |
| 3.7991        | 9.0   | 31230 | 4.6735          | 2.8534   | 3.9596  | 0.6104       | 0.6059 | 0.6139        | 0.6104     | 52.44      |
| 3.7697        | 10.0  | 34700 | 4.7126          | 3.0044   | 3.9610  | 0.6104       | 0.6063 | 0.6122        | 0.6104     | 52.51      |
| 3.7457        | 11.0  | 38170 | 4.7607          | 3.1961   | 3.9612  | 0.6133       | 0.6072 | 0.6182        | 0.6133     | 52.52      |
| 3.7265        | 12.0  | 41640 | 4.7927          | 3.3216   | 3.9617  | 0.6006       | 0.5951 | 0.6036        | 0.6006     | 52.55      |
| 3.7129        | 13.0  | 45110 | 4.7983          | 3.3431   | 3.9620  | 0.6104       | 0.6039 | 0.6133        | 0.6104     | 52.56      |
| 3.7016        | 14.0  | 48580 | 4.8061          | 3.3774   | 3.9612  | 0.6121       | 0.6059 | 0.6124        | 0.6121     | 52.52      |
| 3.6956        | 15.0  | 52050 | 4.8155          | 3.4105   | 3.9623  | 0.6104       | 0.6054 | 0.6110        | 0.6104     | 52.58      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1

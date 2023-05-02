---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- lex_glue
model-index:
- name: ECHR_test_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ECHR_test_2 Task A

This model is a fine-tuned version of [nlpaueb/legal-bert-base-uncased](https://huggingface.co/nlpaueb/legal-bert-base-uncased) on the lex_glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1998
- Macro-f1: 0.5295
- Micro-f1: 0.6157

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Macro-f1 | Micro-f1 |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:--------:|
| 0.2142        | 0.44  | 500   | 0.2887          | 0.2391   | 0.4263   |
| 0.172         | 0.89  | 1000  | 0.2672          | 0.2908   | 0.4628   |
| 0.1737        | 1.33  | 1500  | 0.2612          | 0.3657   | 0.5102   |
| 0.1581        | 1.78  | 2000  | 0.2412          | 0.3958   | 0.5468   |
| 0.1509        | 2.22  | 2500  | 0.2264          | 0.3950   | 0.5552   |
| 0.1606        | 2.67  | 3000  | 0.2342          | 0.4006   | 0.5511   |
| 0.1491        | 3.11  | 3500  | 0.2176          | 0.4558   | 0.5622   |
| 0.1392        | 3.56  | 4000  | 0.2454          | 0.4128   | 0.5596   |
| 0.15          | 4.0   | 4500  | 0.2113          | 0.4684   | 0.5874   |
| 0.1461        | 4.44  | 5000  | 0.2179          | 0.4631   | 0.5815   |
| 0.1457        | 4.89  | 5500  | 0.2151          | 0.4805   | 0.5949   |
| 0.1443        | 5.33  | 6000  | 0.2155          | 0.5123   | 0.5917   |
| 0.1279        | 5.78  | 6500  | 0.2131          | 0.4915   | 0.5998   |
| 0.1377        | 6.22  | 7000  | 0.2244          | 0.4705   | 0.5944   |
| 0.1242        | 6.67  | 7500  | 0.2150          | 0.5089   | 0.5918   |
| 0.1222        | 7.11  | 8000  | 0.2045          | 0.4801   | 0.5981   |
| 0.1372        | 7.56  | 8500  | 0.2074          | 0.5317   | 0.5962   |
| 0.1289        | 8.0   | 9000  | 0.2035          | 0.5323   | 0.6126   |
| 0.1295        | 8.44  | 9500  | 0.2058          | 0.5213   | 0.6073   |
| 0.123         | 8.89  | 10000 | 0.2027          | 0.5486   | 0.6135   |
| 0.1335        | 9.33  | 10500 | 0.1984          | 0.5442   | 0.6249   |
| 0.1258        | 9.78  | 11000 | 0.1998          | 0.5295   | 0.6157   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- lex_glue
model-index:
- name: ECHR_test_Merged
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ECHR_test_Merged

This model is a fine-tuned version of [nlpaueb/legal-bert-base-uncased](https://huggingface.co/nlpaueb/legal-bert-base-uncased) on the lex_glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2162
- Macro-f1: 0.5607
- Micro-f1: 0.6726

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
| 0.2278        | 0.44  | 500   | 0.3196          | 0.2394   | 0.4569   |
| 0.1891        | 0.89  | 1000  | 0.2827          | 0.3255   | 0.5112   |
| 0.1803        | 1.33  | 1500  | 0.2603          | 0.3961   | 0.5698   |
| 0.1676        | 1.78  | 2000  | 0.2590          | 0.4251   | 0.6003   |
| 0.1635        | 2.22  | 2500  | 0.2489          | 0.4186   | 0.6030   |
| 0.1784        | 2.67  | 3000  | 0.2445          | 0.4627   | 0.6159   |
| 0.1556        | 3.11  | 3500  | 0.2398          | 0.4757   | 0.6170   |
| 0.151         | 3.56  | 4000  | 0.2489          | 0.4725   | 0.6163   |
| 0.1564        | 4.0   | 4500  | 0.2289          | 0.5019   | 0.6416   |
| 0.1544        | 4.44  | 5000  | 0.2406          | 0.5013   | 0.6408   |
| 0.1516        | 4.89  | 5500  | 0.2351          | 0.5145   | 0.6510   |
| 0.1487        | 5.33  | 6000  | 0.2354          | 0.5164   | 0.6394   |
| 0.1385        | 5.78  | 6500  | 0.2385          | 0.5205   | 0.6486   |
| 0.145         | 6.22  | 7000  | 0.2337          | 0.5197   | 0.6529   |
| 0.1332        | 6.67  | 7500  | 0.2294          | 0.5421   | 0.6526   |
| 0.1293        | 7.11  | 8000  | 0.2167          | 0.5576   | 0.6652   |
| 0.1475        | 7.56  | 8500  | 0.2218          | 0.5676   | 0.6649   |
| 0.1376        | 8.0   | 9000  | 0.2203          | 0.5565   | 0.6709   |
| 0.1408        | 8.44  | 9500  | 0.2178          | 0.5541   | 0.6716   |
| 0.133         | 8.89  | 10000 | 0.2212          | 0.5692   | 0.6640   |
| 0.1363        | 9.33  | 10500 | 0.2148          | 0.5642   | 0.6736   |
| 0.1344        | 9.78  | 11000 | 0.2162          | 0.5607   | 0.6726   |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

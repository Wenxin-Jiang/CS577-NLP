---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- lex_glue
model-index:
- name: ECHR_test_2_task_B
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ECHR_test_2_task_B

This model is a fine-tuned version of [nlpaueb/legal-bert-base-uncased](https://huggingface.co/nlpaueb/legal-bert-base-uncased) on the lex_glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2092
- Macro-f1: 0.5250
- Micro-f1: 0.6190

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
| 0.2119        | 0.44  | 500   | 0.2945          | 0.2637   | 0.4453   |
| 0.1702        | 0.89  | 1000  | 0.2734          | 0.3246   | 0.4843   |
| 0.1736        | 1.33  | 1500  | 0.2633          | 0.3725   | 0.5133   |
| 0.1571        | 1.78  | 2000  | 0.2549          | 0.3942   | 0.5417   |
| 0.1476        | 2.22  | 2500  | 0.2348          | 0.4187   | 0.5649   |
| 0.1599        | 2.67  | 3000  | 0.2427          | 0.4286   | 0.5606   |
| 0.1481        | 3.11  | 3500  | 0.2210          | 0.4664   | 0.5780   |
| 0.1412        | 3.56  | 4000  | 0.2542          | 0.4362   | 0.5617   |
| 0.1505        | 4.0   | 4500  | 0.2249          | 0.4728   | 0.5863   |
| 0.1425        | 4.44  | 5000  | 0.2311          | 0.4576   | 0.5845   |
| 0.1461        | 4.89  | 5500  | 0.2261          | 0.4590   | 0.5832   |
| 0.1451        | 5.33  | 6000  | 0.2248          | 0.4738   | 0.5901   |
| 0.1281        | 5.78  | 6500  | 0.2317          | 0.4641   | 0.5896   |
| 0.1354        | 6.22  | 7000  | 0.2366          | 0.4639   | 0.5946   |
| 0.1204        | 6.67  | 7500  | 0.2311          | 0.4875   | 0.5877   |
| 0.1229        | 7.11  | 8000  | 0.2083          | 0.4815   | 0.6020   |
| 0.1368        | 7.56  | 8500  | 0.2170          | 0.5213   | 0.6021   |
| 0.1288        | 8.0   | 9000  | 0.2136          | 0.5336   | 0.6176   |
| 0.1275        | 8.44  | 9500  | 0.2180          | 0.5204   | 0.6082   |
| 0.1232        | 8.89  | 10000 | 0.2147          | 0.5334   | 0.6083   |
| 0.1319        | 9.33  | 10500 | 0.2121          | 0.5312   | 0.6186   |
| 0.1267        | 9.78  | 11000 | 0.2092          | 0.5250   | 0.6190   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

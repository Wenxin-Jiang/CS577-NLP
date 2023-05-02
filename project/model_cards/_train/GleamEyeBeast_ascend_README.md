---
tags:
- generated_from_trainer
model-index:
- name: ascend
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ascend

This model is a fine-tuned version of [GleamEyeBeast/ascend](https://huggingface.co/GleamEyeBeast/ascend) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3718
- Wer: 0.6412
- Cer: 0.2428

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|
| 0.5769        | 1.0   | 688   | 1.1864          | 0.7716 | 0.3159 |
| 0.5215        | 2.0   | 1376  | 1.1613          | 0.7504 | 0.2965 |
| 0.4188        | 3.0   | 2064  | 1.1644          | 0.7389 | 0.2950 |
| 0.3695        | 4.0   | 2752  | 1.1937          | 0.7184 | 0.2815 |
| 0.3404        | 5.0   | 3440  | 1.1947          | 0.7083 | 0.2719 |
| 0.2885        | 6.0   | 4128  | 1.2314          | 0.7108 | 0.2685 |
| 0.2727        | 7.0   | 4816  | 1.2243          | 0.6850 | 0.2616 |
| 0.2417        | 8.0   | 5504  | 1.2506          | 0.6767 | 0.2608 |
| 0.2207        | 9.0   | 6192  | 1.2804          | 0.6922 | 0.2595 |
| 0.2195        | 10.0  | 6880  | 1.2582          | 0.6818 | 0.2575 |
| 0.1896        | 11.0  | 7568  | 1.3101          | 0.6814 | 0.2545 |
| 0.1961        | 12.0  | 8256  | 1.2793          | 0.6706 | 0.2526 |
| 0.1752        | 13.0  | 8944  | 1.2643          | 0.6584 | 0.2509 |
| 0.1638        | 14.0  | 9632  | 1.3152          | 0.6588 | 0.2482 |
| 0.1522        | 15.0  | 10320 | 1.3098          | 0.6433 | 0.2439 |
| 0.1351        | 16.0  | 11008 | 1.3253          | 0.6537 | 0.2447 |
| 0.1266        | 17.0  | 11696 | 1.3394          | 0.6365 | 0.2418 |
| 0.1289        | 18.0  | 12384 | 1.3718          | 0.6412 | 0.2443 |
| 0.1204        | 19.0  | 13072 | 1.3708          | 0.6433 | 0.2433 |
| 0.1189        | 20.0  | 13760 | 1.3718          | 0.6412 | 0.2428 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

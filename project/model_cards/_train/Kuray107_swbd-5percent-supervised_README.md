---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: swbd-5percent-supervised
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# swbd-5percent-supervised

This model is a fine-tuned version of [facebook/wav2vec2-large-lv60](https://huggingface.co/facebook/wav2vec2-large-lv60) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6970
- Wer: 0.1352

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 6.8534        | 0.64  | 1000  | 2.9535          | 1.0    |
| 1.8605        | 1.28  | 2000  | 0.7878          | 0.3719 |
| 0.9862        | 1.92  | 3000  | 0.5906          | 0.2684 |
| 0.8405        | 2.56  | 4000  | 0.5555          | 0.2151 |
| 0.6972        | 3.2   | 5000  | 0.5905          | 0.1992 |
| 0.6033        | 3.84  | 6000  | 0.4867          | 0.1781 |
| 0.5393        | 4.48  | 7000  | 0.5447          | 0.1805 |
| 0.529         | 5.12  | 8000  | 0.5398          | 0.1746 |
| 0.5072        | 5.77  | 9000  | 0.5093          | 0.1706 |
| 0.4331        | 6.41  | 10000 | 0.4990          | 0.1627 |
| 0.4837        | 7.05  | 11000 | 0.5319          | 0.1634 |
| 0.3867        | 7.69  | 12000 | 0.4866          | 0.1595 |
| 0.345         | 8.33  | 13000 | 0.5202          | 0.1582 |
| 0.372         | 8.97  | 14000 | 0.5396          | 0.1547 |
| 0.355         | 9.61  | 15000 | 0.5992          | 0.1493 |
| 0.3258        | 10.25 | 16000 | 0.5247          | 0.1527 |
| 0.3327        | 10.89 | 17000 | 0.5664          | 0.1512 |
| 0.3422        | 11.53 | 18000 | 0.5819          | 0.1456 |
| 0.2815        | 12.17 | 19000 | 0.5692          | 0.1453 |
| 0.2719        | 12.81 | 20000 | 0.5012          | 0.1476 |
| 0.2838        | 13.45 | 21000 | 0.5286          | 0.1454 |
| 0.2418        | 14.09 | 22000 | 0.6238          | 0.1486 |
| 0.2412        | 14.73 | 23000 | 0.5889          | 0.1456 |
| 0.2227        | 15.37 | 24000 | 0.5901          | 0.1459 |
| 0.2129        | 16.02 | 25000 | 0.5959          | 0.1454 |
| 0.2071        | 16.66 | 26000 | 0.6259          | 0.1427 |
| 0.2185        | 17.3  | 27000 | 0.6581          | 0.1437 |
| 0.1982        | 17.94 | 28000 | 0.6194          | 0.1411 |
| 0.1928        | 18.58 | 29000 | 0.5940          | 0.1409 |
| 0.1885        | 19.22 | 30000 | 0.6733          | 0.1417 |
| 0.1835        | 19.86 | 31000 | 0.6363          | 0.1393 |
| 0.1756        | 20.5  | 32000 | 0.6675          | 0.1382 |
| 0.1776        | 21.14 | 33000 | 0.6147          | 0.1407 |
| 0.1758        | 21.78 | 34000 | 0.6405          | 0.1420 |
| 0.1645        | 22.42 | 35000 | 0.6999          | 0.1401 |
| 0.1631        | 23.06 | 36000 | 0.6224          | 0.1385 |
| 0.1494        | 23.7  | 37000 | 0.6639          | 0.1374 |
| 0.1472        | 24.34 | 38000 | 0.6471          | 0.1373 |
| 0.1514        | 24.98 | 39000 | 0.6570          | 0.1395 |
| 0.1527        | 25.62 | 40000 | 0.6876          | 0.1375 |
| 0.1514        | 26.27 | 41000 | 0.6835          | 0.1376 |
| 0.1344        | 26.91 | 42000 | 0.6987          | 0.1372 |
| 0.1267        | 27.55 | 43000 | 0.7026          | 0.1362 |
| 0.1384        | 28.19 | 44000 | 0.7021          | 0.1366 |
| 0.1264        | 28.83 | 45000 | 0.7016          | 0.1355 |
| 0.1227        | 29.47 | 46000 | 0.6970          | 0.1352 |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.2
- Datasets 1.18.2
- Tokenizers 0.10.3

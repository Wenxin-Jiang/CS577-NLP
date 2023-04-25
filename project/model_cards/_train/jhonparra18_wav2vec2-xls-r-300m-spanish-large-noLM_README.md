---
license: apache-2.0
tags:
- generated_from_trainer
- "es"
- "robust-speech-event"
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-spanish-large
  results: []
 
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-spanish-large

This model is a fine-tuned version of [tomascufaro/xls-r-es-test](https://huggingface.co/tomascufaro/xls-r-es-test) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1431
- Wer: 0.1197

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 10
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 20
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 300
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.1769        | 0.15  | 400   | 0.1795          | 0.1698 |
| 0.217         | 0.3   | 800   | 0.2000          | 0.1945 |
| 0.2372        | 0.45  | 1200  | 0.1985          | 0.1859 |
| 0.2351        | 0.6   | 1600  | 0.1901          | 0.1772 |
| 0.2269        | 0.75  | 2000  | 0.1968          | 0.1783 |
| 0.2284        | 0.9   | 2400  | 0.1873          | 0.1771 |
| 0.2014        | 1.06  | 2800  | 0.1840          | 0.1696 |
| 0.1988        | 1.21  | 3200  | 0.1904          | 0.1730 |
| 0.1919        | 1.36  | 3600  | 0.1827          | 0.1630 |
| 0.1919        | 1.51  | 4000  | 0.1788          | 0.1629 |
| 0.1817        | 1.66  | 4400  | 0.1755          | 0.1558 |
| 0.1812        | 1.81  | 4800  | 0.1795          | 0.1638 |
| 0.1808        | 1.96  | 5200  | 0.1762          | 0.1603 |
| 0.1625        | 2.11  | 5600  | 0.1721          | 0.1557 |
| 0.1477        | 2.26  | 6000  | 0.1735          | 0.1504 |
| 0.1508        | 2.41  | 6400  | 0.1708          | 0.1478 |
| 0.157         | 2.56  | 6800  | 0.1644          | 0.1466 |
| 0.1491        | 2.71  | 7200  | 0.1638          | 0.1445 |
| 0.1458        | 2.86  | 7600  | 0.1582          | 0.1426 |
| 0.1387        | 3.02  | 8000  | 0.1607          | 0.1376 |
| 0.1269        | 3.17  | 8400  | 0.1559          | 0.1364 |
| 0.1172        | 3.32  | 8800  | 0.1521          | 0.1335 |
| 0.1203        | 3.47  | 9200  | 0.1534          | 0.1330 |
| 0.1177        | 3.62  | 9600  | 0.1485          | 0.1304 |
| 0.1167        | 3.77  | 10000 | 0.1498          | 0.1302 |
| 0.1194        | 3.92  | 10400 | 0.1463          | 0.1287 |
| 0.1053        | 4.07  | 10800 | 0.1483          | 0.1282 |
| 0.098         | 4.22  | 11200 | 0.1498          | 0.1267 |
| 0.0958        | 4.37  | 11600 | 0.1461          | 0.1233 |
| 0.0946        | 4.52  | 12000 | 0.1444          | 0.1218 |
| 0.094         | 4.67  | 12400 | 0.1434          | 0.1206 |
| 0.0932        | 4.82  | 12800 | 0.1424          | 0.1206 |
| 0.0912        | 4.98  | 13200 | 0.1431          | 0.1197 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-xls-r-300m-ar-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-ar-4

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7888
- Wer: 0.3697

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 60
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 4.8069        | 1.18  | 400   | 1.7793          | 0.9883 |
| 1.1949        | 2.35  | 800   | 0.9662          | 0.7908 |
| 0.8996        | 3.53  | 1200  | 0.8404          | 0.7154 |
| 0.7652        | 4.71  | 1600  | 0.7478          | 0.6379 |
| 0.6611        | 5.88  | 2000  | 0.7687          | 0.6229 |
| 0.6015        | 7.06  | 2400  | 0.7153          | 0.5948 |
| 0.5444        | 8.24  | 2800  | 0.7062          | 0.5826 |
| 0.4872        | 9.41  | 3200  | 0.6568          | 0.5414 |
| 0.4729        | 10.59 | 3600  | 0.6817          | 0.5599 |
| 0.4238        | 11.76 | 4000  | 0.6406          | 0.5262 |
| 0.4022        | 12.94 | 4400  | 0.6797          | 0.5184 |
| 0.3945        | 14.12 | 4800  | 0.6744          | 0.5147 |
| 0.3711        | 15.29 | 5200  | 0.6807          | 0.5090 |
| 0.3318        | 16.47 | 5600  | 0.6286          | 0.5011 |
| 0.3132        | 17.65 | 6000  | 0.6481          | 0.4814 |
| 0.2992        | 18.82 | 6400  | 0.6454          | 0.4958 |
| 0.2734        | 20.0  | 6800  | 0.6465          | 0.4825 |
| 0.2534        | 21.18 | 7200  | 0.6559          | 0.4658 |
| 0.2505        | 22.35 | 7600  | 0.6601          | 0.4618 |
| 0.2495        | 23.53 | 8000  | 0.7080          | 0.4813 |
| 0.2387        | 24.71 | 8400  | 0.6635          | 0.4508 |
| 0.2154        | 25.88 | 8800  | 0.6442          | 0.4538 |
| 0.2096        | 27.06 | 9200  | 0.7399          | 0.4579 |
| 0.2007        | 28.24 | 9600  | 0.6957          | 0.4512 |
| 0.1942        | 29.41 | 10000 | 0.6642          | 0.4267 |
| 0.1854        | 30.59 | 10400 | 0.6842          | 0.4393 |
| 0.1782        | 31.76 | 10800 | 0.7007          | 0.4393 |
| 0.1751        | 32.94 | 11200 | 0.7063          | 0.4321 |
| 0.1695        | 34.12 | 11600 | 0.7057          | 0.4330 |
| 0.1638        | 35.29 | 12000 | 0.7416          | 0.4266 |
| 0.1531        | 36.47 | 12400 | 0.7420          | 0.4273 |
| 0.1475        | 37.65 | 12800 | 0.7334          | 0.4218 |
| 0.1388        | 38.82 | 13200 | 0.7420          | 0.4227 |
| 0.1372        | 40.0  | 13600 | 0.7492          | 0.4238 |
| 0.1341        | 41.18 | 14000 | 0.7803          | 0.4193 |
| 0.133         | 42.35 | 14400 | 0.7396          | 0.4105 |
| 0.1238        | 43.53 | 14800 | 0.7561          | 0.4098 |
| 0.1163        | 44.71 | 15200 | 0.7987          | 0.4049 |
| 0.116         | 45.88 | 15600 | 0.7769          | 0.4093 |
| 0.1079        | 47.06 | 16000 | 0.7780          | 0.3986 |
| 0.1043        | 48.24 | 16400 | 0.7674          | 0.3905 |
| 0.1004        | 49.41 | 16800 | 0.7931          | 0.3949 |
| 0.0987        | 50.59 | 17200 | 0.7605          | 0.3938 |
| 0.0963        | 51.76 | 17600 | 0.7735          | 0.3858 |
| 0.0905        | 52.94 | 18000 | 0.7504          | 0.3802 |
| 0.086         | 54.12 | 18400 | 0.8038          | 0.3867 |
| 0.0839        | 55.29 | 18800 | 0.7887          | 0.3797 |
| 0.0798        | 56.47 | 19200 | 0.7832          | 0.3705 |
| 0.0785        | 57.65 | 19600 | 0.7771          | 0.3706 |
| 0.0765        | 58.82 | 20000 | 0.7858          | 0.3703 |
| 0.0739        | 60.0  | 20400 | 0.7888          | 0.3697 |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.11.0
- Datasets 1.18.3
- Tokenizers 0.10.3

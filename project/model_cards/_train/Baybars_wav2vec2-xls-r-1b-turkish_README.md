---
language:
- tr
tags:
- automatic-speech-recognition
- common_voice
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: ''
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [./checkpoint-10500](https://huggingface.co/./checkpoint-10500) on the COMMON_VOICE - TR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7540
- Wer: 0.4647
- Cer: 0.1318

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.999,0.9999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 120.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Cer    | Validation Loss | Wer    |
|:-------------:|:------:|:-----:|:------:|:---------------:|:------:|
| 1.0779        | 4.59   | 500   | 0.2354 | 0.8260          | 0.7395 |
| 0.7573        | 9.17   | 1000  | 0.2100 | 0.7544          | 0.6960 |
| 0.8225        | 13.76  | 1500  | 0.2021 | 0.6867          | 0.6672 |
| 0.621         | 18.35  | 2000  | 0.1874 | 0.6824          | 0.6209 |
| 0.6362        | 22.94  | 2500  | 0.1904 | 0.6712          | 0.6286 |
| 0.624         | 27.52  | 3000  | 0.1820 | 0.6940          | 0.6116 |
| 0.4781        | 32.11  | 3500  | 0.1735 | 0.6966          | 0.5989 |
| 0.5685        | 36.7   | 4000  | 0.1769 | 0.6742          | 0.5971 |
| 0.4384        | 41.28  | 4500  | 0.1767 | 0.6904          | 0.5999 |
| 0.5509        | 45.87  | 5000  | 0.1692 | 0.6734          | 0.5641 |
| 0.3665        | 50.46  | 5500  | 0.1680 | 0.7018          | 0.5662 |
| 0.3914        | 55.05  | 6000  | 0.1631 | 0.7121          | 0.5552 |
| 0.2467        | 59.63  | 6500  | 0.1563 | 0.6657          | 0.5374 |
| 0.2576        | 64.22  | 7000  | 0.1554 | 0.6920          | 0.5316 |
| 0.2711        | 68.81  | 7500  | 0.1495 | 0.6900          | 0.5176 |
| 0.2626        | 73.39  | 8000  | 0.1454 | 0.6843          | 0.5043 |
| 0.1377        | 77.98  | 8500  | 0.1470 | 0.7383          | 0.5101 |
| 0.2005        | 82.57  | 9000  | 0.1430 | 0.7228          | 0.5045 |
| 0.1355        | 87.16  | 9500  | 0.1375 | 0.7231          | 0.4869 |
| 0.0431        | 91.74  | 10000 | 0.1350 | 0.7397          | 0.4749 |
| 0.0586        | 96.33  | 10500 | 0.1339 | 0.7360          | 0.4754 |
| 0.0896        | 100.92 | 11000 | 0.7187 | 0.4885          | 0.1398 |
| 0.183         | 105.5  | 11500 | 0.7310 | 0.4838          | 0.1392 |
| 0.0963        | 110.09 | 12000 | 0.7643 | 0.4759          | 0.1362 |
| 0.0437        | 114.68 | 12500 | 0.7525 | 0.4641          | 0.1328 |
| 0.1122        | 119.27 | 13000 | 0.7535 | 0.4651          | 0.1317 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0

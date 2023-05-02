---
language:
- ar
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
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

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - AR dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1373
- Wer: 0.8607

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6.5e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 30.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 2.2416        | 0.84  | 500   | 1.2867          | 0.8875 |
| 2.3089        | 1.67  | 1000  | 1.8336          | 0.9548 |
| 2.3614        | 2.51  | 1500  | 1.5937          | 0.9469 |
| 2.5234        | 3.35  | 2000  | 1.9765          | 0.9867 |
| 2.5373        | 4.19  | 2500  | 1.9062          | 0.9916 |
| 2.5703        | 5.03  | 3000  | 1.9772          | 0.9915 |
| 2.4656        | 5.86  | 3500  | 1.8083          | 0.9829 |
| 2.4339        | 6.7   | 4000  | 1.7548          | 0.9752 |
| 2.344         | 7.54  | 4500  | 1.6146          | 0.9638 |
| 2.2677        | 8.38  | 5000  | 1.5105          | 0.9499 |
| 2.2074        | 9.21  | 5500  | 1.4191          | 0.9357 |
| 2.3768        | 10.05 | 6000  | 1.6663          | 0.9665 |
| 2.3804        | 10.89 | 6500  | 1.6571          | 0.9720 |
| 2.3237        | 11.72 | 7000  | 1.6049          | 0.9637 |
| 2.317         | 12.56 | 7500  | 1.5875          | 0.9655 |
| 2.2988        | 13.4  | 8000  | 1.5357          | 0.9603 |
| 2.2906        | 14.24 | 8500  | 1.5637          | 0.9592 |
| 2.2848        | 15.08 | 9000  | 1.5326          | 0.9537 |
| 2.2381        | 15.91 | 9500  | 1.5631          | 0.9508 |
| 2.2072        | 16.75 | 10000 | 1.4565          | 0.9395 |
| 2.197         | 17.59 | 10500 | 1.4304          | 0.9406 |
| 2.198         | 18.43 | 11000 | 1.4230          | 0.9382 |
| 2.1668        | 19.26 | 11500 | 1.3998          | 0.9315 |
| 2.1498        | 20.1  | 12000 | 1.3920          | 0.9258 |
| 2.1244        | 20.94 | 12500 | 1.3584          | 0.9153 |
| 2.0953        | 21.78 | 13000 | 1.3274          | 0.9054 |
| 2.0762        | 22.61 | 13500 | 1.2933          | 0.9073 |
| 2.0587        | 23.45 | 14000 | 1.2516          | 0.8944 |
| 2.0363        | 24.29 | 14500 | 1.2214          | 0.8902 |
| 2.0302        | 25.13 | 15000 | 1.2087          | 0.8871 |
| 2.0071        | 25.96 | 15500 | 1.1953          | 0.8786 |
| 1.9882        | 26.8  | 16000 | 1.1738          | 0.8712 |
| 1.9772        | 27.64 | 16500 | 1.1647          | 0.8672 |
| 1.9585        | 28.48 | 17000 | 1.1459          | 0.8635 |
| 1.944         | 29.31 | 17500 | 1.1414          | 0.8616 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0

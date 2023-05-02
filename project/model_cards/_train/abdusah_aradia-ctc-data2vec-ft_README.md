---
tags:
- automatic-speech-recognition
- abdusahmbzuai/arabic_speech_massive_300hrs
- generated_from_trainer
model-index:
- name: aradia-ctc-data2vec-ft
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# aradia-ctc-data2vec-ft

This model is a fine-tuned version of [/l/users/abdulwahab.sahyoun/aradia/aradia-ctc-data2vec-ft](https://huggingface.co//l/users/abdulwahab.sahyoun/aradia/aradia-ctc-data2vec-ft) on the ABDUSAHMBZUAI/ARABIC_SPEECH_MASSIVE_300HRS - NA dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0464
- Wer: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer |
|:-------------:|:-----:|:----:|:---------------:|:---:|
| No log        | 0.43  | 100  | 3.3600          | 1.0 |
| No log        | 0.87  | 200  | 3.0887          | 1.0 |
| No log        | 1.3   | 300  | 3.0779          | 1.0 |
| No log        | 1.74  | 400  | 3.0551          | 1.0 |
| 4.8553        | 2.17  | 500  | 3.0526          | 1.0 |
| 4.8553        | 2.61  | 600  | 3.0560          | 1.0 |
| 4.8553        | 3.04  | 700  | 3.1251          | 1.0 |
| 4.8553        | 3.48  | 800  | 3.0870          | 1.0 |
| 4.8553        | 3.91  | 900  | 3.0822          | 1.0 |
| 3.1133        | 4.35  | 1000 | 3.0484          | 1.0 |
| 3.1133        | 4.78  | 1100 | 3.0558          | 1.0 |
| 3.1133        | 5.22  | 1200 | 3.1019          | 1.0 |
| 3.1133        | 5.65  | 1300 | 3.0914          | 1.0 |
| 3.1133        | 6.09  | 1400 | 3.0691          | 1.0 |
| 3.109         | 6.52  | 1500 | 3.0589          | 1.0 |
| 3.109         | 6.95  | 1600 | 3.0508          | 1.0 |
| 3.109         | 7.39  | 1700 | 3.0540          | 1.0 |
| 3.109         | 7.82  | 1800 | 3.0546          | 1.0 |
| 3.109         | 8.26  | 1900 | 3.0524          | 1.0 |
| 3.1106        | 8.69  | 2000 | 3.0569          | 1.0 |
| 3.1106        | 9.13  | 2100 | 3.0622          | 1.0 |
| 3.1106        | 9.56  | 2200 | 3.0518          | 1.0 |
| 3.1106        | 10.0  | 2300 | 3.0749          | 1.0 |
| 3.1106        | 10.43 | 2400 | 3.0698          | 1.0 |
| 3.1058        | 10.87 | 2500 | 3.0665          | 1.0 |
| 3.1058        | 11.3  | 2600 | 3.0555          | 1.0 |
| 3.1058        | 11.74 | 2700 | 3.0589          | 1.0 |
| 3.1058        | 12.17 | 2800 | 3.0611          | 1.0 |
| 3.1058        | 12.61 | 2900 | 3.0561          | 1.0 |
| 3.1071        | 13.04 | 3000 | 3.0480          | 1.0 |
| 3.1071        | 13.48 | 3100 | 3.0492          | 1.0 |
| 3.1071        | 13.91 | 3200 | 3.0574          | 1.0 |
| 3.1071        | 14.35 | 3300 | 3.0538          | 1.0 |
| 3.1071        | 14.78 | 3400 | 3.0505          | 1.0 |
| 3.1061        | 15.22 | 3500 | 3.0600          | 1.0 |
| 3.1061        | 15.65 | 3600 | 3.0596          | 1.0 |
| 3.1061        | 16.09 | 3700 | 3.0623          | 1.0 |
| 3.1061        | 16.52 | 3800 | 3.0800          | 1.0 |
| 3.1061        | 16.95 | 3900 | 3.0583          | 1.0 |
| 3.1036        | 17.39 | 4000 | 3.0534          | 1.0 |
| 3.1036        | 17.82 | 4100 | 3.0563          | 1.0 |
| 3.1036        | 18.26 | 4200 | 3.0481          | 1.0 |
| 3.1036        | 18.69 | 4300 | 3.0477          | 1.0 |
| 3.1036        | 19.13 | 4400 | 3.0505          | 1.0 |
| 3.1086        | 19.56 | 4500 | 3.0485          | 1.0 |
| 3.1086        | 20.0  | 4600 | 3.0481          | 1.0 |
| 3.1086        | 20.43 | 4700 | 3.0615          | 1.0 |
| 3.1086        | 20.87 | 4800 | 3.0658          | 1.0 |
| 3.1086        | 21.3  | 4900 | 3.0505          | 1.0 |
| 3.1028        | 21.74 | 5000 | 3.0492          | 1.0 |
| 3.1028        | 22.17 | 5100 | 3.0485          | 1.0 |
| 3.1028        | 22.61 | 5200 | 3.0483          | 1.0 |
| 3.1028        | 23.04 | 5300 | 3.0479          | 1.0 |
| 3.1028        | 23.48 | 5400 | 3.0509          | 1.0 |
| 3.1087        | 23.91 | 5500 | 3.0530          | 1.0 |
| 3.1087        | 24.35 | 5600 | 3.0486          | 1.0 |
| 3.1087        | 24.78 | 5700 | 3.0514          | 1.0 |
| 3.1087        | 25.22 | 5800 | 3.0505          | 1.0 |
| 3.1087        | 25.65 | 5900 | 3.0508          | 1.0 |
| 3.1043        | 26.09 | 6000 | 3.0501          | 1.0 |
| 3.1043        | 26.52 | 6100 | 3.0467          | 1.0 |
| 3.1043        | 26.95 | 6200 | 3.0466          | 1.0 |
| 3.1043        | 27.39 | 6300 | 3.0465          | 1.0 |
| 3.1043        | 27.82 | 6400 | 3.0465          | 1.0 |
| 3.1175        | 28.26 | 6500 | 3.0466          | 1.0 |
| 3.1175        | 28.69 | 6600 | 3.0466          | 1.0 |
| 3.1175        | 29.13 | 6700 | 3.0465          | 1.0 |
| 3.1175        | 29.56 | 6800 | 3.0465          | 1.0 |
| 3.1175        | 30.0  | 6900 | 3.0464          | 1.0 |


### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4
- Tokenizers 0.11.6

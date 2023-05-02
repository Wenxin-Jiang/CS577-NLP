---
tags:
- automatic-speech-recognition
- abdusahmbzuai/arabic_speech_massive_300hrs
- generated_from_trainer
model-index:
- name: aradia-ctc-hubert-ft
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# aradia-ctc-hubert-ft

This model is a fine-tuned version of [/l/users/abdulwahab.sahyoun/aradia/aradia-ctc-hubert-ft](https://huggingface.co//l/users/abdulwahab.sahyoun/aradia/aradia-ctc-hubert-ft) on the ABDUSAHMBZUAI/ARABIC_SPEECH_MASSIVE_300HRS - NA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8536
- Wer: 0.3737

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

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 0.43  | 100  | 3.6934          | 1.0    |
| No log        | 0.87  | 200  | 3.0763          | 1.0    |
| No log        | 1.3   | 300  | 2.9737          | 1.0    |
| No log        | 1.74  | 400  | 2.5734          | 1.0    |
| 5.0957        | 2.17  | 500  | 1.1900          | 0.9011 |
| 5.0957        | 2.61  | 600  | 0.9726          | 0.7572 |
| 5.0957        | 3.04  | 700  | 0.8960          | 0.6209 |
| 5.0957        | 3.48  | 800  | 0.7851          | 0.5515 |
| 5.0957        | 3.91  | 900  | 0.7271          | 0.5115 |
| 1.0312        | 4.35  | 1000 | 0.7053          | 0.4955 |
| 1.0312        | 4.78  | 1100 | 0.6823          | 0.4737 |
| 1.0312        | 5.22  | 1200 | 0.6768          | 0.4595 |
| 1.0312        | 5.65  | 1300 | 0.6635          | 0.4488 |
| 1.0312        | 6.09  | 1400 | 0.6602          | 0.4390 |
| 0.6815        | 6.52  | 1500 | 0.6464          | 0.4310 |
| 0.6815        | 6.95  | 1600 | 0.6455          | 0.4394 |
| 0.6815        | 7.39  | 1700 | 0.6630          | 0.4312 |
| 0.6815        | 7.82  | 1800 | 0.6521          | 0.4126 |
| 0.6815        | 8.26  | 1900 | 0.6282          | 0.4284 |
| 0.544         | 8.69  | 2000 | 0.6248          | 0.4178 |
| 0.544         | 9.13  | 2100 | 0.6510          | 0.4104 |
| 0.544         | 9.56  | 2200 | 0.6527          | 0.4013 |
| 0.544         | 10.0  | 2300 | 0.6511          | 0.4064 |
| 0.544         | 10.43 | 2400 | 0.6734          | 0.4061 |
| 0.4478        | 10.87 | 2500 | 0.6756          | 0.4145 |
| 0.4478        | 11.3  | 2600 | 0.6727          | 0.3990 |
| 0.4478        | 11.74 | 2700 | 0.6619          | 0.4007 |
| 0.4478        | 12.17 | 2800 | 0.6614          | 0.4019 |
| 0.4478        | 12.61 | 2900 | 0.6695          | 0.4004 |
| 0.3919        | 13.04 | 3000 | 0.6778          | 0.3966 |
| 0.3919        | 13.48 | 3100 | 0.6872          | 0.3971 |
| 0.3919        | 13.91 | 3200 | 0.6882          | 0.3945 |
| 0.3919        | 14.35 | 3300 | 0.7177          | 0.4010 |
| 0.3919        | 14.78 | 3400 | 0.6888          | 0.4043 |
| 0.3767        | 15.22 | 3500 | 0.7124          | 0.4202 |
| 0.3767        | 15.65 | 3600 | 0.7276          | 0.4120 |
| 0.3767        | 16.09 | 3700 | 0.7265          | 0.4034 |
| 0.3767        | 16.52 | 3800 | 0.7392          | 0.4077 |
| 0.3767        | 16.95 | 3900 | 0.7403          | 0.3965 |
| 0.3603        | 17.39 | 4000 | 0.7445          | 0.4016 |
| 0.3603        | 17.82 | 4100 | 0.7579          | 0.4012 |
| 0.3603        | 18.26 | 4200 | 0.7225          | 0.3963 |
| 0.3603        | 18.69 | 4300 | 0.7355          | 0.3951 |
| 0.3603        | 19.13 | 4400 | 0.7482          | 0.3925 |
| 0.3153        | 19.56 | 4500 | 0.7723          | 0.3972 |
| 0.3153        | 20.0  | 4600 | 0.7469          | 0.3898 |
| 0.3153        | 20.43 | 4700 | 0.7800          | 0.3944 |
| 0.3153        | 20.87 | 4800 | 0.7827          | 0.3897 |
| 0.3153        | 21.3  | 4900 | 0.7935          | 0.3914 |
| 0.286         | 21.74 | 5000 | 0.7984          | 0.3750 |
| 0.286         | 22.17 | 5100 | 0.7945          | 0.3830 |
| 0.286         | 22.61 | 5200 | 0.8011          | 0.3775 |
| 0.286         | 23.04 | 5300 | 0.7978          | 0.3824 |
| 0.286         | 23.48 | 5400 | 0.8161          | 0.3833 |
| 0.2615        | 23.91 | 5500 | 0.7823          | 0.3858 |
| 0.2615        | 24.35 | 5600 | 0.8312          | 0.3863 |
| 0.2615        | 24.78 | 5700 | 0.8427          | 0.3819 |
| 0.2615        | 25.22 | 5800 | 0.8432          | 0.3802 |
| 0.2615        | 25.65 | 5900 | 0.8286          | 0.3794 |
| 0.2408        | 26.09 | 6000 | 0.8224          | 0.3824 |
| 0.2408        | 26.52 | 6100 | 0.8228          | 0.3823 |
| 0.2408        | 26.95 | 6200 | 0.8324          | 0.3795 |
| 0.2408        | 27.39 | 6300 | 0.8564          | 0.3744 |
| 0.2408        | 27.82 | 6400 | 0.8629          | 0.3774 |
| 0.2254        | 28.26 | 6500 | 0.8545          | 0.3778 |
| 0.2254        | 28.69 | 6600 | 0.8492          | 0.3767 |
| 0.2254        | 29.13 | 6700 | 0.8511          | 0.3751 |
| 0.2254        | 29.56 | 6800 | 0.8491          | 0.3753 |
| 0.2254        | 30.0  | 6900 | 0.8536          | 0.3737 |


### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4
- Tokenizers 0.11.6

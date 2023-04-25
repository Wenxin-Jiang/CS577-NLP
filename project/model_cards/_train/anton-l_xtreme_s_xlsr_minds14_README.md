---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: xtreme_s_xlsr_minds14
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xtreme_s_xlsr_minds14

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2566
- F1: {'f1': 0.9460569664921582, 'accuracy': 0.9468540012217471}

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
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- total_train_batch_size: 64
- total_eval_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1                                                          |
|:-------------:|:-----:|:----:|:---------------:|:-----------------------------------------------------------:|
| 2.551         | 2.7   | 200  | 2.5921          | {'f1': 0.03454307545755678, 'accuracy': 0.1148442272449603} |
| 1.6934        | 5.41  | 400  | 1.5353          | {'f1': 0.5831241711045994, 'accuracy': 0.6053756872327428}  |
| 0.5914        | 8.11  | 600  | 0.7337          | {'f1': 0.7990425247664236, 'accuracy': 0.7947464874770922}  |
| 0.3896        | 10.81 | 800  | 0.5076          | {'f1': 0.8738199236080776, 'accuracy': 0.872327428222358}   |
| 0.5052        | 13.51 | 1000 | 0.4917          | {'f1': 0.8744760456867134, 'accuracy': 0.8747709224190593}  |
| 0.4806        | 16.22 | 1200 | 0.4751          | {'f1': 0.8840798740258787, 'accuracy': 0.8845448992058644}  |
| 0.2103        | 18.92 | 1400 | 0.5228          | {'f1': 0.8721632556623751, 'accuracy': 0.8729383017715333}  |
| 0.4198        | 21.62 | 1600 | 0.5910          | {'f1': 0.8755207264572983, 'accuracy': 0.8766035430665852}  |
| 0.11          | 24.32 | 1800 | 0.4464          | {'f1': 0.896423086249818, 'accuracy': 0.8955406230910201}   |
| 0.1233        | 27.03 | 2000 | 0.3760          | {'f1': 0.9012283567348968, 'accuracy': 0.9016493585827734}  |
| 0.1827        | 29.73 | 2200 | 0.4178          | {'f1': 0.9042381720184095, 'accuracy': 0.9059254734270006}  |
| 0.1235        | 32.43 | 2400 | 0.4152          | {'f1': 0.9063257163259107, 'accuracy': 0.9071472205253512}  |
| 0.1873        | 35.14 | 2600 | 0.2903          | {'f1': 0.9369340598806323, 'accuracy': 0.9376908979841173}  |
| 0.017         | 37.84 | 2800 | 0.3046          | {'f1': 0.9300781160576355, 'accuracy': 0.9303604153940135}  |
| 0.0436        | 40.54 | 3000 | 0.3111          | {'f1': 0.9315034391389341, 'accuracy': 0.9321930360415394}  |
| 0.0455        | 43.24 | 3200 | 0.2748          | {'f1': 0.9417365311433034, 'accuracy': 0.9425778863775198}  |
| 0.046         | 45.95 | 3400 | 0.2800          | {'f1': 0.9390712658440112, 'accuracy': 0.9395235186316433}  |
| 0.0042        | 48.65 | 3600 | 0.2566          | {'f1': 0.9460569664921582, 'accuracy': 0.9468540012217471}  |


### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4.dev0
- Tokenizers 0.11.6

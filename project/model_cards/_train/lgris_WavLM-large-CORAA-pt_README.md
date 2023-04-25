---
language:
- pt
license: apache-2.0
tags:
- generated_from_trainer
- pt
model-index:
- name: WavLM-large-CORAA-pt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# WavLM-large-CORAA-pt

This model is a fine-tuned version of [microsoft/wavlm-large](https://huggingface.co/microsoft/wavlm-large) on [CORAA dataset](https://github.com/nilc-nlp/CORAA).
It achieves the following results on the evaluation set:
- Loss: 0.6144
- Wer: 0.3840

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
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- training_steps: 40000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| No log        | 0.04  | 1000  | 1.9230          | 0.9960 |
| 5.153         | 0.08  | 2000  | 1.3733          | 0.8444 |
| 5.153         | 0.13  | 3000  | 1.1992          | 0.7362 |
| 1.367         | 0.17  | 4000  | 1.1289          | 0.6957 |
| 1.367         | 0.21  | 5000  | 1.0357          | 0.6470 |
| 1.1824        | 0.25  | 6000  | 1.0216          | 0.6201 |
| 1.1824        | 0.29  | 7000  | 0.9338          | 0.6036 |
| 1.097         | 0.33  | 8000  | 0.9149          | 0.5760 |
| 1.097         | 0.38  | 9000  | 0.8885          | 0.5541 |
| 1.0254        | 0.42  | 10000 | 0.8678          | 0.5366 |
| 1.0254        | 0.46  | 11000 | 0.8349          | 0.5323 |
| 0.9782        | 0.5   | 12000 | 0.8230          | 0.5155 |
| 0.9782        | 0.54  | 13000 | 0.8245          | 0.5049 |
| 0.9448        | 0.59  | 14000 | 0.7802          | 0.4990 |
| 0.9448        | 0.63  | 15000 | 0.7650          | 0.4900 |
| 0.9092        | 0.67  | 16000 | 0.7665          | 0.4796 |
| 0.9092        | 0.71  | 17000 | 0.7568          | 0.4795 |
| 0.8764        | 0.75  | 18000 | 0.7403          | 0.4615 |
| 0.8764        | 0.8   | 19000 | 0.7219          | 0.4644 |
| 0.8498        | 0.84  | 20000 | 0.7180          | 0.4502 |
| 0.8498        | 0.88  | 21000 | 0.7017          | 0.4436 |
| 0.8278        | 0.92  | 22000 | 0.6992          | 0.4395 |
| 0.8278        | 0.96  | 23000 | 0.7021          | 0.4329 |
| 0.8077        | 1.0   | 24000 | 0.6892          | 0.4265 |
| 0.8077        | 1.05  | 25000 | 0.6940          | 0.4248 |
| 0.7486        | 1.09  | 26000 | 0.6767          | 0.4202 |
| 0.7486        | 1.13  | 27000 | 0.6734          | 0.4150 |
| 0.7459        | 1.17  | 28000 | 0.6650          | 0.4152 |
| 0.7459        | 1.21  | 29000 | 0.6559          | 0.4078 |
| 0.7304        | 1.26  | 30000 | 0.6536          | 0.4088 |
| 0.7304        | 1.3   | 31000 | 0.6537          | 0.4025 |
| 0.7183        | 1.34  | 32000 | 0.6462          | 0.4008 |
| 0.7183        | 1.38  | 33000 | 0.6381          | 0.3973 |
| 0.7059        | 1.42  | 34000 | 0.6266          | 0.3930 |
| 0.7059        | 1.46  | 35000 | 0.6280          | 0.3921 |
| 0.6983        | 1.51  | 36000 | 0.6248          | 0.3897 |
| 0.6983        | 1.55  | 37000 | 0.6275          | 0.3872 |
| 0.6892        | 1.59  | 38000 | 0.6199          | 0.3852 |
| 0.6892        | 1.63  | 39000 | 0.6180          | 0.3842 |
| 0.691         | 1.67  | 40000 | 0.6144          | 0.3840 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0

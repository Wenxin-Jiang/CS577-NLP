---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-53-Total_2e-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-53-Total_2e-4

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2082
- Wer: 0.4355

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 5.0972        | 0.1   | 200   | 2.9261          | 0.9696 |
| 2.2492        | 0.2   | 400   | 1.4255          | 0.7957 |
| 0.9206        | 0.3   | 600   | 1.1854          | 0.6903 |
| 0.8152        | 0.4   | 800   | 1.2227          | 0.6072 |
| 0.7284        | 0.5   | 1000  | 1.2009          | 0.5694 |
| 0.6503        | 0.6   | 1200  | 1.2563          | 0.5603 |
| 0.643         | 0.7   | 1400  | 1.1556          | 0.5404 |
| 0.6692        | 0.8   | 1600  | 1.2245          | 0.5176 |
| 0.5939        | 0.9   | 1800  | 1.1662          | 0.5116 |
| 0.577         | 1.0   | 2000  | 1.1099          | 0.5128 |
| 0.5118        | 1.1   | 2200  | 1.3127          | 0.4911 |
| 0.5389        | 1.2   | 2400  | 1.0365          | 0.4958 |
| 0.5452        | 1.3   | 2600  | 1.0924          | 0.4840 |
| 0.5072        | 1.4   | 2800  | 1.2285          | 0.4787 |
| 0.514         | 1.5   | 3000  | 1.0627          | 0.4802 |
| 0.5275        | 1.6   | 3200  | 1.0770          | 0.4702 |
| 0.5064        | 1.7   | 3400  | 1.1287          | 0.4709 |
| 0.4837        | 1.8   | 3600  | 1.1389          | 0.4694 |
| 0.4939        | 1.9   | 3800  | 1.0724          | 0.4635 |
| 0.5104        | 2.0   | 4000  | 1.2553          | 0.4604 |
| 0.4439        | 2.1   | 4200  | 1.2482          | 0.4570 |
| 0.4546        | 2.2   | 4400  | 1.2378          | 0.4732 |
| 0.4294        | 2.3   | 4600  | 1.1122          | 0.4519 |
| 0.4533        | 2.4   | 4800  | 1.1338          | 0.4508 |
| 0.4526        | 2.5   | 5000  | 1.2038          | 0.4540 |
| 0.4642        | 2.6   | 5200  | 1.2188          | 0.4635 |
| 0.4403        | 2.7   | 5400  | 1.2394          | 0.4512 |
| 0.4485        | 2.8   | 5600  | 1.0510          | 0.4577 |
| 0.4614        | 2.9   | 5800  | 1.1459          | 0.4451 |
| 0.4233        | 3.0   | 6000  | 1.1758          | 0.4397 |
| 0.4013        | 3.1   | 6200  | 1.0858          | 0.4456 |
| 0.4166        | 3.2   | 6400  | 1.2246          | 0.4420 |
| 0.3998        | 3.3   | 6600  | 1.1516          | 0.4465 |
| 0.4106        | 3.4   | 6800  | 1.2585          | 0.4394 |
| 0.4031        | 3.5   | 7000  | 1.2514          | 0.4419 |
| 0.3858        | 3.6   | 7200  | 1.2545          | 0.4447 |
| 0.393         | 3.7   | 7400  | 1.0103          | 0.4387 |
| 0.3819        | 3.8   | 7600  | 1.1280          | 0.4355 |
| 0.3957        | 3.9   | 7800  | 1.1960          | 0.4476 |
| 0.392         | 4.0   | 8000  | 1.1318          | 0.4461 |
| 0.355         | 4.1   | 8200  | 1.1822          | 0.4387 |
| 0.3377        | 4.2   | 8400  | 1.2258          | 0.4403 |
| 0.353         | 4.3   | 8600  | 1.2232          | 0.4350 |
| 0.3595        | 4.4   | 8800  | 1.1642          | 0.4329 |
| 0.3762        | 4.5   | 9000  | 1.1507          | 0.4365 |
| 0.3455        | 4.6   | 9200  | 1.2259          | 0.4337 |
| 0.3398        | 4.7   | 9400  | 1.2888          | 0.4350 |
| 0.3624        | 4.8   | 9600  | 1.2015          | 0.4364 |
| 0.3392        | 4.9   | 9800  | 1.2045          | 0.4350 |
| 0.339         | 5.0   | 10000 | 1.2082          | 0.4355 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3

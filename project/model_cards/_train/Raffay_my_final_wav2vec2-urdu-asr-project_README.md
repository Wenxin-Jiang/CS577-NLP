---
tags:
- generated_from_trainer
model-index:
- name: my_final_wav2vec2-urdu-asr-project
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_final_wav2vec2-urdu-asr-project

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 5.4680
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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 400
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer |
|:-------------:|:-----:|:----:|:---------------:|:---:|
| 7.8981        | 1.41  | 200  | 5.5809          | 1.0 |
| 5.254         | 2.82  | 400  | 5.4720          | 1.0 |
| 5.2209        | 4.23  | 600  | 5.4862          | 1.0 |
| 5.256         | 5.63  | 800  | 5.4716          | 1.0 |
| 5.1244        | 7.04  | 1000 | 5.4912          | 1.0 |
| 5.0641        | 8.45  | 1200 | 5.4797          | 1.0 |
| 5.0923        | 9.86  | 1400 | 5.5290          | 1.0 |
| 5.0166        | 11.27 | 1600 | 5.4722          | 1.0 |
| 5.1251        | 12.68 | 1800 | 5.4690          | 1.0 |
| 5.0201        | 14.08 | 2000 | 5.4684          | 1.0 |
| 5.1285        | 15.49 | 2200 | 5.4745          | 1.0 |
| 5.0853        | 16.9  | 2400 | 5.4734          | 1.0 |
| 5.0112        | 18.31 | 2600 | 5.4668          | 1.0 |
| 5.0372        | 19.72 | 2800 | 5.4680          | 1.0 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xls-r-300m-gl-jupyter4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-gl-jupyter4

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0970
- Wer: 0.0636

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 45
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.492         | 3.36  | 400  | 0.3109          | 0.3158 |
| 0.194         | 6.72  | 800  | 0.1279          | 0.1454 |
| 0.0794        | 10.08 | 1200 | 0.1210          | 0.1240 |
| 0.0565        | 13.44 | 1600 | 0.1209          | 0.1150 |
| 0.041         | 16.8  | 2000 | 0.1186          | 0.1107 |
| 0.0343        | 20.17 | 2400 | 0.1143          | 0.0933 |
| 0.0283        | 23.53 | 2800 | 0.1067          | 0.0900 |
| 0.0231        | 26.89 | 3200 | 0.1076          | 0.0812 |
| 0.0176        | 30.25 | 3600 | 0.1094          | 0.0780 |
| 0.0169        | 33.61 | 4000 | 0.1041          | 0.0766 |
| 0.0138        | 36.97 | 4400 | 0.1012          | 0.0711 |
| 0.0109        | 40.33 | 4800 | 0.0985          | 0.0655 |
| 0.0099        | 43.69 | 5200 | 0.0970          | 0.0636 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.1+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3

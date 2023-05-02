---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xls-r-300m-gl-jupyter9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-gl-jupyter9

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0970
- Wer: 0.0624

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
- num_epochs: 60
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.6977        | 3.36  | 400  | 0.4273          | 0.4574 |
| 0.2282        | 6.72  | 800  | 0.1492          | 0.1723 |
| 0.0884        | 10.08 | 1200 | 0.1344          | 0.1336 |
| 0.0594        | 13.44 | 1600 | 0.1329          | 0.1238 |
| 0.0437        | 16.8  | 2000 | 0.1137          | 0.1153 |
| 0.0384        | 20.17 | 2400 | 0.1197          | 0.1033 |
| 0.0332        | 23.53 | 2800 | 0.1147          | 0.0980 |
| 0.0282        | 26.89 | 3200 | 0.1079          | 0.0917 |
| 0.0236        | 30.25 | 3600 | 0.1144          | 0.0922 |
| 0.0237        | 33.61 | 4000 | 0.1130          | 0.0880 |
| 0.019         | 36.97 | 4400 | 0.1035          | 0.0818 |
| 0.0164        | 40.33 | 4800 | 0.1045          | 0.0813 |
| 0.0146        | 43.69 | 5200 | 0.1037          | 0.0735 |
| 0.0111        | 47.06 | 5600 | 0.1085          | 0.0701 |
| 0.0093        | 50.42 | 6000 | 0.1039          | 0.0659 |
| 0.0084        | 53.78 | 6400 | 0.0970          | 0.0636 |
| 0.0073        | 57.14 | 6800 | 0.0970          | 0.0624 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.1+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3

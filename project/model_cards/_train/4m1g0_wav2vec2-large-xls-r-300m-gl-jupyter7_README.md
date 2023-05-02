---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xls-r-300m-gl-jupyter7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-gl-jupyter7

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1004
- Wer: 0.0647

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
| 3.8074        | 3.36  | 400  | 0.4882          | 0.5245 |
| 0.2396        | 6.72  | 800  | 0.1335          | 0.1524 |
| 0.0876        | 10.08 | 1200 | 0.1216          | 0.1199 |
| 0.0597        | 13.44 | 1600 | 0.1289          | 0.1241 |
| 0.0449        | 16.8  | 2000 | 0.1164          | 0.1028 |
| 0.0372        | 20.17 | 2400 | 0.1270          | 0.1023 |
| 0.0319        | 23.53 | 2800 | 0.1111          | 0.0966 |
| 0.0286        | 26.89 | 3200 | 0.1142          | 0.0925 |
| 0.0246        | 30.25 | 3600 | 0.1142          | 0.0926 |
| 0.0235        | 33.61 | 4000 | 0.1075          | 0.0836 |
| 0.0181        | 36.97 | 4400 | 0.1083          | 0.0837 |
| 0.0151        | 40.33 | 4800 | 0.1140          | 0.0768 |
| 0.014         | 43.69 | 5200 | 0.1015          | 0.0748 |
| 0.0111        | 47.06 | 5600 | 0.1023          | 0.0702 |
| 0.0093        | 50.42 | 6000 | 0.1028          | 0.0708 |
| 0.0078        | 53.78 | 6400 | 0.0999          | 0.0645 |
| 0.0071        | 57.14 | 6800 | 0.1004          | 0.0647 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.1+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3

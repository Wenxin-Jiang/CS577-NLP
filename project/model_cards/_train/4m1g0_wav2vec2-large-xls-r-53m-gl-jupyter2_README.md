---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xls-r-53m-gl-jupyter2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-53m-gl-jupyter2

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0941
- Wer: 0.0615

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
| 3.7298        | 3.36  | 400  | 0.2477          | 0.2493 |
| 0.1507        | 6.72  | 800  | 0.1294          | 0.1264 |
| 0.066         | 10.08 | 1200 | 0.1235          | 0.1161 |
| 0.0456        | 13.44 | 1600 | 0.1011          | 0.1001 |
| 0.0347        | 16.8  | 2000 | 0.1033          | 0.0909 |
| 0.0284        | 20.17 | 2400 | 0.1083          | 0.0861 |
| 0.0221        | 23.53 | 2800 | 0.1010          | 0.0761 |
| 0.0199        | 26.89 | 3200 | 0.0911          | 0.0754 |
| 0.0155        | 30.25 | 3600 | 0.1026          | 0.0743 |
| 0.0142        | 33.61 | 4000 | 0.1024          | 0.0719 |
| 0.0125        | 36.97 | 4400 | 0.0977          | 0.0676 |
| 0.0104        | 40.33 | 4800 | 0.0945          | 0.0664 |
| 0.0089        | 43.69 | 5200 | 0.0941          | 0.0615 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.1+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3

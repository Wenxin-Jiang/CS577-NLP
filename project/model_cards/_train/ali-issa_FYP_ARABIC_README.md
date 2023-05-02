---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-arabic-gpu-colab-similar-to-german-bigger-warm-up
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-arabic-gpu-colab-similar-to-german-bigger-warm-up

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6370
- Wer: 0.4146

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
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 6
- total_train_batch_size: 12
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 5000
- num_epochs: 40
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 9.4958        | 2.83  | 400  | 3.4822          | 1.0    |
| 3.2281        | 5.67  | 800  | 2.9404          | 1.0    |
| 2.942         | 8.51  | 1200 | 2.8690          | 1.0    |
| 2.6346        | 11.35 | 1600 | 1.5452          | 0.9994 |
| 1.3472        | 14.18 | 2000 | 0.8261          | 0.6853 |
| 0.8972        | 17.02 | 2400 | 0.6812          | 0.5737 |
| 0.6924        | 19.85 | 2800 | 0.6552          | 0.5291 |
| 0.5687        | 22.69 | 3200 | 0.6108          | 0.4909 |
| 0.4734        | 25.53 | 3600 | 0.5877          | 0.4674 |
| 0.4029        | 28.37 | 4000 | 0.6204          | 0.4662 |
| 0.3483        | 31.2  | 4400 | 0.5932          | 0.4451 |
| 0.307         | 34.04 | 4800 | 0.6445          | 0.4392 |
| 0.2722        | 36.88 | 5200 | 0.6126          | 0.4292 |
| 0.2247        | 39.71 | 5600 | 0.6370          | 0.4146 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

---
license: mit
tags:
- generated_from_trainer
model-index:
- name: Romance-cleaned-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Romance-cleaned-1

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.7175

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1000
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 0.97  | 29   | 9.9497          |
| No log        | 1.97  | 58   | 9.1816          |
| No log        | 2.97  | 87   | 8.5947          |
| No log        | 3.97  | 116  | 8.2217          |
| No log        | 4.97  | 145  | 7.8354          |
| No log        | 5.97  | 174  | 7.5075          |
| No log        | 6.97  | 203  | 7.2112          |
| No log        | 7.97  | 232  | 6.9077          |
| No log        | 8.97  | 261  | 6.5994          |
| No log        | 9.97  | 290  | 6.3077          |
| No log        | 10.97 | 319  | 6.0416          |
| No log        | 11.97 | 348  | 5.8126          |
| No log        | 12.97 | 377  | 5.6197          |
| No log        | 13.97 | 406  | 5.4789          |
| No log        | 14.97 | 435  | 5.3665          |
| No log        | 15.97 | 464  | 5.2738          |
| No log        | 16.97 | 493  | 5.1942          |
| No log        | 17.97 | 522  | 5.1382          |
| No log        | 18.97 | 551  | 5.0784          |
| No log        | 19.97 | 580  | 5.0347          |
| No log        | 20.97 | 609  | 4.9873          |
| No log        | 21.97 | 638  | 4.9514          |
| No log        | 22.97 | 667  | 4.9112          |
| No log        | 23.97 | 696  | 4.8838          |
| No log        | 24.97 | 725  | 4.8468          |
| No log        | 25.97 | 754  | 4.8221          |
| No log        | 26.97 | 783  | 4.7996          |
| No log        | 27.97 | 812  | 4.7815          |
| No log        | 28.97 | 841  | 4.7606          |
| No log        | 29.97 | 870  | 4.7394          |
| No log        | 30.97 | 899  | 4.7167          |
| No log        | 31.97 | 928  | 4.7140          |
| No log        | 32.97 | 957  | 4.6910          |
| No log        | 33.97 | 986  | 4.6844          |
| No log        | 34.97 | 1015 | 4.6765          |
| No log        | 35.97 | 1044 | 4.6687          |
| No log        | 36.97 | 1073 | 4.6721          |
| No log        | 37.97 | 1102 | 4.6724          |
| No log        | 38.97 | 1131 | 4.6629          |
| No log        | 39.97 | 1160 | 4.6772          |
| No log        | 40.97 | 1189 | 4.6795          |
| No log        | 41.97 | 1218 | 4.6788          |
| No log        | 42.97 | 1247 | 4.6832          |
| No log        | 43.97 | 1276 | 4.6954          |
| No log        | 44.97 | 1305 | 4.7009          |
| No log        | 45.97 | 1334 | 4.7082          |
| No log        | 46.97 | 1363 | 4.7140          |
| No log        | 47.97 | 1392 | 4.7158          |
| No log        | 48.97 | 1421 | 4.7181          |
| No log        | 49.97 | 1450 | 4.7175          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1

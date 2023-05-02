---
license: mit
tags:
- generated_from_trainer
model-index:
- name: Romance-cleaned-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Romance-cleaned-2

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 5.0319

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
| No log        | 0.96  | 16   | 10.3553         |
| No log        | 1.96  | 32   | 9.5625          |
| No log        | 2.96  | 48   | 9.0898          |
| No log        | 3.96  | 64   | 8.7852          |
| No log        | 4.96  | 80   | 8.4694          |
| No log        | 5.96  | 96   | 8.2122          |
| No log        | 6.96  | 112  | 8.0040          |
| No log        | 7.96  | 128  | 7.8029          |
| No log        | 8.96  | 144  | 7.5950          |
| No log        | 9.96  | 160  | 7.4081          |
| No log        | 10.96 | 176  | 7.2391          |
| No log        | 11.96 | 192  | 7.0784          |
| No log        | 12.96 | 208  | 6.9139          |
| No log        | 13.96 | 224  | 6.7530          |
| No log        | 14.96 | 240  | 6.5983          |
| No log        | 15.96 | 256  | 6.4403          |
| No log        | 16.96 | 272  | 6.3025          |
| No log        | 17.96 | 288  | 6.1562          |
| No log        | 18.96 | 304  | 6.0147          |
| No log        | 19.96 | 320  | 5.8919          |
| No log        | 20.96 | 336  | 5.7709          |
| No log        | 21.96 | 352  | 5.6666          |
| No log        | 22.96 | 368  | 5.5818          |
| No log        | 23.96 | 384  | 5.5051          |
| No log        | 24.96 | 400  | 5.4356          |
| No log        | 25.96 | 416  | 5.3788          |
| No log        | 26.96 | 432  | 5.3230          |
| No log        | 27.96 | 448  | 5.2823          |
| No log        | 28.96 | 464  | 5.2513          |
| No log        | 29.96 | 480  | 5.2218          |
| No log        | 30.96 | 496  | 5.1910          |
| No log        | 31.96 | 512  | 5.1609          |
| No log        | 32.96 | 528  | 5.1500          |
| No log        | 33.96 | 544  | 5.1268          |
| No log        | 34.96 | 560  | 5.1012          |
| No log        | 35.96 | 576  | 5.0973          |
| No log        | 36.96 | 592  | 5.0769          |
| No log        | 37.96 | 608  | 5.0653          |
| No log        | 38.96 | 624  | 5.0489          |
| No log        | 39.96 | 640  | 5.0458          |
| No log        | 40.96 | 656  | 5.0379          |
| No log        | 41.96 | 672  | 5.0347          |
| No log        | 42.96 | 688  | 5.0161          |
| No log        | 43.96 | 704  | 5.0226          |
| No log        | 44.96 | 720  | 5.0215          |
| No log        | 45.96 | 736  | 5.0190          |
| No log        | 46.96 | 752  | 5.0087          |
| No log        | 47.96 | 768  | 5.0309          |
| No log        | 48.96 | 784  | 5.0232          |
| No log        | 49.96 | 800  | 5.0319          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1

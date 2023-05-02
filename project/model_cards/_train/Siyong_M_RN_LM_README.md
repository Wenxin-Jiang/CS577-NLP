---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: MilladRN
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# MilladRN

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.4355
- Wer: 0.4907
- Cer: 0.2802

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 4000
- num_epochs: 750
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer    | Cer    |
|:-------------:|:------:|:-----:|:---------------:|:------:|:------:|
| 3.3347        | 33.9   | 2000  | 2.2561          | 0.9888 | 0.6087 |
| 1.3337        | 67.8   | 4000  | 1.8137          | 0.6877 | 0.3407 |
| 0.6504        | 101.69 | 6000  | 2.0718          | 0.6245 | 0.3229 |
| 0.404         | 135.59 | 8000  | 2.2246          | 0.6004 | 0.3221 |
| 0.2877        | 169.49 | 10000 | 2.2624          | 0.5836 | 0.3107 |
| 0.2149        | 203.39 | 12000 | 2.3788          | 0.5279 | 0.2802 |
| 0.1693        | 237.29 | 14000 | 1.8928          | 0.5502 | 0.2937 |
| 0.1383        | 271.19 | 16000 | 2.7520          | 0.5725 | 0.3103 |
| 0.1169        | 305.08 | 18000 | 2.2552          | 0.5446 | 0.2968 |
| 0.1011        | 338.98 | 20000 | 2.6794          | 0.5725 | 0.3119 |
| 0.0996        | 372.88 | 22000 | 2.4704          | 0.5595 | 0.3142 |
| 0.0665        | 406.78 | 24000 | 2.9073          | 0.5836 | 0.3194 |
| 0.0538        | 440.68 | 26000 | 3.1357          | 0.5632 | 0.3213 |
| 0.0538        | 474.58 | 28000 | 2.5639          | 0.5613 | 0.3091 |
| 0.0493        | 508.47 | 30000 | 3.3801          | 0.5613 | 0.3119 |
| 0.0451        | 542.37 | 32000 | 3.5469          | 0.5428 | 0.3158 |
| 0.0307        | 576.27 | 34000 | 4.2243          | 0.5390 | 0.3126 |
| 0.0301        | 610.17 | 36000 | 3.6666          | 0.5297 | 0.2929 |
| 0.0269        | 644.07 | 38000 | 3.2164          | 0.5    | 0.2838 |
| 0.0182        | 677.97 | 40000 | 3.0557          | 0.4963 | 0.2779 |
| 0.0191        | 711.86 | 42000 | 3.5190          | 0.5130 | 0.2921 |
| 0.0133        | 745.76 | 44000 | 3.4355          | 0.4907 | 0.2802 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_10_0
model-index:
- name: fine-tune-Wav2Vec2-XLS-R-300M-Indonesia-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fine-tune-Wav2Vec2-XLS-R-300M-Indonesia-1

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice_10_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2114
- Wer: 0.1762

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
- train_batch_size: 36
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 72
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 60
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.9372        | 4.0   | 460  | 2.8359          | 1.0    |
| 2.2755        | 8.0   | 920  | 0.3708          | 0.3983 |
| 0.6614        | 12.0  | 1380 | 0.2433          | 0.2636 |
| 0.5071        | 16.0  | 1840 | 0.2347          | 0.2395 |
| 0.4516        | 20.0  | 2300 | 0.2213          | 0.2185 |
| 0.4206        | 24.0  | 2760 | 0.2222          | 0.2008 |
| 0.3844        | 28.0  | 3220 | 0.2072          | 0.1887 |
| 0.3678        | 32.0  | 3680 | 0.2071          | 0.1886 |
| 0.3565        | 36.0  | 4140 | 0.2015          | 0.1851 |
| 0.3388        | 40.0  | 4600 | 0.2137          | 0.1850 |
| 0.3235        | 44.0  | 5060 | 0.2072          | 0.1791 |
| 0.3173        | 48.0  | 5520 | 0.2095          | 0.1777 |
| 0.3088        | 52.0  | 5980 | 0.2102          | 0.1784 |
| 0.3           | 56.0  | 6440 | 0.2164          | 0.1772 |
| 0.2957        | 60.0  | 6900 | 0.2114          | 0.1762 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.10.0+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1

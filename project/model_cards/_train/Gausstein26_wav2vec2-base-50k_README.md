---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-base-50k
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-50k

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 3.5640
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
- learning_rate: 7.5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer |
|:-------------:|:-----:|:----:|:---------------:|:---:|
| 10.7005       | 0.48  | 300  | 5.3021          | 1.0 |
| 3.9938        | 0.96  | 600  | 3.4997          | 1.0 |
| 3.591         | 1.44  | 900  | 3.5641          | 1.0 |
| 3.6168        | 1.92  | 1200 | 3.5641          | 1.0 |
| 3.6252        | 2.4   | 1500 | 3.5641          | 1.0 |
| 3.6137        | 2.88  | 1800 | 3.5641          | 1.0 |
| 3.6124        | 3.36  | 2100 | 3.5641          | 1.0 |
| 3.6171        | 3.84  | 2400 | 3.5641          | 1.0 |
| 3.6436        | 4.32  | 2700 | 3.5641          | 1.0 |
| 3.6189        | 4.8   | 3000 | 3.5640          | 1.0 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

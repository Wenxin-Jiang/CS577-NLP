---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_1_0
model-index:
- name: dat259-wav2vec2-en2-copy
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dat259-wav2vec2-en2-copy

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the common_voice_1_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5429
- Wer: 0.5569

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 300
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.5149        | 1.82  | 200  | 3.0474          | 1.0    |
| 2.0483        | 3.64  | 400  | 1.8004          | 0.7808 |
| 0.5464        | 5.45  | 600  | 1.5242          | 0.6529 |
| 0.3269        | 7.27  | 800  | 1.3820          | 0.6046 |
| 0.2337        | 9.09  | 1000 | 1.4605          | 0.5866 |
| 0.1863        | 10.91 | 1200 | 1.5567          | 0.5864 |
| 0.1531        | 12.73 | 1400 | 1.5787          | 0.5871 |
| 0.1326        | 14.55 | 1600 | 1.5766          | 0.5679 |
| 0.1118        | 16.36 | 1800 | 1.4709          | 0.5566 |
| 0.1017        | 18.18 | 2000 | 1.5455          | 0.5598 |
| 0.0955        | 20.0  | 2200 | 1.5429          | 0.5569 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1

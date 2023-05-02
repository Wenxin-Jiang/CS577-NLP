---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-E
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-E

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4832
- Wer: 0.3432

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.5034        | 4.0   | 500  | 1.1620          | 0.8995 |
| 0.5738        | 8.0   | 1000 | 0.4625          | 0.4396 |
| 0.2142        | 12.0  | 1500 | 0.4791          | 0.3965 |
| 0.1219        | 16.0  | 2000 | 0.4677          | 0.3703 |
| 0.0854        | 20.0  | 2500 | 0.4782          | 0.3544 |
| 0.0587        | 24.0  | 3000 | 0.4680          | 0.3516 |
| 0.044         | 28.0  | 3500 | 0.4832          | 0.3432 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.10.3

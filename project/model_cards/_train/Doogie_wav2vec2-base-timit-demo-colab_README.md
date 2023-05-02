---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-base-timit-demo-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-timit-demo-colab

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4180
- Wer: 0.3392

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
| 3.656         | 4.0   | 500  | 1.8973          | 1.0130 |
| 0.8647        | 8.0   | 1000 | 0.4667          | 0.4705 |
| 0.2968        | 12.0  | 1500 | 0.4211          | 0.4035 |
| 0.1719        | 16.0  | 2000 | 0.4725          | 0.3739 |
| 0.1272        | 20.0  | 2500 | 0.4586          | 0.3543 |
| 0.1079        | 24.0  | 3000 | 0.4356          | 0.3484 |
| 0.0808        | 28.0  | 3500 | 0.4180          | 0.3392 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3

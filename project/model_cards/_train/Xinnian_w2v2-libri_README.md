---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: w2v2-libri
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# w2v2-libri

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5387
- Wer: 0.5380

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
- optimizer: Adam with betas=(0.9,0.98) and epsilon=1e-07
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- training_steps: 2500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 8.8253        | 50.0  | 200  | 3.1879          | 1.0    |
| 3.0174        | 100.0 | 400  | 2.9619          | 1.0    |
| 2.8589        | 150.0 | 600  | 2.9499          | 1.0    |
| 1.8086        | 200.0 | 800  | 1.0896          | 0.7123 |
| 0.2145        | 250.0 | 1000 | 1.1973          | 0.6321 |
| 0.0641        | 300.0 | 1200 | 1.3631          | 0.6100 |
| 0.0391        | 350.0 | 1400 | 1.4521          | 0.5837 |
| 0.0258        | 400.0 | 1600 | 1.3671          | 0.5781 |
| 0.0185        | 450.0 | 1800 | 1.3828          | 0.5698 |
| 0.0107        | 500.0 | 2000 | 1.4402          | 0.5463 |
| 0.0099        | 550.0 | 2200 | 1.5724          | 0.5477 |
| 0.0058        | 600.0 | 2400 | 1.5387          | 0.5380 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 1.18.3
- Tokenizers 0.13.2

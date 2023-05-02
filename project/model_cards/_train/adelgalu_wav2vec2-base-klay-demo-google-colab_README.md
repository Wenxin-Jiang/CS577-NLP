---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-base-klay-demo-google-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-klay-demo-google-colab

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0060
- Wer: 0.1791

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
- lr_scheduler_warmup_steps: 500
- num_epochs: 300
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 15.0  | 300  | 2.4020          | 0.9889 |
| 2.4596        | 30.0  | 600  | 1.3773          | 0.9833 |
| 2.4596        | 45.0  | 900  | 0.5241          | 0.7253 |
| 1.1148        | 60.0  | 1200 | 0.2260          | 0.4472 |
| 0.3637        | 75.0  | 1500 | 0.1474          | 0.3682 |
| 0.3637        | 90.0  | 1800 | 0.0742          | 0.2848 |
| 0.1874        | 105.0 | 2100 | 0.0563          | 0.2681 |
| 0.1874        | 120.0 | 2400 | 0.0535          | 0.2436 |
| 0.1273        | 135.0 | 2700 | 0.0335          | 0.2258 |
| 0.0914        | 150.0 | 3000 | 0.0336          | 0.2214 |
| 0.0914        | 165.0 | 3300 | 0.0323          | 0.2136 |
| 0.0733        | 180.0 | 3600 | 0.0225          | 0.2069 |
| 0.0733        | 195.0 | 3900 | 0.0953          | 0.2314 |
| 0.0678        | 210.0 | 4200 | 0.0122          | 0.1902 |
| 0.0428        | 225.0 | 4500 | 0.0104          | 0.1869 |
| 0.0428        | 240.0 | 4800 | 0.0120          | 0.1791 |
| 0.0291        | 255.0 | 5100 | 0.0110          | 0.1835 |
| 0.0291        | 270.0 | 5400 | 0.0062          | 0.1802 |
| 0.0235        | 285.0 | 5700 | 0.0061          | 0.1802 |
| 0.0186        | 300.0 | 6000 | 0.0060          | 0.1791 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1

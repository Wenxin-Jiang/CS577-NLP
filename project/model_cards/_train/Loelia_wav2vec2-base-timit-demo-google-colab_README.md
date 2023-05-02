---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-base-timit-demo-google-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-timit-demo-google-colab

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4414
- Wer: 0.3578

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
- lr_scheduler_warmup_steps: 1000
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.095         | 1.0   | 500  | 0.4785          | 0.3873 |
| 0.09          | 2.01  | 1000 | 0.5840          | 0.4203 |
| 0.1059        | 3.01  | 1500 | 0.5674          | 0.4073 |
| 0.0857        | 4.02  | 2000 | 0.5026          | 0.3797 |
| 0.0719        | 5.02  | 2500 | 0.4981          | 0.3783 |
| 0.0565        | 6.02  | 3000 | 0.4595          | 0.3721 |
| 0.0463        | 7.03  | 3500 | 0.4578          | 0.3629 |
| 0.0363        | 8.03  | 4000 | 0.4832          | 0.3669 |
| 0.0444        | 9.04  | 4500 | 0.4414          | 0.3578 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-base-timit-demo-google-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-timit-demo-google-colab

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5452
- Wer: 0.3296

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
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 3.5557        | 1.0   | 500   | 1.9362          | 1.0072 |
| 0.867         | 2.01  | 1000  | 0.5197          | 0.5173 |
| 0.4281        | 3.01  | 1500  | 0.4609          | 0.4552 |
| 0.3002        | 4.02  | 2000  | 0.4066          | 0.4129 |
| 0.2252        | 5.02  | 2500  | 0.4122          | 0.3952 |
| 0.1857        | 6.02  | 3000  | 0.4650          | 0.3990 |
| 0.1541        | 7.03  | 3500  | 0.4784          | 0.3834 |
| 0.1372        | 8.03  | 4000  | 0.3875          | 0.3805 |
| 0.1213        | 9.04  | 4500  | 0.5606          | 0.4002 |
| 0.1043        | 10.04 | 5000  | 0.4713          | 0.3762 |
| 0.0972        | 11.04 | 5500  | 0.4770          | 0.3692 |
| 0.0876        | 12.05 | 6000  | 0.4755          | 0.3671 |
| 0.0812        | 13.05 | 6500  | 0.4854          | 0.3616 |
| 0.0705        | 14.06 | 7000  | 0.4380          | 0.3659 |
| 0.0759        | 15.06 | 7500  | 0.5025          | 0.3516 |
| 0.0709        | 16.06 | 8000  | 0.5310          | 0.3577 |
| 0.0572        | 17.07 | 8500  | 0.5097          | 0.3561 |
| 0.0572        | 18.07 | 9000  | 0.5150          | 0.3510 |
| 0.0482        | 19.08 | 9500  | 0.4954          | 0.3488 |
| 0.0703        | 20.08 | 10000 | 0.5279          | 0.3512 |
| 0.0457        | 21.08 | 10500 | 0.5336          | 0.3459 |
| 0.036         | 22.09 | 11000 | 0.5471          | 0.3440 |
| 0.0368        | 23.09 | 11500 | 0.5109          | 0.3417 |
| 0.0342        | 24.1  | 12000 | 0.5506          | 0.3415 |
| 0.0318        | 25.1  | 12500 | 0.5291          | 0.3357 |
| 0.03          | 26.1  | 13000 | 0.5347          | 0.3363 |
| 0.026         | 27.11 | 13500 | 0.5475          | 0.3318 |
| 0.0232        | 28.11 | 14000 | 0.5628          | 0.3332 |
| 0.0246        | 29.12 | 14500 | 0.5452          | 0.3296 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1

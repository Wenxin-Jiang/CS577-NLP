---
license: mit
tags:
- generated_from_trainer
model-index:
- name: deberta-classifier-feedback-1024-pseudo-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-classifier-feedback-1024-pseudo-final

This model is a fine-tuned version of [TTian/deberta-classifier-feedback-1024-pseudo](https://huggingface.co/TTian/deberta-classifier-feedback-1024-pseudo) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5263

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.5814        | 0.04  | 10   | 0.5888          |
| 0.5521        | 0.08  | 20   | 0.5736          |
| 0.5685        | 0.13  | 30   | 0.5809          |
| 0.6052        | 0.17  | 40   | 0.5702          |
| 0.5532        | 0.21  | 50   | 0.5571          |
| 0.6177        | 0.25  | 60   | 0.5848          |
| 0.6196        | 0.3   | 70   | 0.5464          |
| 0.5772        | 0.34  | 80   | 0.5307          |
| 0.5805        | 0.38  | 90   | 0.5550          |
| 0.6453        | 0.42  | 100  | 0.5467          |
| 0.5756        | 0.47  | 110  | 0.5587          |
| 0.5901        | 0.51  | 120  | 0.5482          |
| 0.568         | 0.55  | 130  | 0.5263          |
| 0.5452        | 0.59  | 140  | 0.5698          |
| 0.5949        | 0.64  | 150  | 0.5484          |
| 0.5537        | 0.68  | 160  | 0.5783          |
| 0.5327        | 0.72  | 170  | 0.5202          |
| 0.5449        | 0.76  | 180  | 0.5272          |
| 0.5345        | 0.81  | 190  | 0.5621          |
| 0.5837        | 0.85  | 200  | 0.5501          |
| 0.5969        | 0.89  | 210  | 0.5470          |
| 0.5905        | 0.93  | 220  | 0.5924          |
| 0.5481        | 0.97  | 230  | 0.5415          |
| 0.5035        | 1.02  | 240  | 0.5321          |
| 0.4508        | 1.06  | 250  | 0.5371          |
| 0.4227        | 1.1   | 260  | 0.5276          |
| 0.4423        | 1.14  | 270  | 0.5324          |
| 0.432         | 1.19  | 280  | 0.5378          |
| 0.4317        | 1.23  | 290  | 0.5302          |
| 0.46          | 1.27  | 300  | 0.5302          |
| 0.435         | 1.31  | 310  | 0.5326          |
| 0.3813        | 1.36  | 320  | 0.5431          |
| 0.4422        | 1.4   | 330  | 0.5323          |
| 0.4298        | 1.44  | 340  | 0.5575          |
| 0.5068        | 1.48  | 350  | 0.5529          |
| 0.4619        | 1.53  | 360  | 0.5589          |
| 0.4852        | 1.57  | 370  | 0.5256          |
| 0.3888        | 1.61  | 380  | 0.5731          |
| 0.4319        | 1.65  | 390  | 0.5335          |
| 0.4422        | 1.69  | 400  | 0.5419          |
| 0.4522        | 1.74  | 410  | 0.5547          |
| 0.4276        | 1.78  | 420  | 0.5263          |
| 0.3988        | 1.82  | 430  | 0.5481          |
| 0.4063        | 1.86  | 440  | 0.5404          |
| 0.4141        | 1.91  | 450  | 0.5292          |
| 0.4149        | 1.95  | 460  | 0.5241          |
| 0.4104        | 1.99  | 470  | 0.5263          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2

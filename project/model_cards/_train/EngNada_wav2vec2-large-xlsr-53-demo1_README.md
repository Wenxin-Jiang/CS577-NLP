---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xlsr-53-demo1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-53-demo1

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9692
- Wer: 0.8462

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 5
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 10
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 12.978        | 0.06  | 100  | 3.5377          | 1.0    |
| 3.5026        | 0.13  | 200  | 3.4366          | 1.0    |
| 3.4084        | 0.19  | 300  | 3.3831          | 1.0    |
| 3.3551        | 0.26  | 400  | 3.2563          | 1.0    |
| 3.2668        | 0.32  | 500  | 3.2109          | 1.0    |
| 2.9398        | 0.38  | 600  | 2.4548          | 0.9987 |
| 2.2204        | 0.45  | 700  | 1.8870          | 1.0135 |
| 1.7401        | 0.51  | 800  | 1.6816          | 1.0247 |
| 1.5748        | 0.57  | 900  | 1.4741          | 0.9953 |
| 1.4539        | 0.64  | 1000 | 1.4573          | 0.9852 |
| 1.3612        | 0.7   | 1100 | 1.3534          | 0.9529 |
| 1.3328        | 0.77  | 1200 | 1.3380          | 0.9320 |
| 1.2459        | 0.83  | 1300 | 1.2984          | 0.9247 |
| 1.1976        | 0.89  | 1400 | 1.2515          | 0.9252 |
| 1.1593        | 0.96  | 1500 | 1.2345          | 0.9030 |
| 1.1094        | 1.02  | 1600 | 1.2135          | 0.9305 |
| 1.0485        | 1.09  | 1700 | 1.2045          | 0.9121 |
| 0.9893        | 1.15  | 1800 | 1.1876          | 0.8990 |
| 1.0099        | 1.21  | 1900 | 1.1663          | 0.8889 |
| 0.982         | 1.28  | 2000 | 1.1674          | 0.8901 |
| 0.9975        | 1.34  | 2100 | 1.1181          | 0.8812 |
| 0.952         | 1.4   | 2200 | 1.1119          | 0.8817 |
| 0.9311        | 1.47  | 2300 | 1.0786          | 0.8773 |
| 0.9398        | 1.53  | 2400 | 1.1016          | 0.8720 |
| 0.9148        | 1.6   | 2500 | 1.0878          | 0.8778 |
| 0.9114        | 1.66  | 2600 | 1.1004          | 0.8712 |
| 0.902         | 1.72  | 2700 | 1.0223          | 0.8744 |
| 0.8978        | 1.79  | 2800 | 1.0616          | 0.8459 |
| 0.8675        | 1.85  | 2900 | 1.0974          | 0.8643 |
| 0.8373        | 1.92  | 3000 | 1.0389          | 0.8547 |
| 0.8575        | 1.98  | 3100 | 1.0388          | 0.8480 |
| 0.8313        | 2.04  | 3200 | 1.0001          | 0.8648 |
| 0.7357        | 2.11  | 3300 | 1.0222          | 0.8705 |
| 0.743         | 2.17  | 3400 | 1.0859          | 0.8765 |
| 0.7306        | 2.23  | 3500 | 1.0109          | 0.8515 |
| 0.7525        | 2.3   | 3600 | 0.9942          | 0.8619 |
| 0.7308        | 2.36  | 3700 | 1.0004          | 0.8578 |
| 0.7266        | 2.43  | 3800 | 1.0003          | 0.8497 |
| 0.737         | 2.49  | 3900 | 1.0146          | 0.8505 |
| 0.7202        | 2.55  | 4000 | 1.0172          | 0.8653 |
| 0.6945        | 2.62  | 4100 | 0.9894          | 0.8415 |
| 0.6633        | 2.68  | 4200 | 0.9894          | 0.8496 |
| 0.6972        | 2.75  | 4300 | 0.9805          | 0.8505 |
| 0.6872        | 2.81  | 4400 | 0.9939          | 0.8509 |
| 0.7238        | 2.87  | 4500 | 0.9740          | 0.8532 |
| 0.6847        | 2.94  | 4600 | 0.9692          | 0.8462 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.14.0
- Tokenizers 0.10.3

---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-base-asc-demo-google-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-asc-demo-google-colab

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9473
- Wer: 0.8943

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
- lr_scheduler_warmup_steps: 100
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 10.9515       | 1.06  | 100  | 4.0400          | 1.0    |
| 3.026         | 2.13  | 200  | 3.7680          | 1.0    |
| 2.9349        | 3.19  | 300  | 3.8252          | 1.0    |
| 2.7955        | 4.26  | 400  | 3.4536          | 1.0    |
| 2.5002        | 5.32  | 500  | 3.1430          | 1.0    |
| 1.8767        | 6.38  | 600  | 2.5167          | 1.0    |
| 1.179         | 7.45  | 700  | 1.8392          | 0.9879 |
| 0.7846        | 8.51  | 800  | 1.3472          | 0.9293 |
| 0.4949        | 9.57  | 900  | 1.4321          | 0.94   |
| 0.3398        | 10.64 | 1000 | 1.2133          | 0.9214 |
| 0.3259        | 11.7  | 1100 | 1.6726          | 0.9207 |
| 0.2736        | 12.77 | 1200 | 1.6282          | 0.9114 |
| 0.224         | 13.83 | 1300 | 1.6113          | 0.9    |
| 0.1962        | 14.89 | 1400 | 1.6028          | 0.8986 |
| 0.1734        | 15.96 | 1500 | 1.7467          | 0.8979 |
| 0.1761        | 17.02 | 1600 | 1.8196          | 0.8993 |
| 0.1574        | 18.09 | 1700 | 1.8836          | 0.895  |
| 0.1397        | 19.15 | 1800 | 1.7974          | 0.8921 |
| 0.145         | 20.21 | 1900 | 1.7876          | 0.8971 |
| 0.1311        | 21.28 | 2000 | 1.8534          | 0.9029 |
| 0.1329        | 22.34 | 2100 | 1.8521          | 0.8914 |
| 0.1141        | 23.4  | 2200 | 1.8889          | 0.8914 |
| 0.1307        | 24.47 | 2300 | 1.9190          | 0.8957 |
| 0.1094        | 25.53 | 2400 | 1.9745          | 0.8943 |
| 0.1133        | 26.6  | 2500 | 1.9405          | 0.8936 |
| 0.0967        | 27.66 | 2600 | 1.9461          | 0.8914 |
| 0.1088        | 28.72 | 2700 | 1.9458          | 0.8943 |
| 0.1066        | 29.79 | 2800 | 1.9473          | 0.8943 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

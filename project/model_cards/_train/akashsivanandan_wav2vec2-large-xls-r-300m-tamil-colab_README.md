---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-tamil-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-tamil-colab

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8072
- Wer: 0.6531

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 11.0967       | 1.0   | 118  | 4.6437          | 1.0    |
| 3.4973        | 2.0   | 236  | 3.2588          | 1.0    |
| 3.1305        | 3.0   | 354  | 2.6566          | 1.0    |
| 1.2931        | 4.0   | 472  | 0.9156          | 0.9944 |
| 0.6851        | 5.0   | 590  | 0.7474          | 0.8598 |
| 0.525         | 6.0   | 708  | 0.6649          | 0.7995 |
| 0.4325        | 7.0   | 826  | 0.6740          | 0.7752 |
| 0.3766        | 8.0   | 944  | 0.6220          | 0.7628 |
| 0.3256        | 9.0   | 1062 | 0.6316          | 0.7322 |
| 0.2802        | 10.0  | 1180 | 0.6442          | 0.7305 |
| 0.2575        | 11.0  | 1298 | 0.6885          | 0.7280 |
| 0.2248        | 12.0  | 1416 | 0.6702          | 0.7197 |
| 0.2089        | 13.0  | 1534 | 0.6781          | 0.7173 |
| 0.1893        | 14.0  | 1652 | 0.6981          | 0.7049 |
| 0.1652        | 15.0  | 1770 | 0.7154          | 0.7436 |
| 0.1643        | 16.0  | 1888 | 0.6798          | 0.7023 |
| 0.1472        | 17.0  | 2006 | 0.7381          | 0.6947 |
| 0.1372        | 18.0  | 2124 | 0.7240          | 0.7065 |
| 0.1318        | 19.0  | 2242 | 0.7305          | 0.6714 |
| 0.1211        | 20.0  | 2360 | 0.7288          | 0.6597 |
| 0.1178        | 21.0  | 2478 | 0.7417          | 0.6699 |
| 0.1118        | 22.0  | 2596 | 0.7476          | 0.6753 |
| 0.1016        | 23.0  | 2714 | 0.7973          | 0.6647 |
| 0.0998        | 24.0  | 2832 | 0.8027          | 0.6633 |
| 0.0917        | 25.0  | 2950 | 0.8045          | 0.6680 |
| 0.0907        | 26.0  | 3068 | 0.7884          | 0.6565 |
| 0.0835        | 27.0  | 3186 | 0.8009          | 0.6622 |
| 0.0749        | 28.0  | 3304 | 0.8123          | 0.6536 |
| 0.0755        | 29.0  | 3422 | 0.8006          | 0.6555 |
| 0.074         | 30.0  | 3540 | 0.8072          | 0.6531 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3

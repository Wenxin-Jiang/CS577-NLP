---
license: apache-2.0
tags:
- automatic-speech-recognition
- NbAiLab/NPSC
- generated_from_trainer
model-index:
- name: wav2vec2-xlsr-300M-NPSC-OH
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xlsr-300M-NPSC-OH

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the NBAILAB/NPSC - 16K_MP3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1692
- Wer: 0.1663

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 13
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 15.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 3.1638        | 0.66  | 500   | 3.0686          | 1.0    |
| 2.9311        | 1.31  | 1000  | 2.9208          | 1.0    |
| 2.4175        | 1.97  | 1500  | 1.5009          | 0.9049 |
| 1.4442        | 2.63  | 2000  | 0.4426          | 0.3783 |
| 1.2624        | 3.28  | 2500  | 0.3193          | 0.2998 |
| 1.1889        | 3.94  | 3000  | 0.2867          | 0.2630 |
| 1.1315        | 4.6   | 3500  | 0.2566          | 0.2444 |
| 1.0864        | 5.26  | 4000  | 0.2368          | 0.2294 |
| 1.093         | 5.91  | 4500  | 0.2240          | 0.2151 |
| 1.0368        | 6.57  | 5000  | 0.2117          | 0.2056 |
| 1.0178        | 7.23  | 5500  | 0.2020          | 0.1954 |
| 1.0035        | 7.88  | 6000  | 0.2005          | 0.1924 |
| 0.9759        | 8.54  | 6500  | 0.1971          | 0.1863 |
| 0.9795        | 9.2   | 7000  | 0.1892          | 0.1812 |
| 0.9601        | 9.85  | 7500  | 0.1863          | 0.1795 |
| 0.9673        | 10.51 | 8000  | 0.1809          | 0.1761 |
| 0.9233        | 11.17 | 8500  | 0.1818          | 0.1755 |
| 0.9382        | 11.83 | 9000  | 0.1767          | 0.1741 |
| 0.9242        | 12.48 | 9500  | 0.1743          | 0.1703 |
| 0.9703        | 13.14 | 10000 | 0.1711          | 0.1711 |
| 0.9139        | 13.8  | 10500 | 0.1718          | 0.1672 |
| 0.9073        | 14.45 | 11000 | 0.1700          | 0.1665 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0

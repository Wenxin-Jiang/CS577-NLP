---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-l-xlsr-es-col-pro-noise
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-l-xlsr-es-col-pro-noise

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-spanish](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-spanish) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0677
- Wer: 0.0380

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
| 0.94          | 1.21  | 400  | 0.0800          | 0.0814 |
| 0.4711        | 2.42  | 800  | 0.0730          | 0.0692 |
| 0.3451        | 3.62  | 1200 | 0.0729          | 0.0669 |
| 0.2958        | 4.83  | 1600 | 0.0796          | 0.0667 |
| 0.2544        | 6.04  | 2000 | 0.0808          | 0.0584 |
| 0.227         | 7.25  | 2400 | 0.0791          | 0.0643 |
| 0.2061        | 8.46  | 2800 | 0.0718          | 0.0582 |
| 0.1901        | 9.67  | 3200 | 0.0709          | 0.0587 |
| 0.179         | 10.87 | 3600 | 0.0698          | 0.0558 |
| 0.1693        | 12.08 | 4000 | 0.0709          | 0.0530 |
| 0.1621        | 13.29 | 4400 | 0.0640          | 0.0487 |
| 0.1443        | 14.5  | 4800 | 0.0793          | 0.0587 |
| 0.1408        | 15.71 | 5200 | 0.0741          | 0.0528 |
| 0.1377        | 16.92 | 5600 | 0.0702          | 0.0462 |
| 0.1292        | 18.13 | 6000 | 0.0822          | 0.0539 |
| 0.1197        | 19.33 | 6400 | 0.0625          | 0.0436 |
| 0.1137        | 20.54 | 6800 | 0.0650          | 0.0419 |
| 0.1017        | 21.75 | 7200 | 0.0630          | 0.0392 |
| 0.0976        | 22.96 | 7600 | 0.0630          | 0.0387 |
| 0.0942        | 24.17 | 8000 | 0.0631          | 0.0380 |
| 0.0924        | 25.38 | 8400 | 0.0645          | 0.0374 |
| 0.0862        | 26.59 | 8800 | 0.0677          | 0.0402 |
| 0.0831        | 27.79 | 9200 | 0.0680          | 0.0393 |
| 0.077         | 29.0  | 9600 | 0.0677          | 0.0380 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.1+cu102
- Datasets 1.13.3
- Tokenizers 0.10.3

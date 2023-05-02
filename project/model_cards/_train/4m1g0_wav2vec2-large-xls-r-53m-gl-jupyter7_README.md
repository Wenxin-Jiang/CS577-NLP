---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xls-r-53m-gl-jupyter7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-53m-gl-jupyter7

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1000
- Wer: 0.0639

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
- num_epochs: 60
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.8697        | 3.36  | 400  | 0.2631          | 0.2756 |
| 0.1569        | 6.72  | 800  | 0.1243          | 0.1300 |
| 0.0663        | 10.08 | 1200 | 0.1124          | 0.1153 |
| 0.0468        | 13.44 | 1600 | 0.1118          | 0.1037 |
| 0.0356        | 16.8  | 2000 | 0.1102          | 0.0978 |
| 0.0306        | 20.17 | 2400 | 0.1095          | 0.0935 |
| 0.0244        | 23.53 | 2800 | 0.1072          | 0.0844 |
| 0.0228        | 26.89 | 3200 | 0.1014          | 0.0874 |
| 0.0192        | 30.25 | 3600 | 0.1084          | 0.0831 |
| 0.0174        | 33.61 | 4000 | 0.1048          | 0.0772 |
| 0.0142        | 36.97 | 4400 | 0.1063          | 0.0764 |
| 0.0131        | 40.33 | 4800 | 0.1046          | 0.0770 |
| 0.0116        | 43.69 | 5200 | 0.0999          | 0.0716 |
| 0.0095        | 47.06 | 5600 | 0.1044          | 0.0729 |
| 0.0077        | 50.42 | 6000 | 0.1024          | 0.0670 |
| 0.0071        | 53.78 | 6400 | 0.0968          | 0.0631 |
| 0.0064        | 57.14 | 6800 | 0.1000          | 0.0639 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.1+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3

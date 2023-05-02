---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-dutch-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-dutch-baseline

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5107
- Wer: 0.2674
- Cer: 0.0863

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- total_eval_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 3.655         | 1.31  | 400  | 0.9337          | 0.7332 | 0.2534 |
| 0.42          | 2.61  | 800  | 0.5018          | 0.4115 | 0.1374 |
| 0.2267        | 3.92  | 1200 | 0.4776          | 0.3791 | 0.1259 |
| 0.1624        | 5.23  | 1600 | 0.4807          | 0.3590 | 0.1208 |
| 0.135         | 6.54  | 2000 | 0.4899          | 0.3417 | 0.1121 |
| 0.1179        | 7.84  | 2400 | 0.5096          | 0.3445 | 0.1133 |
| 0.1035        | 9.15  | 2800 | 0.4563          | 0.3455 | 0.1129 |
| 0.092         | 10.46 | 3200 | 0.5061          | 0.3382 | 0.1127 |
| 0.0804        | 11.76 | 3600 | 0.4969          | 0.3285 | 0.1088 |
| 0.0748        | 13.07 | 4000 | 0.5274          | 0.3380 | 0.1114 |
| 0.0669        | 14.38 | 4400 | 0.5201          | 0.3115 | 0.1028 |
| 0.0588        | 15.69 | 4800 | 0.5238          | 0.3212 | 0.1054 |
| 0.0561        | 16.99 | 5200 | 0.5273          | 0.3185 | 0.1044 |
| 0.0513        | 18.3  | 5600 | 0.5577          | 0.3032 | 0.1010 |
| 0.0476        | 19.61 | 6000 | 0.5298          | 0.3050 | 0.1008 |
| 0.0408        | 20.91 | 6400 | 0.5725          | 0.2982 | 0.0984 |
| 0.0376        | 22.22 | 6800 | 0.5605          | 0.2953 | 0.0966 |
| 0.0339        | 23.53 | 7200 | 0.5419          | 0.2865 | 0.0938 |
| 0.0315        | 24.84 | 7600 | 0.5530          | 0.2782 | 0.0915 |
| 0.0286        | 26.14 | 8000 | 0.5354          | 0.2788 | 0.0917 |
| 0.0259        | 27.45 | 8400 | 0.5245          | 0.2715 | 0.0878 |
| 0.0231        | 28.76 | 8800 | 0.5107          | 0.2674 | 0.0863 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.0+cu102
- Datasets 2.7.1
- Tokenizers 0.13.2

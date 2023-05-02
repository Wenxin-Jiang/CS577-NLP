---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-korean-demo-colab-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-korean-demo-colab-2

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2481
- Wer: 0.2480

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
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.7387        | 2.12  | 400  | 3.1791          | 1.0    |
| 1.3766        | 4.23  | 800  | 0.4876          | 0.5264 |
| 0.476         | 6.35  | 1200 | 0.2955          | 0.3648 |
| 0.3209        | 8.46  | 1600 | 0.2926          | 0.3473 |
| 0.2591        | 10.58 | 2000 | 0.2723          | 0.3094 |
| 0.2055        | 12.7  | 2400 | 0.2746          | 0.3027 |
| 0.1802        | 14.81 | 2800 | 0.2672          | 0.2976 |
| 0.1552        | 16.93 | 3200 | 0.2822          | 0.2807 |
| 0.1413        | 19.05 | 3600 | 0.2652          | 0.2856 |
| 0.1232        | 21.16 | 4000 | 0.2631          | 0.2655 |
| 0.1146        | 23.28 | 4400 | 0.2561          | 0.2574 |
| 0.1086        | 25.4  | 4800 | 0.2461          | 0.2527 |
| 0.0944        | 27.51 | 5200 | 0.2521          | 0.2535 |
| 0.0881        | 29.63 | 5600 | 0.2481          | 0.2480 |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

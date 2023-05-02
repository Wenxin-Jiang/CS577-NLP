---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xlsr-53-demo-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-53-demo-colab

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4253
- Wer: 0.4880

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
| 5.2135        | 4.21  | 400  | 2.5232          | 1.0    |
| 0.8323        | 8.42  | 800  | 0.4673          | 0.6142 |
| 0.3247        | 12.63 | 1200 | 0.4087          | 0.5536 |
| 0.217         | 16.84 | 1600 | 0.3950          | 0.5237 |
| 0.166         | 21.05 | 2000 | 0.4294          | 0.5075 |
| 0.141         | 25.26 | 2400 | 0.4219          | 0.4944 |
| 0.1193        | 29.47 | 2800 | 0.4253          | 0.4880 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu102
- Datasets 2.1.0
- Tokenizers 0.12.1

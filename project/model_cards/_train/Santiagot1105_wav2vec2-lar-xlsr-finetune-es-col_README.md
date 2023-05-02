---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-lar-xlsr-finetune-es-col
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-lar-xlsr-finetune-es-col

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1669
- Wer: 0.2595

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
| 5.1108        | 8.51  | 400  | 0.5936          | 0.6085 |
| 0.3015        | 17.02 | 800  | 0.2071          | 0.2941 |
| 0.0989        | 25.53 | 1200 | 0.1669          | 0.2595 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.1+cu102
- Datasets 1.13.3
- Tokenizers 0.10.3

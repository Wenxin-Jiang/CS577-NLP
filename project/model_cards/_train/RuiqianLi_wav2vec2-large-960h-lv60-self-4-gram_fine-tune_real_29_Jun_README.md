---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- uob_singlish
model-index:
- name: wav2vec2-large-960h-lv60-self-4-gram_fine-tune_real_29_Jun
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-960h-lv60-self-4-gram_fine-tune_real_29_Jun

This model is a fine-tuned version of [facebook/wav2vec2-large-960h-lv60-self](https://huggingface.co/facebook/wav2vec2-large-960h-lv60-self) on the uob_singlish dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2895
- Wer: 0.4583

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.1283        | 1.82  | 20   | 1.5236          | 0.5764 |
| 1.3015        | 3.64  | 40   | 1.2956          | 0.4931 |
| 0.9918        | 5.45  | 60   | 1.3087          | 0.5347 |
| 0.849         | 7.27  | 80   | 1.2914          | 0.5139 |
| 0.6191        | 9.09  | 100  | 1.2895          | 0.4583 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- filipino_voice
model-index:
- name: english-filipino-wav2vec2-l-xls-r-test-06
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# english-filipino-wav2vec2-l-xls-r-test-06

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) on the filipino_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5806
- Wer: 0.6568

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.002
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.0031        | 2.09  | 400  | 1.2366          | 0.8780 |
| 0.9084        | 4.19  | 800  | 1.0653          | 0.8081 |
| 0.6484        | 6.28  | 1200 | 1.1648          | 0.8258 |
| 0.5335        | 8.38  | 1600 | 1.0903          | 0.7542 |
| 0.4359        | 10.47 | 2000 | 0.9466          | 0.7058 |
| 0.3629        | 12.57 | 2400 | 0.9266          | 0.7048 |
| 0.3057        | 14.66 | 2800 | 1.0879          | 0.7018 |
| 0.2477        | 16.75 | 3200 | 1.1113          | 0.7022 |
| 0.208         | 18.85 | 3600 | 1.1345          | 0.6742 |
| 0.1781        | 20.94 | 4000 | 1.3117          | 0.6974 |
| 0.1465        | 23.04 | 4400 | 1.3248          | 0.6916 |
| 0.1288        | 25.13 | 4800 | 1.4306          | 0.6523 |
| 0.1108        | 27.23 | 5200 | 1.5155          | 0.6685 |
| 0.099         | 29.32 | 5600 | 1.5806          | 0.6568 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

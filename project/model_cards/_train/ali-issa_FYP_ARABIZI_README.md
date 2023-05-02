---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-Arabizi-gpu-colab-similar-to-german-param
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-Arabizi-gpu-colab-similar-to-german-param

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5609
- Wer: 0.4042

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 6
- total_train_batch_size: 12
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.6416        | 2.83  | 400  | 2.8983          | 1.0    |
| 1.4951        | 5.67  | 800  | 0.6272          | 0.6097 |
| 0.6419        | 8.51  | 1200 | 0.5491          | 0.5069 |
| 0.4767        | 11.35 | 1600 | 0.5152          | 0.4553 |
| 0.3899        | 14.18 | 2000 | 0.5436          | 0.4475 |
| 0.3342        | 17.02 | 2400 | 0.5400          | 0.4431 |
| 0.2982        | 19.85 | 2800 | 0.5599          | 0.4248 |
| 0.2738        | 22.69 | 3200 | 0.5401          | 0.4103 |
| 0.2563        | 25.53 | 3600 | 0.5710          | 0.4198 |
| 0.2443        | 28.37 | 4000 | 0.5609          | 0.4042 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

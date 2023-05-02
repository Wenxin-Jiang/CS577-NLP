---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xlsr-53-AL-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xlsr-53-AL-colab

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5358
- Wer: 0.5443

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.9391        | 0.4   | 400  | 2.0722          | 0.9249 |
| 0.8775        | 0.8   | 800  | 1.7171          | 0.6778 |
| 0.665         | 1.2   | 1200 | 1.7250          | 0.6235 |
| 0.6135        | 1.6   | 1600 | 1.4021          | 0.5847 |
| 0.5795        | 2.0   | 2000 | 1.6191          | 0.5696 |
| 0.5031        | 2.4   | 2400 | 1.6767          | 0.5586 |
| 0.4933        | 2.8   | 2800 | 1.5358          | 0.5443 |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3

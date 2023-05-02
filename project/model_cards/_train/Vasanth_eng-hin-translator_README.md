---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: eng-hin-translator
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# eng-hin-translator

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-hi](https://huggingface.co/Helsinki-NLP/opus-mt-en-hi) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4143
- Bleu Score: 34.2532

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu Score |
|:-------------:|:-----:|:----:|:---------------:|:----------:|
| 1.7332        | 1.0   | 548  | 1.5131          | 31.6167    |
| 1.3588        | 2.0   | 1096 | 1.4463          | 33.0225    |
| 1.1651        | 3.0   | 1644 | 1.4209          | 34.0514    |
| 1.042         | 4.0   | 2192 | 1.4139          | 34.0137    |
| 0.9686        | 5.0   | 2740 | 1.4143          | 34.2532    |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1

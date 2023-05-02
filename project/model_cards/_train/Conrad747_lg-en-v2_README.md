---
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: lg-en-test-version
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# lg-en-test-version

This model is a fine-tuned version of [AI-Lab-Makerere/lg_en](https://huggingface.co/AI-Lab-Makerere/lg_en) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5803
- Bleu: 31.3111

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 9.687717341785184e-05
- train_batch_size: 15
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| No log        | 1.0   | 24   | 1.0100          | 28.5722 |
| No log        | 2.0   | 48   | 0.7758          | 27.7506 |
| No log        | 3.0   | 72   | 0.6459          | 40.3866 |
| No log        | 4.0   | 96   | 0.5803          | 31.3111 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

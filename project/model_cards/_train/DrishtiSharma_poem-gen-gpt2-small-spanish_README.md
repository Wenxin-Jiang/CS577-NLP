---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: poem-gen-gpt2-small-spanish
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# poem-gen-gpt2-small-spanish

This model is a fine-tuned version of [datificate/gpt2-small-spanish](https://huggingface.co/datificate/gpt2-small-spanish) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.9229

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 4.2121        | 1.0   | 2569 | 3.9954          |
| 4.0612        | 2.0   | 5138 | 3.9375          |
| 3.9988        | 3.0   | 7707 | 3.9229          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

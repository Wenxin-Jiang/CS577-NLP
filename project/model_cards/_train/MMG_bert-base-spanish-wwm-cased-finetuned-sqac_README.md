---
tags:
- generated_from_trainer
datasets:
- sqac
model-index:
- name: bert-base-spanish-wwm-cased-finetuned-sqac
  results: []
language:
- es
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-spanish-wwm-cased-finetuned-sqac

This model is a fine-tuned version of [dccuchile/bert-base-spanish-wwm-cased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) on the sqac dataset.
It achieves the following results on the evaluation set:
{'exact_match': 62.017167, 'f1': 79.452767}

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.1335        | 1.0   | 1230 | 0.9346          |
| 0.6794        | 2.0   | 2460 | 0.8634          |
| 0.3992        | 3.0   | 3690 | 0.9662          |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3

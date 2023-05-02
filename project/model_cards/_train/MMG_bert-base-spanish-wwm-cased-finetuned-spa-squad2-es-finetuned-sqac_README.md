---
tags:
- generated_from_trainer
datasets:
- sqac
model-index:
- name: bert-base-spanish-wwm-cased-finetuned-spa-squad2-es-finetuned-sqac-v2
  results: []
language:
- es
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-spanish-wwm-cased-finetuned-spa-squad2-es-finetuned-sqac-v2

This model is a fine-tuned version of [mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es](https://huggingface.co/mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es) on the sqac dataset.
It achieves the following results on the evaluation set:
- {'exact_match': 65.02145922746782, 'f1': 81.6651482773275}

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
| 0.9417        | 1.0   | 1277 | 0.7903          |
| 0.5002        | 2.0   | 2554 | 0.8459          |
| 0.2895        | 3.0   | 3831 | 0.9482          |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3

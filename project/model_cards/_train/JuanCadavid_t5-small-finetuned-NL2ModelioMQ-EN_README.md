---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- generator
model-index:
- name: t5-small-finetuned-NL2ModelioMQ-EN
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-NL2ModelioMQ-EN

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the generator dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0000
- Rouge2 Precision: 0.9789
- Rouge2 Recall: 0.6055
- Rouge2 Fmeasure: 0.7295

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge2 Precision | Rouge2 Recall | Rouge2 Fmeasure |
|:-------------:|:-----:|:-----:|:---------------:|:----------------:|:-------------:|:---------------:|
| 0.0107        | 1.0   | 4449  | 0.0006          | 0.9688           | 0.6005        | 0.7229          |
| 0.0022        | 2.0   | 8898  | 0.0001          | 0.9787           | 0.6054        | 0.7294          |
| 0.001         | 3.0   | 13347 | 0.0000          | 0.9789           | 0.6055        | 0.7295          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5-small-finetuned-NL2ModelioMQ
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-NL2ModelioMQ

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0755
- Rouge2 Precision: 0.7481
- Rouge2 Recall: 0.462
- Rouge2 Fmeasure: 0.5577

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

| Training Loss | Epoch | Step | Validation Loss | Rouge2 Precision | Rouge2 Recall | Rouge2 Fmeasure |
|:-------------:|:-----:|:----:|:---------------:|:----------------:|:-------------:|:---------------:|
| No log        | 1.0   | 449  | 0.1696          | 0.6061           | 0.3886        | 0.4635          |
| 0.653         | 2.0   | 898  | 0.0933          | 0.7231           | 0.4496        | 0.5415          |
| 0.2028        | 3.0   | 1347 | 0.0755          | 0.7481           | 0.462         | 0.5577          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2

---
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: mbart-large-50-many-to-many-mmt-finetuned-ar_AR-to-en_XX-finetuned-ar_AR-to-en_XX
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart-large-50-many-to-many-mmt-finetuned-ar_AR-to-en_XX-finetuned-ar_AR-to-en_XX

This model is a fine-tuned version of [Shamus/mbart-large-50-many-to-many-mmt-finetuned-ar_AR-to-en_XX](https://huggingface.co/Shamus/mbart-large-50-many-to-many-mmt-finetuned-ar_AR-to-en_XX) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1972
- Bleu: 30.3169
- Gen Len: 34.536

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| 1.122         | 1.0   | 2759 | 1.1972          | 30.3169 | 34.536  |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

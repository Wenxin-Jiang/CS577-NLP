---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- alex-apostolo/filtered-cuad
model-index:
- name: legal-bert-base-uncased-finetuned-filtered-cuad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# legal-bert-base-uncased-finetuned-filtered-cuad

This model is a fine-tuned version of [nlpaueb/legal-bert-base-uncased](https://huggingface.co/nlpaueb/legal-bert-base-uncased) on the filtered-cuad dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0436

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.0606        | 1.0   | 7312  | 0.0467          |
| 0.0379        | 2.0   | 14624 | 0.0455          |
| 0.0296        | 3.0   | 21936 | 0.0436          |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

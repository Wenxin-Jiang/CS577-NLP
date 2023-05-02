---
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: my_awesome_qa_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_awesome_qa_model

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on the squad dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4542

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
| No log        | 1.0   | 250  | 1.6813          |
| 2.1248        | 2.0   | 500  | 1.4503          |
| 2.1248        | 3.0   | 750  | 1.4542          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1

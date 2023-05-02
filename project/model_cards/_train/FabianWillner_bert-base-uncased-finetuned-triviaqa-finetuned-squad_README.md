---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad
model-index:
- name: bert-base-uncased-finetuned-triviaqa-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-triviaqa-finetuned-squad

This model is a fine-tuned version of [FabianWillner/bert-base-uncased-finetuned-triviaqa](https://huggingface.co/FabianWillner/bert-base-uncased-finetuned-triviaqa) on the squad dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9981

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.0184        | 1.0   | 5533  | 0.9733          |
| 0.7496        | 2.0   | 11066 | 0.9981          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
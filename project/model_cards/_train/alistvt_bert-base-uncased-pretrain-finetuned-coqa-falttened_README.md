---
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-pretrain-finetuned-coqa-falttened
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-pretrain-finetuned-coqa-falttened

This model is a fine-tuned version of [alistvt/bert-base-uncased-pretrained-mlm-coqa-stories](https://huggingface.co/alistvt/bert-base-uncased-pretrained-mlm-coqa-stories) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8655

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

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 3.2886        | 0.29  | 2000  | 3.0142          |
| 3.0801        | 0.59  | 4000  | 2.8347          |
| 2.9744        | 0.88  | 6000  | 2.7643          |
| 2.494         | 1.18  | 8000  | 2.7605          |
| 2.4417        | 1.47  | 10000 | 2.7790          |
| 2.4042        | 1.77  | 12000 | 2.7382          |
| 2.1285        | 2.06  | 14000 | 2.8588          |
| 2.0569        | 2.36  | 16000 | 2.8937          |
| 2.0794        | 2.65  | 18000 | 2.8511          |
| 2.0679        | 2.95  | 20000 | 2.8655          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3

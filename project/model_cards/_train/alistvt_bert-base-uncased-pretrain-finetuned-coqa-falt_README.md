---
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-pretrain-finetuned-coqa-falt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-pretrain-finetuned-coqa-falt

This model is a fine-tuned version of [alistvt/bert-base-uncased-pretrained-mlm-coqa-stories](https://huggingface.co/alistvt/bert-base-uncased-pretrained-mlm-coqa-stories) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8125

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 3.4039        | 0.29  | 2000  | 3.0921          |
| 3.1438        | 0.59  | 4000  | 2.8826          |
| 3.0252        | 0.88  | 6000  | 2.7885          |
| 2.7112        | 1.18  | 8000  | 2.7720          |
| 2.6703        | 1.47  | 10000 | 2.7581          |
| 2.6432        | 1.77  | 12000 | 2.7316          |
| 2.385         | 2.06  | 14000 | 2.7798          |
| 2.3314        | 2.36  | 16000 | 2.7836          |
| 2.3433        | 2.65  | 18000 | 2.7650          |
| 2.3604        | 2.95  | 20000 | 2.7585          |
| 2.2232        | 3.24  | 22000 | 2.8120          |
| 2.2094        | 3.53  | 24000 | 2.7945          |
| 2.2306        | 3.83  | 26000 | 2.8125          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.0
- Tokenizers 0.10.3

---
tags:
- generated_from_trainer
model-index:
- name: german-poetry-xlm-roberta
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# german-poetry-xlm-roberta

This model is a fine-tuned version of [xlm-roberta-large-finetuned-conll03-german](https://huggingface.co/xlm-roberta-large-finetuned-conll03-german) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8672

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 3.1984        | 1.0   | 2774  | 2.8507          |
| 2.7279        | 2.0   | 5548  | 2.5140          |
| 2.5236        | 3.0   | 8322  | 2.3583          |
| 2.4115        | 4.0   | 11096 | 2.2371          |
| 2.2953        | 5.0   | 13870 | 2.1773          |
| 2.2179        | 6.0   | 16644 | 2.1217          |
| 2.1652        | 7.0   | 19418 | 2.0483          |
| 2.1023        | 8.0   | 22192 | 2.0003          |
| 2.0532        | 9.0   | 24966 | 1.9961          |
| 2.0153        | 10.0  | 27740 | 1.9626          |
| 1.9657        | 11.0  | 30514 | 1.9310          |
| 1.9456        | 12.0  | 33288 | 1.9065          |
| 1.919         | 13.0  | 36062 | 1.8906          |
| 1.9077        | 14.0  | 38836 | 1.8712          |
| 1.9048        | 15.0  | 41610 | 1.8672          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

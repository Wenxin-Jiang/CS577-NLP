---
license: apache-2.0
datasets:
- null
model_index:
- name: dear-jarvis-v5
  results:
  - task:
      name: Text Classification
      type: text-classification
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dear-jarvis-v5

This model is a fine-tuned version of [distilbert-base-cased](https://huggingface.co/distilbert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3148

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 470  | 0.3106          |
| 0.3452        | 2.0   | 940  | 0.3064          |
| 0.2692        | 3.0   | 1410 | 0.3148          |


### Framework versions

- Transformers 4.7.0
- Pytorch 1.9.0+cu102
- Datasets 1.8.0
- Tokenizers 0.10.3

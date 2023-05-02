---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilroberta-base-finetuned-fakeNews
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilroberta-base-finetuned-fakeNews

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0355
- Accuracy: 0.9910

## Training and evaluation data

All of the process to train this model is available in this repository: https://github.com/G0nz4lo-4lvarez-H3rv4s/FakeNewsDetection
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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0301        | 1.0   | 1523 | 0.0322          | 0.9868   |
| 0.0165        | 2.0   | 3046 | 0.0292          | 0.9892   |
| 0.0088        | 3.0   | 4569 | 0.0355          | 0.9910   |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1

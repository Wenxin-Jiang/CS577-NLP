---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-finetuned-sentiment
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-sentiment

This model is a fine-tuned version of [nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4884
- Accuracy: 0.7698

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6778        | 1.0   | 722  | 0.7149          | 0.7482   |
| 0.3768        | 2.0   | 1444 | 0.9821          | 0.7410   |
| 0.1612        | 3.0   | 2166 | 1.4027          | 0.7662   |
| 0.094         | 4.0   | 2888 | 1.4884          | 0.7698   |
| 0.0448        | 5.0   | 3610 | 1.6463          | 0.7590   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1

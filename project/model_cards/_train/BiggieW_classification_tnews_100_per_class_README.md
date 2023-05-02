---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
widget:
- '全国高校科研质量排名，清华北大浙大无缘前五。'
model-index:
- name: classification_tnews_100_per_class
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# classification_tnews_100_per_class

This model is a fine-tuned version of [hfl/chinese-roberta-wwm-ext](https://huggingface.co/hfl/chinese-roberta-wwm-ext) on a subset of TNEWS dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0423
- Accuracy: 0.7133

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
- train_batch_size: 10
- eval_batch_size: 10
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.8994        | 1.0   | 150  | 1.2250          | 0.6733   |
| 0.9706        | 2.0   | 300  | 1.0644          | 0.6867   |
| 0.622         | 3.0   | 450  | 1.0083          | 0.6933   |
| 0.4115        | 4.0   | 600  | 1.0495          | 0.6867   |
| 0.2959        | 5.0   | 750  | 1.0423          | 0.7133   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

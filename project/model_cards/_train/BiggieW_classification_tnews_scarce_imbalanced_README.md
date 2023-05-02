---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
widget:
- '全国高校科研质量排名，清华北大浙大无缘前五。'
model-index:
- name: classification_tnews_scarce_imbalanced
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# classification_tnews_scarce_imbalanced

This model is a fine-tuned version of [hfl/chinese-roberta-wwm-ext](https://huggingface.co/hfl/chinese-roberta-wwm-ext) on a small&imbalanced subset of TNEWS dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8763
- Accuracy: 0.5867

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.7407        | 1.0   | 15   | 2.6972          | 0.1267   |
| 2.476         | 2.0   | 30   | 2.5490          | 0.2467   |
| 2.1124        | 3.0   | 45   | 2.4033          | 0.4067   |
| 1.8335        | 4.0   | 60   | 2.2475          | 0.4867   |
| 1.5516        | 5.0   | 75   | 2.1290          | 0.5333   |
| 1.3702        | 6.0   | 90   | 2.0374          | 0.5667   |
| 1.1347        | 7.0   | 105  | 1.9598          | 0.5733   |
| 1.1171        | 8.0   | 120  | 1.9145          | 0.58     |
| 0.9873        | 9.0   | 135  | 1.8869          | 0.5867   |
| 0.9644        | 10.0  | 150  | 1.8763          | 0.5867   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2

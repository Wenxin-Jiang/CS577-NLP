---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: correct_twitter_RoBERTa_token_itr0_1e-05_webDiscourse_01_03_2022-15_30_39
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# correct_twitter_RoBERTa_token_itr0_1e-05_webDiscourse_01_03_2022-15_30_39

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6169
- Precision: 0.0031
- Recall: 0.0357
- F1: 0.0057
- Accuracy: 0.6464

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 10   | 0.6339          | 0.0116    | 0.0120 | 0.0118 | 0.6662   |
| No log        | 2.0   | 20   | 0.6182          | 0.0064    | 0.0120 | 0.0084 | 0.6688   |
| No log        | 3.0   | 30   | 0.6139          | 0.0029    | 0.0241 | 0.0052 | 0.6659   |
| No log        | 4.0   | 40   | 0.6172          | 0.0020    | 0.0241 | 0.0037 | 0.6622   |
| No log        | 5.0   | 50   | 0.6165          | 0.0019    | 0.0241 | 0.0036 | 0.6599   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

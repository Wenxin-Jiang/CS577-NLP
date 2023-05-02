---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: sentence-transformers-msmarco-distilbert-base-tas-b-twitter_sentiment
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sentence-transformers-msmarco-distilbert-base-tas-b-twitter_sentiment

This model is a fine-tuned version of [sentence-transformers/msmarco-distilbert-base-tas-b](https://huggingface.co/sentence-transformers/msmarco-distilbert-base-tas-b) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6954
- Accuracy: 0.7146

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.8892        | 1.0   | 1387  | 0.8472          | 0.6180   |
| 0.7965        | 2.0   | 2774  | 0.7797          | 0.6609   |
| 0.7459        | 3.0   | 4161  | 0.7326          | 0.6872   |
| 0.7096        | 4.0   | 5548  | 0.7133          | 0.6995   |
| 0.6853        | 5.0   | 6935  | 0.6998          | 0.7002   |
| 0.6561        | 6.0   | 8322  | 0.6949          | 0.7059   |
| 0.663         | 7.0   | 9709  | 0.6956          | 0.7077   |
| 0.6352        | 8.0   | 11096 | 0.6890          | 0.7164   |
| 0.6205        | 9.0   | 12483 | 0.6888          | 0.7117   |
| 0.6203        | 10.0  | 13870 | 0.6871          | 0.7121   |
| 0.6005        | 11.0  | 15257 | 0.6879          | 0.7171   |
| 0.5985        | 12.0  | 16644 | 0.6870          | 0.7139   |
| 0.5839        | 13.0  | 18031 | 0.6882          | 0.7164   |
| 0.5861        | 14.0  | 19418 | 0.6910          | 0.7124   |
| 0.5732        | 15.0  | 20805 | 0.6916          | 0.7153   |
| 0.5797        | 16.0  | 22192 | 0.6947          | 0.7110   |
| 0.5565        | 17.0  | 23579 | 0.6930          | 0.7175   |
| 0.5636        | 18.0  | 24966 | 0.6959          | 0.7106   |
| 0.5642        | 19.0  | 26353 | 0.6952          | 0.7132   |
| 0.5717        | 20.0  | 27740 | 0.6954          | 0.7146   |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3

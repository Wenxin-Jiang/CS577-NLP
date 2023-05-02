---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-US_Airline_Twitter_Sentiment_Analysis
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-US_Airline_Twitter_Sentiment_Analysis

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5594
- Accuracy: 0.8466
- F1 Score: 0.8471

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
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Score |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.8015        | 1.0   | 92   | 0.5483          | 0.7952   | 0.8018   |
| 0.4795        | 2.0   | 184  | 0.4993          | 0.8233   | 0.8266   |
| 0.3995        | 3.0   | 276  | 0.5888          | 0.8205   | 0.8160   |
| 0.339         | 4.0   | 368  | 0.4935          | 0.8349   | 0.8350   |
| 0.2857        | 5.0   | 460  | 0.5100          | 0.8336   | 0.8370   |
| 0.2439        | 6.0   | 552  | 0.5275          | 0.8377   | 0.8400   |
| 0.2181        | 7.0   | 644  | 0.5463          | 0.8418   | 0.8426   |
| 0.1983        | 8.0   | 736  | 0.5594          | 0.8466   | 0.8471   |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1

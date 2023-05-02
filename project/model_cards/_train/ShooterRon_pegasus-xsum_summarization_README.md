---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: pegasus-xsum_summarization
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-xsum_summarization

This model is a fine-tuned version of [google/pegasus-xsum](https://huggingface.co/google/pegasus-xsum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7876
- Rouge1: 25.7148
- Rouge2: 10.9685
- Rougel: 21.6394
- Rougelsum: 22.3122

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 1.633         | 1.0   | 50   | 1.8839          | 24.9703 | 9.6517  | 19.9759 | 21.088    |
| 1.3917        | 2.0   | 100  | 1.8565          | 24.4395 | 9.1755  | 19.5702 | 20.5489   |
| 1.2576        | 3.0   | 150  | 1.8361          | 24.8266 | 10.2009 | 20.074  | 21.382    |
| 1.1191        | 4.0   | 200  | 1.8226          | 25.9635 | 11.7704 | 21.7787 | 22.365    |
| 1.1138        | 5.0   | 250  | 1.8239          | 26.7874 | 12.2832 | 22.7792 | 23.4501   |
| 1.0338        | 6.0   | 300  | 1.8094          | 26.3543 | 12.0501 | 22.3172 | 23.1194   |
| 1.0084        | 7.0   | 350  | 1.7923          | 25.5686 | 11.0213 | 21.5288 | 21.8892   |
| 1.0098        | 8.0   | 400  | 1.7876          | 25.7148 | 10.9685 | 21.6394 | 22.3122   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0
- Datasets 2.3.2
- Tokenizers 0.12.1

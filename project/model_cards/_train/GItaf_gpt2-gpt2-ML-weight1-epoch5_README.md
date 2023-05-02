---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-ML-weight1-epoch5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-ML-weight1-epoch5

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.5008
- Cls loss: 0.5177
- Lm loss: 3.9827
- Cls Accuracy: 0.6069
- Cls F1: 0.7986
- Cls Precision: 0.8382
- Cls Recall: 0.7988
- Perplexity: 53.66

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:-------:|:------------:|:------:|:-------------:|:----------:|:----------:|
| 4.6559        | 1.0   | 3470  | 4.4661          | 0.4247   | 4.0411  | 0.5827       | 0.7880 | 0.8440        | 0.7785     | 56.89      |
| 4.4053        | 2.0   | 6940  | 4.4125          | 0.4061   | 4.0061  | 0.6121       | 0.8008 | 0.8504        | 0.7923     | 54.93      |
| 4.292         | 3.0   | 10410 | 4.4590          | 0.4656   | 3.9930  | 0.6063       | 0.7981 | 0.8463        | 0.7927     | 54.22      |
| 4.2006        | 4.0   | 13880 | 4.4918          | 0.5056   | 3.9858  | 0.6058       | 0.7978 | 0.8399        | 0.7972     | 53.83      |
| 4.1427        | 5.0   | 17350 | 4.5008          | 0.5177   | 3.9827  | 0.6069       | 0.7986 | 0.8382        | 0.7988     | 53.66      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
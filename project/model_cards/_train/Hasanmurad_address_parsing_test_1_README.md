---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: address_parsing_test_1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# address_parsing_test_1

This model is a fine-tuned version of [csebuetnlp/banglabert](https://huggingface.co/csebuetnlp/banglabert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0207
- Precision: 0.9953
- Recall: 0.9957
- F1: 0.9955
- Accuracy: 0.9963

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0669        | 1.0   | 1266 | 0.0168          | 0.9890    | 0.9913 | 0.9902 | 0.9937   |
| 0.02          | 2.0   | 2532 | 0.0132          | 0.9953    | 0.9961 | 0.9957 | 0.9967   |
| 0.0122        | 3.0   | 3798 | 0.0177          | 0.9949    | 0.9955 | 0.9952 | 0.9962   |
| 0.0068        | 4.0   | 5064 | 0.0181          | 0.9951    | 0.9957 | 0.9954 | 0.9963   |
| 0.0048        | 5.0   | 6330 | 0.0207          | 0.9953    | 0.9957 | 0.9955 | 0.9963   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2

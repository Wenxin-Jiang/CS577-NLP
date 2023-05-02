---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-finetuned-removed-0529
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-removed-0529

This model is a fine-tuned version of [YeRyeongLee/bert-base-uncased-finetuned-0505-2](https://huggingface.co/YeRyeongLee/bert-base-uncased-finetuned-0505-2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1501
- Accuracy: 0.8767
- F1: 0.8765

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 3180  | 0.5072          | 0.8358   | 0.8373 |
| No log        | 2.0   | 6360  | 0.5335          | 0.8566   | 0.8564 |
| No log        | 3.0   | 9540  | 0.6317          | 0.8594   | 0.8603 |
| No log        | 4.0   | 12720 | 0.6781          | 0.8723   | 0.8727 |
| No log        | 5.0   | 15900 | 0.8235          | 0.8679   | 0.8682 |
| No log        | 6.0   | 19080 | 0.9205          | 0.8676   | 0.8674 |
| No log        | 7.0   | 22260 | 0.9898          | 0.8698   | 0.8695 |
| 0.2348        | 8.0   | 25440 | 1.0756          | 0.8695   | 0.8695 |
| 0.2348        | 9.0   | 28620 | 1.1342          | 0.8739   | 0.8735 |
| 0.2348        | 10.0  | 31800 | 1.1501          | 0.8767   | 0.8765 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.0
- Datasets 1.16.1
- Tokenizers 0.12.1

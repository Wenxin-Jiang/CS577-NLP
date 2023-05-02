---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: xlm-roberta-base-finetuned-TRAC-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-TRAC-DS

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0206
- Accuracy: 0.6814
- Precision: 0.6561
- Recall: 0.6528
- F1: 0.6543

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
- train_batch_size: 8
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9928        | 0.5   | 612  | 0.9026          | 0.6201   | 0.5845    | 0.5812 | 0.5809 |
| 0.8756        | 1.0   | 1224 | 0.7883          | 0.6373   | 0.6358    | 0.6382 | 0.6251 |
| 0.7793        | 1.5   | 1836 | 0.8551          | 0.6340   | 0.6226    | 0.6368 | 0.6020 |
| 0.7667        | 2.0   | 2448 | 0.7861          | 0.6618   | 0.6518    | 0.6637 | 0.6442 |
| 0.6619        | 2.5   | 3060 | 0.8597          | 0.6887   | 0.6662    | 0.6472 | 0.6503 |
| 0.6786        | 3.0   | 3672 | 0.7905          | 0.6634   | 0.6587    | 0.6658 | 0.6513 |
| 0.573         | 3.5   | 4284 | 0.9263          | 0.6797   | 0.6575    | 0.6488 | 0.6514 |
| 0.5805        | 4.0   | 4896 | 0.8351          | 0.6944   | 0.6719    | 0.6740 | 0.6723 |
| 0.5069        | 4.5   | 5508 | 0.9772          | 0.6748   | 0.6564    | 0.6572 | 0.6546 |
| 0.5085        | 5.0   | 6120 | 1.0206          | 0.6814   | 0.6561    | 0.6528 | 0.6543 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1

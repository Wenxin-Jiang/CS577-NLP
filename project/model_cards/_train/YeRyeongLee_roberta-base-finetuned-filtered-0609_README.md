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
- name: roberta-base-finetuned-filtered-0609
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-filtered-0609

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1343
- Accuracy: 0.9824
- Precision: 0.9824
- Recall: 0.9824
- F1: 0.9824

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

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.1817        | 1.0   | 3180  | 0.1883          | 0.9651   | 0.9654    | 0.9651 | 0.9651 |
| 0.1647        | 2.0   | 6360  | 0.1264          | 0.9777   | 0.9778    | 0.9777 | 0.9777 |
| 0.1295        | 3.0   | 9540  | 0.1514          | 0.9723   | 0.9724    | 0.9723 | 0.9723 |
| 0.0991        | 4.0   | 12720 | 0.1487          | 0.9761   | 0.9763    | 0.9761 | 0.9761 |
| 0.0749        | 5.0   | 15900 | 0.1119          | 0.9802   | 0.9802    | 0.9802 | 0.9802 |
| 0.0532        | 6.0   | 19080 | 0.1357          | 0.9789   | 0.9790    | 0.9789 | 0.9789 |
| 0.0471        | 7.0   | 22260 | 0.1397          | 0.9780   | 0.9782    | 0.9780 | 0.9780 |
| 0.0153        | 8.0   | 25440 | 0.1568          | 0.9777   | 0.9778    | 0.9777 | 0.9777 |
| 0.0147        | 9.0   | 28620 | 0.1274          | 0.9824   | 0.9824    | 0.9824 | 0.9824 |
| 0.0135        | 10.0  | 31800 | 0.1343          | 0.9824   | 0.9824    | 0.9824 | 0.9824 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.1+cu111
- Datasets 1.16.1
- Tokenizers 0.12.1

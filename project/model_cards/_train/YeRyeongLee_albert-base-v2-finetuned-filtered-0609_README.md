---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: albert-base-v2-finetuned-filtered-0609
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-v2-finetuned-filtered-0609

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2062
- Accuracy: 0.9723
- Precision: 0.9724
- Recall: 0.9723
- F1: 0.9723

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
| 0.2688        | 1.0   | 3180  | 0.2282          | 0.9560   | 0.9577    | 0.9560 | 0.9562 |
| 0.2268        | 2.0   | 6360  | 0.1909          | 0.9638   | 0.9640    | 0.9638 | 0.9638 |
| 0.1831        | 3.0   | 9540  | 0.2590          | 0.9572   | 0.9584    | 0.9572 | 0.9572 |
| 0.1588        | 4.0   | 12720 | 0.1752          | 0.9673   | 0.9678    | 0.9673 | 0.9673 |
| 0.0972        | 5.0   | 15900 | 0.1868          | 0.9695   | 0.9696    | 0.9695 | 0.9695 |
| 0.0854        | 6.0   | 19080 | 0.2042          | 0.9701   | 0.9707    | 0.9701 | 0.9702 |
| 0.0599        | 7.0   | 22260 | 0.1793          | 0.9748   | 0.9749    | 0.9748 | 0.9749 |
| 0.0389        | 8.0   | 25440 | 0.1996          | 0.9742   | 0.9743    | 0.9742 | 0.9742 |
| 0.0202        | 9.0   | 28620 | 0.2188          | 0.9723   | 0.9726    | 0.9723 | 0.9724 |
| 0.0152        | 10.0  | 31800 | 0.2062          | 0.9723   | 0.9724    | 0.9723 | 0.9723 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.1+cu111
- Datasets 1.16.1
- Tokenizers 0.12.1

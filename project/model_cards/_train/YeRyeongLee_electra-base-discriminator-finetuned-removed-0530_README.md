---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: electra-base-discriminator-finetuned-removed-0530
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# electra-base-discriminator-finetuned-removed-0530

This model is a fine-tuned version of [google/electra-base-discriminator](https://huggingface.co/google/electra-base-discriminator) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9713
- Accuracy: 0.8824
- F1: 0.8824

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
| No log        | 1.0   | 3180  | 0.6265          | 0.8107   | 0.8128 |
| No log        | 2.0   | 6360  | 0.5158          | 0.8544   | 0.8541 |
| No log        | 3.0   | 9540  | 0.6686          | 0.8563   | 0.8567 |
| No log        | 4.0   | 12720 | 0.6491          | 0.8711   | 0.8709 |
| No log        | 5.0   | 15900 | 0.8048          | 0.8660   | 0.8672 |
| No log        | 6.0   | 19080 | 0.8110          | 0.8708   | 0.8710 |
| No log        | 7.0   | 22260 | 1.0082          | 0.8651   | 0.8640 |
| 0.2976        | 8.0   | 25440 | 0.8343          | 0.8811   | 0.8814 |
| 0.2976        | 9.0   | 28620 | 0.9366          | 0.8780   | 0.8780 |
| 0.2976        | 10.0  | 31800 | 0.9713          | 0.8824   | 0.8824 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.0
- Datasets 1.16.1
- Tokenizers 0.12.1

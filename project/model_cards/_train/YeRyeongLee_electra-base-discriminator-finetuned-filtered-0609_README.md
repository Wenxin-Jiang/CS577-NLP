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
- name: electra-base-discriminator-finetuned-filtered-0609
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# electra-base-discriminator-finetuned-filtered-0609

This model is a fine-tuned version of [google/electra-base-discriminator](https://huggingface.co/google/electra-base-discriminator) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1933
- Accuracy: 0.9745
- Precision: 0.9747
- Recall: 0.9745
- F1: 0.9746

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
| 0.238         | 1.0   | 3180  | 0.1861          | 0.9682   | 0.9686    | 0.9682 | 0.9682 |
| 0.1827        | 2.0   | 6360  | 0.2262          | 0.9645   | 0.9648    | 0.9645 | 0.9644 |
| 0.1326        | 3.0   | 9540  | 0.1904          | 0.9711   | 0.9716    | 0.9711 | 0.9712 |
| 0.1575        | 4.0   | 12720 | 0.2065          | 0.9676   | 0.9680    | 0.9676 | 0.9676 |
| 0.1224        | 5.0   | 15900 | 0.2666          | 0.9557   | 0.9571    | 0.9557 | 0.9558 |
| 0.1083        | 6.0   | 19080 | 0.1697          | 0.9752   | 0.9754    | 0.9752 | 0.9752 |
| 0.0792        | 7.0   | 22260 | 0.1684          | 0.9742   | 0.9744    | 0.9742 | 0.9742 |
| 0.0751        | 8.0   | 25440 | 0.1784          | 0.9723   | 0.9726    | 0.9723 | 0.9723 |
| 0.0572        | 9.0   | 28620 | 0.1868          | 0.9736   | 0.9737    | 0.9736 | 0.9736 |
| 0.0593        | 10.0  | 31800 | 0.1933          | 0.9745   | 0.9747    | 0.9745 | 0.9746 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.1+cu111
- Datasets 1.16.1
- Tokenizers 0.12.1

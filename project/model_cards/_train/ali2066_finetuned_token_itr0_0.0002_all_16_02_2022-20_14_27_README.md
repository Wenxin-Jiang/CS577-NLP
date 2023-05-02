---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: finetuned_token_itr0_0.0002_all_16_02_2022-20_14_27
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_0.0002_all_16_02_2022-20_14_27

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1588
- Precision: 0.4510
- Recall: 0.5622
- F1: 0.5005
- Accuracy: 0.9477

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 38   | 0.2896          | 0.1483    | 0.1981 | 0.1696 | 0.8745   |
| No log        | 2.0   | 76   | 0.2553          | 0.2890    | 0.3604 | 0.3207 | 0.8918   |
| No log        | 3.0   | 114  | 0.2507          | 0.246     | 0.4642 | 0.3216 | 0.8925   |
| No log        | 4.0   | 152  | 0.2540          | 0.2428    | 0.4792 | 0.3223 | 0.8922   |
| No log        | 5.0   | 190  | 0.2601          | 0.2747    | 0.4717 | 0.3472 | 0.8965   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3

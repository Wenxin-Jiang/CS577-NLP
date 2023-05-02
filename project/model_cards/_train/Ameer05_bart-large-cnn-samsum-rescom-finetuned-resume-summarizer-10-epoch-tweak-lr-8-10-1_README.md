---
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-cnn-samsum-rescom-finetuned-resume-summarizer-10-epoch-tweak-lr-8-10-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-samsum-rescom-finetuned-resume-summarizer-10-epoch-tweak-lr-8-10-1

This model is a fine-tuned version of [Ameer05/model-token-repo](https://huggingface.co/Ameer05/model-token-repo) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4855
- Rouge1: 58.3832
- Rouge2: 49.9973
- Rougel: 55.3055
- Rougelsum: 57.7139

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| No log        | 0.91  | 5    | 2.0183          | 52.3098 | 45.5304 | 49.2759 | 51.7456   |
| No log        | 1.91  | 10   | 1.6564          | 61.815  | 53.9035 | 58.4243 | 60.784    |
| No log        | 2.91  | 15   | 1.5330          | 61.3032 | 54.12   | 58.9152 | 60.7178   |
| No log        | 3.91  | 20   | 1.4539          | 63.3012 | 56.2987 | 61.0907 | 62.5217   |
| 1.5646        | 4.91  | 25   | 1.4578          | 62.4815 | 55.1453 | 60.3921 | 61.6067   |
| 1.5646        | 5.91  | 30   | 1.4284          | 61.5347 | 54.1271 | 58.8474 | 60.5427   |
| 1.5646        | 6.91  | 35   | 1.4467          | 61.5081 | 53.8512 | 59.2782 | 60.6928   |
| 1.5646        | 7.91  | 40   | 1.4653          | 59.5349 | 51.8208 | 56.5996 | 58.8211   |
| 0.6692        | 8.91  | 45   | 1.4740          | 57.2917 | 49.5416 | 54.8409 | 56.6276   |
| 0.6692        | 9.91  | 50   | 1.4855          | 58.3832 | 49.9973 | 55.3055 | 57.7139   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.9.1
- Datasets 1.18.4
- Tokenizers 0.10.3

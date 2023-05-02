---
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-cnn-samsum-rescom-finetuned-resume-summarizer-9-epoch-tweak
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-samsum-rescom-finetuned-resume-summarizer-9-epoch-tweak

This model is a fine-tuned version of [Ameer05/model-token-repo](https://huggingface.co/Ameer05/model-token-repo) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4511
- Rouge1: 59.76
- Rouge2: 52.1999
- Rougel: 57.3631
- Rougelsum: 59.3075

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
- num_epochs: 9
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| No log        | 0.91  | 5    | 2.0185          | 52.2186 | 45.4675 | 49.3152 | 51.9415   |
| No log        | 1.91  | 10   | 1.6571          | 60.7728 | 52.8611 | 57.3487 | 60.1676   |
| No log        | 2.91  | 15   | 1.5323          | 60.5674 | 52.2246 | 57.9846 | 60.073    |
| No log        | 3.91  | 20   | 1.4556          | 61.2167 | 53.5087 | 58.9609 | 60.893    |
| 1.566         | 4.91  | 25   | 1.4632          | 62.918  | 55.4544 | 60.7116 | 62.6614   |
| 1.566         | 5.91  | 30   | 1.4360          | 60.4173 | 52.5859 | 57.8131 | 59.8864   |
| 1.566         | 6.91  | 35   | 1.4361          | 61.4273 | 53.9663 | 59.4445 | 60.9672   |
| 1.566         | 7.91  | 40   | 1.4477          | 60.3401 | 52.7276 | 57.7504 | 59.8209   |
| 0.6928        | 8.91  | 45   | 1.4511          | 59.76   | 52.1999 | 57.3631 | 59.3075   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.9.1
- Datasets 1.18.4
- Tokenizers 0.10.3

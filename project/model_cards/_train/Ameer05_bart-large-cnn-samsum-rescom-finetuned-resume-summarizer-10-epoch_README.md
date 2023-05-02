---
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-cnn-samsum-rescom-finetuned-resume-summarizer-10-epoch
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-samsum-rescom-finetuned-resume-summarizer-10-epoch

This model is a fine-tuned version of [Ameer05/model-token-repo](https://huggingface.co/Ameer05/model-token-repo) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5216
- Rouge1: 59.5791
- Rouge2: 51.3273
- Rougel: 56.9984
- Rougelsum: 59.1424

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
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
| No log        | 0.91  | 5    | 2.0124          | 53.776  | 46.7427 | 50.7565 | 53.5502   |
| No log        | 1.91  | 10   | 1.6353          | 61.8019 | 53.8614 | 58.9744 | 61.339    |
| No log        | 2.91  | 15   | 1.5321          | 59.7045 | 51.5968 | 57.0823 | 59.2417   |
| No log        | 3.91  | 20   | 1.4569          | 62.4379 | 54.5464 | 59.9202 | 61.9242   |
| 1.5608        | 4.91  | 25   | 1.4613          | 63.3808 | 55.8818 | 61.432  | 63.0208   |
| 1.5608        | 5.91  | 30   | 1.4321          | 59.6761 | 50.9812 | 56.7977 | 59.1214   |
| 1.5608        | 6.91  | 35   | 1.4753          | 62.6439 | 54.7158 | 60.3831 | 62.1046   |
| 1.5608        | 7.91  | 40   | 1.4783          | 60.2735 | 52.7462 | 57.77   | 59.9725   |
| 0.6428        | 8.91  | 45   | 1.4974          | 62.8691 | 54.9062 | 60.3496 | 62.5132   |
| 0.6428        | 9.91  | 50   | 1.5216          | 59.5791 | 51.3273 | 56.9984 | 59.1424   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.9.1
- Datasets 1.18.4
- Tokenizers 0.10.3

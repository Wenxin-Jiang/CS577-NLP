---
license: mit
tags:
- generated_from_trainer
widget:
- text: "I feel so low and numb, don't feel like doing anything. Just passing my days"
- text: "Sleep is my greatest and most comforting escape whenever I wake up these days. The literal very first emotion I feel is just misery and reminding myself of all my problems."
- text: "I went to a movie today. It was below my expectations but the day was fine."
- text: "The first day of work was a little hectic but met pretty good colleagues, we went for a team dinner party at the end of the day."

metrics:
- accuracy
model-index:
- name: finetuned-roberta-depression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-roberta-depression

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1385
- Accuracy: 0.9745

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
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0238        | 1.0   | 625  | 0.1385          | 0.9745   |
| 0.0333        | 2.0   | 1250 | 0.1385          | 0.9745   |
| 0.0263        | 3.0   | 1875 | 0.1385          | 0.9745   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

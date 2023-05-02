---
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: bertweet-base-finetuned-filtered-0609
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertweet-base-finetuned-filtered-0609

This model is a fine-tuned version of [vinai/bertweet-base](https://huggingface.co/vinai/bertweet-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5397
- Accuracy: 0.9299
- Precision: 0.9297
- Recall: 0.9299
- F1: 0.9298

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
| 0.331         | 1.0   | 3180  | 0.3687          | 0.9069   | 0.9147    | 0.9069 | 0.9081 |
| 0.2611        | 2.0   | 6360  | 0.3725          | 0.9223   | 0.9227    | 0.9223 | 0.9224 |
| 0.1993        | 3.0   | 9540  | 0.2948          | 0.9336   | 0.9350    | 0.9336 | 0.9339 |
| 0.1648        | 4.0   | 12720 | 0.3563          | 0.9296   | 0.9303    | 0.9296 | 0.9298 |
| 0.1324        | 5.0   | 15900 | 0.4136          | 0.9267   | 0.9279    | 0.9267 | 0.9270 |
| 0.1102        | 6.0   | 19080 | 0.4060          | 0.9352   | 0.9357    | 0.9352 | 0.9353 |
| 0.0568        | 7.0   | 22260 | 0.4653          | 0.9321   | 0.9328    | 0.9321 | 0.9322 |
| 0.0292        | 8.0   | 25440 | 0.4818          | 0.9311   | 0.9310    | 0.9311 | 0.9310 |
| 0.0155        | 9.0   | 28620 | 0.5405          | 0.9286   | 0.9288    | 0.9286 | 0.9286 |
| 0.0095        | 10.0  | 31800 | 0.5397          | 0.9299   | 0.9297    | 0.9299 | 0.9298 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.1+cu111
- Datasets 1.16.1
- Tokenizers 0.12.1

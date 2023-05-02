---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-TF-weight1-epoch15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-TF-weight1-epoch15

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 6.0647
- Cls loss: 2.1295
- Lm loss: 3.9339
- Cls Accuracy: 0.8375
- Cls F1: 0.8368
- Cls Precision: 0.8381
- Cls Recall: 0.8375
- Perplexity: 51.11

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Cls loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Lm loss | Perplexity | Validation Loss |
|:-------------:|:-----:|:-----:|:--------:|:------------:|:------:|:-------------:|:----------:|:-------:|:----------:|:---------------:|
| 4.8702        | 1.0   | 3470  | 0.6951   | 0.7752       | 0.7670 | 0.7978        | 0.7752     | 4.0201  | 55.71      | 4.7157          |
| 4.5856        | 2.0   | 6940  | 0.6797   | 0.8352       | 0.8333 | 0.8406        | 0.8352     | 3.9868  | 53.88      | 4.6669          |
| 4.4147        | 3.0   | 10410 | 0.6899   | 0.8375       | 0.8368 | 0.8384        | 0.8375     | 3.9716  | 53.07      | 4.6619          |
| 4.2479        | 4.0   | 13880 | 0.8678   | 0.8403       | 0.8396 | 0.8413        | 0.8403     | 3.9622  | 52.57      | 4.8305          |
| 4.1281        | 5.0   | 17350 | 0.9747   | 0.8340       | 0.8334 | 0.8346        | 0.8340     | 3.9596  | 52.44      | 4.9349          |


| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity| 
|:-------------:|:-----:|:-----:|:--------:|:------------:|:------:|:-------------:|:----------:|:-------:|:----------:|:---------------:|
| 4.195         | 6.0   | 20820 | 4.9303   | 0.9770       | 3.9528 | 0.8300        | 0.8299     | 0.8299  | 0.8300     | 52.08           |
| 4.0645        | 7.0   | 24290 | 5.0425   | 1.0979       | 3.9440 | 0.8317        | 0.8313     | 0.8317  | 0.8317     | 51.62           |
| 3.9637        | 8.0   | 27760 | 5.3955   | 1.4533       | 3.9414 | 0.8329        | 0.8325     | 0.8328  | 0.8329     | 51.49           |
| 3.9094        | 9.0   | 31230 | 5.6029   | 1.6645       | 3.9375 | 0.8231        | 0.8233     | 0.8277  | 0.8231     | 51.29           |
| 3.8661        | 10.0  | 34700 | 5.8175   | 1.8821       | 3.9344 | 0.8144        | 0.8115     | 0.8222  | 0.8144     | 51.13           |
| 3.8357        | 11.0  | 38170 | 5.6824   | 1.7494       | 3.9319 | 0.8340        | 0.8336     | 0.8342  | 0.8340     | 51.01           |
| 3.8019        | 12.0  | 41640 | 5.8509   | 1.9167       | 3.9332 | 0.8369        | 0.8357     | 0.8396  | 0.8369     | 51.07           |
| 3.7815        | 13.0  | 45110 | 5.9044   | 1.9686       | 3.9346 | 0.8409        | 0.8407     | 0.8408  | 0.8409     | 51.14           |
| 3.7662        | 14.0  | 48580 | 6.0088   | 2.0738       | 3.9337 | 0.8363        | 0.8359     | 0.8364  | 0.8363     | 51.10           |
| 3.7524        | 15.0  | 52050 | 6.0647   | 2.1295       | 3.9339 | 0.8375        | 0.8368     | 0.8381  | 0.8375     | 51.11           |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
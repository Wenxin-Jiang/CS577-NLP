---
license: mit
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-cnn-samsum-whole_summary_chatGPT_and_tweetsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-samsum-whole_summary_chatGPT_and_tweetsum

This model is a fine-tuned version of [philschmid/bart-large-cnn-samsum](https://huggingface.co/philschmid/bart-large-cnn-samsum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 5.1747
- Rouge1: 22.1238
- Rouge2: 7.5755
- Rougel: 15.8539
- Rougelsum: 18.8483
- Gen Len: 62.2

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 397  | 2.3879          | 19.7449 | 8.1533  | 16.4998 | 17.8335   | 62.0    |
| 1.9889        | 2.0   | 794  | 2.6982          | 21.8787 | 12.2713 | 19.5273 | 19.3784   | 63.6    |
| 1.0298        | 3.0   | 1191 | 2.8150          | 20.3414 | 9.8563  | 16.7994 | 16.7994   | 61.0    |
| 0.52          | 4.0   | 1588 | 3.2921          | 19.5424 | 7.94    | 15.3118 | 17.1955   | 60.8    |
| 0.52          | 5.0   | 1985 | 3.4467          | 17.0802 | 5.6269  | 13.365  | 13.365    | 61.8    |
| 0.3114        | 6.0   | 2382 | 4.3416          | 23.5849 | 10.5415 | 17.8904 | 19.7952   | 59.2    |
| 0.1644        | 7.0   | 2779 | 4.7510          | 20.4712 | 8.7588  | 15.7973 | 18.1441   | 61.8    |
| 0.0814        | 8.0   | 3176 | 4.5738          | 22.4661 | 8.1775  | 15.6491 | 16.9007   | 60.0    |
| 0.045         | 9.0   | 3573 | 5.1804          | 23.1379 | 7.3984  | 16.6129 | 17.7338   | 62.6    |
| 0.045         | 10.0  | 3970 | 5.1747          | 22.1238 | 7.5755  | 15.8539 | 18.8483   | 62.2    |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.12.1

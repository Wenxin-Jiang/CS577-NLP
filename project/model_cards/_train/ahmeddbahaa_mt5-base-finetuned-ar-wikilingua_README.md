---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- wiki_lingua
model-index:
- name: mt5-base-finetuned-ar-wikilingua
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-finetuned-ar-wikilingua

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the wiki_lingua dataset.
It achieves the following results on the evaluation set:
- Loss: 3.6790
- Rouge-1: 19.46
- Rouge-2: 6.82
- Rouge-l: 17.57
- Gen Len: 18.83
- Bertscore: 70.18

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge-1 | Rouge-2 | Rouge-l | Gen Len | Bertscore |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:-------:|:---------:|
| 4.9783        | 1.0   | 5111  | 4.0107          | 15.8    | 4.65    | 14.18   | 18.98   | 68.66     |
| 4.2093        | 2.0   | 10222 | 3.8664          | 16.46   | 5.17    | 15.08   | 18.91   | 68.5      |
| 4.0303        | 3.0   | 15333 | 3.7847          | 17.0    | 5.43    | 15.45   | 18.89   | 68.75     |
| 3.9165        | 4.0   | 20444 | 3.7405          | 17.03   | 5.5     | 15.45   | 18.86   | 68.78     |
| 3.8396        | 5.0   | 25555 | 3.7102          | 17.14   | 5.57    | 15.48   | 18.87   | 68.92     |
| 3.7825        | 6.0   | 30666 | 3.6944          | 17.64   | 5.73    | 15.96   | 18.82   | 69.14     |
| 3.7447        | 7.0   | 35777 | 3.6801          | 17.6    | 5.66    | 15.9    | 18.78   | 69.23     |
| 3.7203        | 8.0   | 40888 | 3.6790          | 17.94   | 5.81    | 16.21   | 18.81   | 69.29     |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1

---
tags:
- summarization
- ar
- encoder-decoder
- arabert
- arabert2arabert
- Abstractive Summarization
- generated_from_trainer
datasets:
- wiki_lingua
model-index:
- name: arabert2arabert-finetuned-ar-wikilingua
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# arabert2arabert-finetuned-ar-wikilingua

This model is a fine-tuned version of [](https://huggingface.co/) on the wiki_lingua dataset.
It achieves the following results on the evaluation set:
- Loss: 4.6877
- Rouge-1: 13.2
- Rouge-2: 3.43
- Rouge-l: 12.45
- Gen Len: 20.0
- Bertscore: 64.88

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
- gradient_accumulation_steps: 16
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge-1 | Rouge-2 | Rouge-l | Gen Len | Bertscore |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:-------:|:---------:|
| 6.7667        | 1.0   | 156  | 5.3846          | 3.36    | 0.56    | 3.27    | 20.0    | 60.6      |
| 5.257         | 2.0   | 312  | 5.0424          | 5.44    | 0.88    | 5.35    | 20.0    | 60.56     |
| 4.743         | 3.0   | 468  | 4.8294          | 9.21    | 1.8     | 8.93    | 20.0    | 62.91     |
| 4.3832        | 4.0   | 624  | 4.7240          | 9.88    | 2.19    | 9.6     | 20.0    | 62.65     |
| 4.1166        | 5.0   | 780  | 4.6861          | 11.61   | 2.86    | 11.13   | 20.0    | 63.71     |
| 3.91          | 6.0   | 936  | 4.6692          | 12.27   | 3.11    | 11.76   | 20.0    | 64.07     |
| 3.7569        | 7.0   | 1092 | 4.6805          | 12.93   | 3.38    | 12.28   | 20.0    | 64.61     |
| 3.6454        | 8.0   | 1248 | 4.6877          | 13.2    | 3.43    | 12.45   | 20.0    | 64.88     |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

---
tags:
- summarization
- ar
- encoder-decoder
- roberta
- xlmroberta2xlmroberta
- Abstractive Summarization
- generated_from_trainer
datasets:
- wiki_lingua
model-index:
- name: xlmroberta2xlmroberta-finetuned-ar-wikilingua
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlmroberta2xlmroberta-finetuned-ar-wikilingua

This model is a fine-tuned version of [](https://huggingface.co/) on the wiki_lingua dataset.
It achieves the following results on the evaluation set:
- Loss: 4.7757
- Rouge-1: 11.2
- Rouge-2: 1.96
- Rouge-l: 10.28
- Gen Len: 19.8
- Bertscore: 66.27

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
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 10
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge-1 | Rouge-2 | Rouge-l | Gen Len | Bertscore |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:-------:|:---------:|
| 8.03          | 1.0   | 312  | 7.3208          | 0.19    | 0.0     | 0.19    | 20.0    | 54.84     |
| 7.2309        | 2.0   | 624  | 7.1107          | 1.17    | 0.03    | 1.16    | 20.0    | 60.0      |
| 7.0752        | 3.0   | 936  | 7.0061          | 2.58    | 0.15    | 2.55    | 20.0    | 63.52     |
| 6.7538        | 4.0   | 1248 | 6.4189          | 5.75    | 0.46    | 5.55    | 19.95   | 62.83     |
| 6.1513        | 5.0   | 1560 | 5.8402          | 8.46    | 1.04    | 8.08    | 19.2    | 64.25     |
| 5.6639        | 6.0   | 1872 | 5.3938          | 8.62    | 1.17    | 8.16    | 19.28   | 64.81     |
| 5.2857        | 7.0   | 2184 | 5.0719          | 9.34    | 1.41    | 8.61    | 19.71   | 65.29     |
| 5.027         | 8.0   | 2496 | 4.9047          | 10.42   | 1.52    | 9.57    | 19.57   | 65.75     |
| 4.8747        | 9.0   | 2808 | 4.8032          | 10.79   | 1.71    | 9.91    | 19.42   | 66.2      |
| 4.7855        | 10.0  | 3120 | 4.7757          | 11.01   | 1.73    | 10.04   | 19.55   | 66.24     |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

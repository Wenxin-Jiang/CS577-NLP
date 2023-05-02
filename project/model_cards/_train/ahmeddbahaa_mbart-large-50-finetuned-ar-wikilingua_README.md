---
tags:
- summarization
- generated_from_trainer
datasets:
- wiki_lingua
model-index:
- name: mbart-large-50-finetuned-ar-wikilingua
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart-large-50-finetuned-ar-wikilingua

This model is a fine-tuned version of [facebook/mbart-large-50](https://huggingface.co/facebook/mbart-large-50) on the wiki_lingua dataset.
It achieves the following results on the evaluation set:
- Loss: 4.0001
- Rouge-1: 22.11
- Rouge-2: 7.33
- Rouge-l: 19.75
- Gen Len: 59.4
- Bertscore: 68.9

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
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
| 5.2671        | 1.0   | 5111  | 4.6414          | 18.37   | 5.63    | 16.32   | 96.39   | 65.12     |
| 4.5375        | 2.0   | 10222 | 4.3144          | 20.49   | 6.64    | 18.35   | 95.44   | 65.79     |
| 4.308         | 3.0   | 15333 | 4.1592          | 21.16   | 7.09    | 18.85   | 67.75   | 67.65     |
| 4.1562        | 4.0   | 20444 | 4.0812          | 21.59   | 7.31    | 19.42   | 68.66   | 68.02     |
| 4.0749        | 5.0   | 25555 | 4.0409          | 21.99   | 7.42    | 19.82   | 66.4    | 68.05     |
| 4.0271        | 6.0   | 30666 | 4.0183          | 22.04   | 7.42    | 19.64   | 56.88   | 68.95     |
| 3.9991        | 7.0   | 35777 | 4.0042          | 22.05   | 7.35    | 19.71   | 55.75   | 68.94     |
| 3.9833        | 8.0   | 40888 | 4.0001          | 22.12   | 7.39    | 19.78   | 55.72   | 69.0      |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1

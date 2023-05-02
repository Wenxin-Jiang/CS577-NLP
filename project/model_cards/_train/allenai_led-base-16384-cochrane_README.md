---
language: en
tags:
- generated_from_trainer
datasets:
- allenai/mslr2022
model-index:
- name: baseline
  results: []
---

# Overview

This model is a fine-tuned version of [allenai/led-base-16384](https://huggingface.co/allenai/led-base-16384) on the [Cochrane](https://github.com/allenai/mslr-shared-task#cochrane-dataset) dataset. The model received as input the titles and abstracts of up to 25 included studies for each example, concatenated by the `"</s>"` token. Global attention is applied to the special start token `"<s>"` and each of the document separator tokens `"</s>"`. The model slightly outperforms the reported results in the original paper: [MS2: Multi-Document Summarization of Medical Studies](https://arxiv.org/abs/2104.06486). See the [Cochrane leaderboard](https://leaderboard.allenai.org/mslr-cochrane/submissions/public) for results on the blind test set. 

It achieves the following results on the `validation` set:

- Loss: 4.0216
- Rouge1 Fmeasure Mean: 26.3026
- Rouge2 Fmeasure Mean: 6.0324
- Rougel Fmeasure Mean: 18.1513
- Rougelsum Fmeasure Mean: 22.5031
- Bertscore Hashcode: microsoft/deberta-xlarge-mnli_L40_no-idf_version=0.3.11(hug_trans=4.22.0.dev0)-rescaled_fast-tokenizer
- Bertscore F1 Mean: 20.5937
- Seed: 42
- Model Name Or Path: allenai/led-base-16384
- Doc Sep Token: `"</s>"`

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 20
- mixed_precision_training: Native AMP
- label_smoothing_factor: 0.1

### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.0
- Datasets 2.4.0
- Tokenizers 0.12.1

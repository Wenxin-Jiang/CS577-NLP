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

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Overview

This model is a fine-tuned version of [allenai/led-base-16384](https://huggingface.co/allenai/led-base-16384) on the [MS^2](https://github.com/allenai/mslr-shared-task#ms2-dataset) dataset. The model received as input the background section and the titles and abstracts of up to 25 included studies for each example, concatenated by the `"</s>"` token. Global attention is applied to the special start token `"<s>"` and each of the document separator tokens `"</s>"`. The model slightly outperforms the reported results in the original paper: [MS2: Multi-Document Summarization of Medical Studies](https://arxiv.org/abs/2104.06486). See the [MS2 leaderboard](https://leaderboard.allenai.org/mslr-ms2/submissions/public) for results on the blind test set. 

It achieves the following results on the evaluation set:
- Loss: 3.7602
- Rouge1 Fmeasure Mean: 28.5338
- Rouge2 Fmeasure Mean: 9.5060
- RougeL Fmeasure Mean: 20.9321
- RougeLsum Fmeasure Mean: 24.0998
- Bertscore Hashcode: microsoft/deberta-xlarge-mnli_L40_no-idf_version=0.3.11(hug_trans=4.21.0.dev0)-rescaled_fast-tokenizer
- Bertscore F1 Mean: 22.7619
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
- num_epochs: 10
- mixed_precision_training: Native AMP
- label_smoothing_factor: 0.1

### Framework versions

- Transformers 4.21.0.dev0
- Pytorch 1.10.0
- Datasets 2.4.0
- Tokenizers 0.12.1

---
tags:
- generated_from_trainer
- seq2seq
model-index:
- name: codebert-gpt2-commitgen
  results: []
language:
- en
metrics:
- rouge
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# codebert-gpt2-commitgen

This model is a fine-tuned version [](https://huggingface.co/) on  dataset provided in the paper titled "Towards Automatic Generation of Short Summaries of Commits" by 
Siyuan Jiang and Collin McMillan. 
Heres are the links

Paper :https://arxiv.org/abs/1708.09492
Data : https://sjiang1.github.io/commitgen

## Model description

This is a sequence2sequence model with microsoft/codebert-base as encoder and gpt2 as decoder. Givena gitdiff file, this model can generate a short commit message summarizing the change.


## Intended uses & limitations

The intended use is to automate github commit message. One limitation to consider is that the model can generate a summary of changes, but is only confined to type of change and might not be able to provide details about the change or output specific keywords related to change. 

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 3

### Training results

- global_step=4521
- training_loss=3.55994465065804
- train_runtime: 3300.0492
- train_samples_per_second: 21.919
- train_steps_per_second: 1.37
- total_flos: 1.062667587499776e+16
- train_loss: 3.55994465065804

### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2
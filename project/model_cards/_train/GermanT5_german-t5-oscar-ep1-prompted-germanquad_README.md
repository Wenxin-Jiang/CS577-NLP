---
tags:
- generated_from_trainer
widget:
 - text: |
     Philipp ist 26 Jahre alt und lebt in Nürnberg, Deutschland. Derzeit arbeitet er als Machine Learning Engineer und Tech Lead bei Hugging Face, um künstliche Intelligenz durch Open Source und Open Science zu demokratisieren.
     
     Welches Ziel hat Hugging Face?
model-index:
- name: test-german-t5-prompted-germanquad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test-german-t5-prompted-germanquad

eval_loss = 0.5907255411148071  
eval_rouge1 = 62.0922  
eval_rouge2 = 47.2761  
eval_rougeL = 61.7706  
eval_rougeLsum = 61.8036  
eval_runtime = 4501.8065  
eval_samples_per_second = 5.487  
eval_steps_per_second = 2.743  



## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 4
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.9.1+cu102
- Datasets 1.18.0
- Tokenizers 0.11.0

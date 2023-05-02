Hugging Face's logo
Hugging Face
Search models, datasets, users...
Models
Datasets
Spaces
Docs
Solutions
Pricing


Hugging Face is way more fun with friends and colleagues! 🤗 Join an organization

James-kc-min
/
AGT_Roberta Copied
like
0
Text Classification
PyTorch
Transformers
apache-2.0
roberta
generated_from_trainer
Eval Results
Infinity Compatible
Model card
Files and versions
Settings
AGT_Roberta
/
README.md
James-kc-min's picture
James-kc-min
update model card README.md
3abd7dd
about 3 hours ago
raw
history
blame
edit
delete
Safe
1.01 kB
---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: AGT_Roberta
  results: []
---
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->
# AGT_Roberta

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the None dataset.

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 1.16.0
- Tokenizers 0.12.1


---
tags:
- translation
- generated_from_trainer
metrics:
- bleu
model-index:
- name: pt-unicamp-handcrafted
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pt-unicamp-handcrafted

This model is a fine-tuned version of [VanessaSchenkel/pt-unicamp-news-t5](https://huggingface.co/VanessaSchenkel/pt-unicamp-news-t5) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7061
- Bleu: 75.3691

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
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.22.0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

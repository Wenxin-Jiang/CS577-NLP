---
license: mit
tags:
- generated_from_trainer
metrics:
- bleu
- rouge
model-index:
- name: mbart-large-50-English_German_Translation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbart-large-50-English_German_Translation

This model is a fine-tuned version of [facebook/mbart-large-50](https://huggingface.co/facebook/mbart-large-50) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2342
- Bleu: 35.5931
- Rouge: {'rouge1': 0.5803386608353808, 'rouge2': 0.3939141514072567, 'rougeL': 0.5438629663406402, 'rougeLsum': 0.544153348468965}
- Meteor: {'meteor': 0.5500546034636025}

## Model description

Here is the link to the script I created to train this model:

https://github.com/DunnBC22/NLP_Projects/blob/main/Machine%20Translation/NLP%20Translation%20Project-EN:DE.ipynb

## Intended uses & limitations

More information needed

## Training and evaluation data

Here is a the link to the page where I found this dataset:

https://www.kaggle.com/datasets/hgultekin/paralel-translation-corpus-in-22-languages

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Rouge                                                                                                                      | Meteor                         |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------:|
| 1.7738        | 1.0   | 900  | 1.2342          | 35.7436 | {'rouge1': 0.5805815969432273, 'rouge2': 0.3941222478624937, 'rougeL': 0.544162316313326, 'rougeLsum': 0.5444260344836553} | {'meteor': 0.5511605039667078} |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1
- Datasets 2.5.2
- Tokenizers 0.12.1

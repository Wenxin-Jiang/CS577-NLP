---
tags:
- translation
- generated_from_trainer
datasets:
- ted_iwlst2013
metrics:
- bleu
model-index:
- name: unicamp-finetuned-en-to-pt-dataset-ted
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: ted_iwlst2013
      type: ted_iwlst2013
      args: en-pt
    metrics:
    - name: Bleu
      type: bleu
      value: 25.65030250145235
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# unicamp-finetuned-en-to-pt-dataset-ted

This model is a fine-tuned version of [unicamp-dl/translation-pt-en-t5](https://huggingface.co/unicamp-dl/translation-pt-en-t5) on the ted_iwlst2013 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8861
- Bleu: 25.6503

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

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1

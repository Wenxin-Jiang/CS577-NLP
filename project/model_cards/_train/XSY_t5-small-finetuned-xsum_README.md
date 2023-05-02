这个模型是根据这个一步一步完成的，如果想自己微调，请参考https://colab.research.google.com/github/huggingface/notebooks/blob/master/examples/summarization.ipynb
This model is completed step by step according to this, if you want to fine-tune yourself, please refer to https://colab.research.google.com/github/huggingface/notebooks/blob/master/examples/summarization.ipynb

---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- xsum
metrics:
- rouge
model-index:
- name: t5-small-finetuned-xsum
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: xsum
      type: xsum
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 28.6901
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-xsum

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the xsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4500
- Rouge1: 28.6901
- Rouge2: 8.0102
- Rougel: 22.6087
- Rougelsum: 22.6105
- Gen Len: 18.824

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 2.6799        | 1.0   | 25506 | 2.4500          | 28.6901 | 8.0102 | 22.6087 | 22.6105   | 18.824  |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.9.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3

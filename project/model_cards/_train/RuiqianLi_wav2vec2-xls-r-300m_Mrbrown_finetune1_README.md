---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- uob_singlish
model-index:
- name: wav2vec2-xls-r-300m_Mrbrown_finetune1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m_Mrbrown_finetune1

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the uob_singlish dataset.

## This time use self-made dataset(cut the audio of "https://www.youtube.com/watch?v=a2ZOTD3R7JI" into slices and write the corresponding transcript, totally 4 mins), don't know why the word-error-rate keep 1. But can know that much be the problem of dataset, because last time use the same pre-trained model and standard singlish corpus fine-tune get nice result. (can find it at:RuiqianLi/wav2vec2-large-xls-r-300m-singlish-colab)

It achieves the following results on the evaluation set:
- Loss: 3.0927
- Wer: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.01
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer |
|:-------------:|:-----:|:----:|:---------------:|:---:|
| 3.7943        | 20.0  | 200  | 3.0597          | 1.0 |
| 2.9902        | 40.0  | 400  | 3.1604          | 1.0 |
| 2.9696        | 60.0  | 600  | 3.1112          | 1.0 |
| 2.8885        | 80.0  | 800  | 3.0234          | 1.0 |
| 2.8154        | 100.0 | 1000 | 3.0927          | 1.0 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3

---
license: mit
tags:
- generated_from_trainer
model-index:
- name: GPT2-LM-Finetuned-MBTI
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# GPT2-LM-Finetuned-MBTI

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.9582
- Lm loss: 3.9581
- Perplexity: 52.36

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Lm loss | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:----------:|
| 4.1981        | 1.0   | 3470  | 4.0349          | 4.0348  | 56.53      |
| 4.0457        | 2.0   | 6940  | 3.9963          | 3.9962  | 54.39      |
| 3.9757        | 3.0   | 10410 | 3.9815          | 3.9814  | 53.59      |
| 3.9247        | 4.0   | 13880 | 3.9701          | 3.9701  | 52.99      |
| 3.885         | 5.0   | 17350 | 3.9614          | 3.9613  | 52.52      |
| 3.8523        | 6.0   | 20820 | 3.9627          | 3.9627  | 52.60      |
| 3.8274        | 7.0   | 24290 | 3.9607          | 3.9606  | 52.49      |
| 3.8076        | 8.0   | 27760 | 3.9585          | 3.9584  | 52.37      |
| 3.7924        | 9.0   | 31230 | 3.9576          | 3.9575  | 52.33      |
| 3.782         | 10.0  | 34700 | 3.9582          | 3.9581  | 52.36      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1

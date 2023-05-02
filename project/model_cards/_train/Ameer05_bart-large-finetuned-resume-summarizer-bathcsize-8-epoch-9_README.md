---
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-finetuned-resume-summarizer-bathcsize-8-epoch-9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-finetuned-resume-summarizer-bathcsize-8-epoch-9

This model is a fine-tuned version of [Ameer05/tokenizer-repo](https://huggingface.co/Ameer05/tokenizer-repo) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5988
- Rouge1: 54.4865
- Rouge2: 45.2321
- Rougel: 50.0237
- Rougelsum: 53.2463

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 9
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 0.3463        | 1.0   | 44   | 2.0015          | 50.2382 | 40.3332 | 45.6831 | 49.1811   |
| 0.2771        | 2.0   | 88   | 2.0433          | 58.3265 | 50.1555 | 54.3681 | 56.9592   |
| 0.172         | 3.0   | 132  | 2.2077          | 55.9801 | 47.6352 | 51.9102 | 54.3347   |
| 0.1251        | 4.0   | 176  | 2.1834          | 53.3525 | 44.2643 | 49.9253 | 52.0145   |
| 0.0901        | 5.0   | 220  | 2.2857          | 56.7259 | 46.7879 | 52.3245 | 55.16     |
| 0.0506        | 6.0   | 264  | 2.5131          | 53.8128 | 44.9024 | 50.4617 | 52.8586   |
| 0.0434        | 7.0   | 308  | 2.5274          | 52.076  | 41.8135 | 47.3822 | 50.2634   |
| 0.0269        | 8.0   | 352  | 2.6374          | 54.7639 | 45.51   | 50.2608 | 53.6006   |
| 0.0147        | 9.0   | 396  | 2.5988          | 54.4865 | 45.2321 | 50.0237 | 53.2463   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.9.1
- Datasets 2.0.0
- Tokenizers 0.10.3

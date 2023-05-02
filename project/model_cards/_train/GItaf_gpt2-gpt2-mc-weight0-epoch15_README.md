---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-mc-weight0-epoch15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-mc-weight0-epoch15

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.9633
- Cls loss: 6.8154
- Lm loss: 3.9632
- Cls Accuracy: 0.1337
- Cls F1: 0.0531
- Cls Precision: 0.0331
- Cls Recall: 0.1337
- Perplexity: 52.63

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
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:-------:|:------------:|:------:|:-------------:|:----------:|:----------:|
| 4.1973        | 1.0   | 3470  | 4.0341          | 6.8497   | 4.0341  | 0.1331       | 0.0529 | 0.0330        | 0.1331     | 56.49      |
| 4.0446        | 2.0   | 6940  | 3.9948          | 6.8450   | 3.9947  | 0.1337       | 0.0531 | 0.0331        | 0.1337     | 54.31      |
| 3.9714        | 3.0   | 10410 | 3.9795          | 6.8404   | 3.9794  | 0.1337       | 0.0531 | 0.0331        | 0.1337     | 53.48      |
| 3.9176        | 4.0   | 13880 | 3.9686          | 6.8359   | 3.9686  | 0.1337       | 0.0531 | 0.0331        | 0.1337     | 52.91      |
| 3.8739        | 5.0   | 17350 | 3.9580          | 6.8317   | 3.9579  | 0.1331       | 0.0529 | 0.0330        | 0.1331     | 52.35      |
| 3.8359        | 6.0   | 20820 | 3.9591          | 6.8286   | 3.9590  | 0.1331       | 0.0529 | 0.0330        | 0.1331     | 52.40      |
| 3.8035        | 7.0   | 24290 | 3.9585          | 6.8263   | 3.9585  | 0.1331       | 0.0529 | 0.0330        | 0.1331     | 52.38      |
| 3.7762        | 8.0   | 27760 | 3.9585          | 6.8240   | 3.9585  | 0.1331       | 0.0529 | 0.0330        | 0.1331     | 52.38      |
| 3.7517        | 9.0   | 31230 | 3.9567          | 6.8216   | 3.9567  | 0.1337       | 0.0531 | 0.0331        | 0.1337     | 52.28      |
| 3.7313        | 10.0  | 34700 | 3.9599          | 6.8193   | 3.9598  | 0.1337       | 0.0531 | 0.0331        | 0.1337     | 52.45      |
| 3.7131        | 11.0  | 38170 | 3.9606          | 6.8169   | 3.9605  | 0.1337       | 0.0531 | 0.0331        | 0.1337     | 52.48      |
| 3.6982        | 12.0  | 41640 | 3.9614          | 6.8154   | 3.9614  | 0.1337       | 0.0531 | 0.0331        | 0.1337     | 52.53      |
| 3.6862        | 13.0  | 45110 | 3.9623          | 6.8154   | 3.9622  | 0.1337       | 0.0531 | 0.0331        | 0.1337     | 52.57      |
| 3.6767        | 14.0  | 48580 | 3.9621          | 6.8154   | 3.9620  | 0.1337       | 0.0531 | 0.0331        | 0.1337     | 52.56      |
| 3.6711        | 15.0  | 52050 | 3.9633          | 6.8154   | 3.9632  | 0.1337       | 0.0531 | 0.0331        | 0.1337     | 52.63      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
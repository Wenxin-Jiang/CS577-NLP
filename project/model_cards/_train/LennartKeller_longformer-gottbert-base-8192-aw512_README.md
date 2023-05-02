---
tags:
- generated_from_trainer
model-index:
- name: first
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# first

This model is a fine-tuned version of [longformer-gottbert-base-8192-aw512-](https://huggingface.co/longformer-8192-aw512-gottbert-base) on the a 500 million token subset of the german parts of the OSCAR dataset.
It achieves the following results on the custom evaluation set:
- Loss: 1.4981

## Model description

The weights of the model are initialized from the german version of Roberta [gottbert-base](https://huggingface.co/uklfr/gottbert-base).
The local attention windows have a fixed size of 512 tokens across all layers.
The maximum sequence length is 8192.

## Intended uses & limitations

Longformer models enable processing long texts using a mixture of local attention on each subword token and task specific global attention on a subset of the tokens.

## Training and evaluation data

The [OSCAR](https://oscar-corpus.com) dataset is freely avaible corpus of filtered web texts from the Common Crawl in various languages. We used the 2017 version of the dataset. 

## Training procedure
The model was trained with masked language modeling for 3 epochs on a customly created 500 million tokens subset of the german proportion of the [OSCAR](https://oscar-corpus.com) dataset.
It was validated using 5% of the original subset. 
### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 2
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.5636        | 0.1   | 500   | 2.2399          |
| 2.0426        | 0.2   | 1000  | 1.8841          |
| 1.9653        | 0.3   | 1500  | 1.7807          |
| 1.9422        | 0.4   | 2000  | 1.7206          |
| 1.9323        | 0.49  | 2500  | 1.6800          |
| 1.7587        | 0.59  | 3000  | 1.6507          |
| 1.7239        | 0.69  | 3500  | 1.6316          |
| 1.7452        | 0.79  | 4000  | 1.6137          |
| 1.7415        | 0.89  | 4500  | 1.5983          |
| 1.7733        | 0.99  | 5000  | 1.5830          |
| 1.7656        | 1.09  | 5500  | 1.5735          |
| 1.6543        | 1.19  | 6000  | 1.5643          |
| 1.7131        | 1.28  | 6500  | 1.5546          |
| 1.6456        | 1.38  | 7000  | 1.5503          |
| 1.716         | 1.48  | 7500  | 1.5422          |
| 1.806         | 1.58  | 8000  | 1.5377          |
| 1.8407        | 1.68  | 8500  | 1.5327          |
| 1.6371        | 1.78  | 9000  | 1.5278          |
| 1.6453        | 1.88  | 9500  | 1.5231          |
| 1.7754        | 1.98  | 10000 | 1.5214          |
| 1.7695        | 2.08  | 10500 | 1.5165          |
| 1.7109        | 2.17  | 11000 | 1.5138          |
| 1.6992        | 2.27  | 11500 | 1.5107          |
| 1.6707        | 2.37  | 12000 | 1.5097          |
| 1.6835        | 2.47  | 12500 | 1.5040          |
| 1.7171        | 2.57  | 13000 | 1.5041          |
| 1.7257        | 2.67  | 13500 | 1.4990          |
| 1.6287        | 2.77  | 14000 | 1.5017          |
| 1.7737        | 2.87  | 14500 | 1.4983          |
| 1.4002        | 2.96  | 15000 | 1.4992          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.17.0
- Tokenizers 0.10.3

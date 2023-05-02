---
tags:
- Buddhist Sanskrit
- BERT
- name: bert-base-buddhist-sanskrit
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-buddhist-sanskrit

The best performing model of the research described in the paper 'Embeddings models for Buddhist Sanskrit' published at LREC 2022 (Link to the paper will be added after 
the publication of conference proceedings).

## Model description

The model has the bert-base architecture and configuration and was pretrained from scratch as a masked language model 
on the Sanskrit reference corpus, and fine-tuned on the smaller corpus of Buddhist Sanskrit. 

## How to use it

```
model = AutoModelForMaskedLM.from_pretrained("Matej/bert-base-buddhist-sanskrit")
tokenizer = AutoTokenizer.from_pretrained("Matej/bert-base-buddhist-sanskrit", use_fast=True)
```

## Intended uses & limitations

MIT license, no limitations

## Training and evaluation data

See the paper 'Embeddings models for Buddhist Sanskrit' for details on the corpora and the evaluation procedure.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 28
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 300.0

### Framework versions

- Transformers 4.11.2
- Pytorch 1.7.0
- Datasets 1.12.1
- Tokenizers 0.10.3

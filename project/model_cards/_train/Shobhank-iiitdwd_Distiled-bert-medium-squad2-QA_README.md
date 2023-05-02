---
language: en
license: mit
tags:
- exbert
datasets:
- squad_v2
thumbnail: https://thumb.tildacdn.com/tild3433-3637-4830-a533-353833613061/-/resize/720x/-/format/webp/germanquad.jpg
model-index:
- name: deepset/bert-medium-squad2-distilled
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad_v2
      type: squad_v2
      config: squad_v2
      split: validation
    metrics:
    - type: exact_match
      value: 69.8231
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMmE4MGRkZTVjNmViMGNjYjVhY2E1NzcyOGQ1OWE1MWMzMjY5NWU0MmU0Y2I4OWU4YTU5OWQ5YTI2NWE1NmM0ZSIsInZlcnNpb24iOjF9.tnCJvWzMctTwiQu5yig_owO2ZI1t1MZz1AN2lQy4COAGOzuMovD-74acQvMbxJQoRfNNkIetz2hqYivf1lJKDw
    - type: f1
      value: 72.9232
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTMwNzk0ZDRjNGUyMjQyNzc1NzczZmUwMTU2MTM5MGQ3M2NhODlmOTU4ZDI0YjhlNTVjNDA1MGEwM2M1MzIyZSIsInZlcnNpb24iOjF9.eElGmTOXH_qHTNaPwZ-dUJfVz9VMvCutDCof_6UG_625MwctT_j7iVkWcGwed4tUnunuq1BPm-0iRh1RuuB-AQ
---

## Overview
**Language model:** deepset/roberta-base-squad2-distilled   
**Language:** English  
**Training data:** SQuAD 2.0 training set  
**Eval data:** SQuAD 2.0 dev set  
**Infrastructure**: 1x V100 GPU   
**Published**: Apr 21st, 2021 

## Details
- haystack's distillation feature was used for training. deepset/bert-large-uncased-whole-word-masking-squad2 was used as the teacher model.

## Hyperparameters
```
batch_size = 6
n_epochs = 2
max_seq_len = 384
learning_rate = 3e-5
lr_schedule = LinearWarmup
embeds_dropout_prob = 0.1
temperature = 5
distillation_loss_weight = 1
```
## Performance
```
"exact": 68.6431398972458
"f1": 72.7637083790805
```

## Authors
- Timo Möller: `timo.moeller [at] deepset.ai`
- Julian Risch: `julian.risch [at] deepset.ai`
- Malte Pietsch: `malte.pietsch [at] deepset.ai`
- Michel Bartels: `michel.bartels [at] deepset.ai`
## About us
![deepset logo](https://workablehr.s3.amazonaws.com/uploads/account/logo/476306/logo)
We bring NLP to the industry via open source!  
Our focus: Industry specific language models & large scale QA systems.  
  
Some of our work: 
- [German BERT (aka "bert-base-german-cased")](https://deepset.ai/german-bert)
- [GermanQuAD and GermanDPR datasets and models (aka "gelectra-base-germanquad", "gbert-base-germandpr")](https://deepset.ai/germanquad)
- [FARM](https://github.com/deepset-ai/FARM)
- [Haystack](https://github.com/deepset-ai/haystack/)

Get in touch:
[Twitter](https://twitter.com/deepset_ai) | [LinkedIn](https://www.linkedin.com/company/deepset-ai/) | [Discord](https://haystack.deepset.ai/community/join) | [GitHub Discussions](https://github.com/deepset-ai/haystack/discussions) | [Website](https://deepset.ai)

By the way: [we're hiring!](http://www.deepset.ai/jobs)
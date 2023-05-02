---
language: en
tags:
- natural-questions-short
- question-answering
license: mit
---

# xtremedistil-l6-h256-uncased for QA 

This is a [xtremedistil-l6-h256-uncased](https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased) model, fine-tuned using the [NaturalQuestionsShort](https://research.google/pubs/pub47761/) dataset from the [MRQA Shared Task 2019](https://github.com/mrqa/MRQA-Shared-Task-2019) repository.

## Overview
**Language model:** xtremedistil-l6-h256-uncased  
**Language:** English  
**Downstream-task:** Extractive QA  
**Training data:** NaturalQuestionsShort  
**Eval data:** NaturalQuestionsShort  
**Infrastructure**: Google Colaboratory GPU

## Hyperparameters

```
batch_size = 16
n_epochs = 2
base_LM_model = "xtremedistil-l6-h256-uncased"
max_seq_len = 512
learning_rate = 3e-5
optimizer = AdamW
weight_decay = 0.01
lr_schedule = Linear
warmup_steps = 0
``` 

## Performance
The model was evaluated on the on the [NaturalQuestionsShort](https://research.google/pubs/pub47761/) dev set from the [MRQA Shared Task 2019](https://github.com/mrqa/MRQA-Shared-Task-2019) repository.

```
"exact_match": 46.914926768463694,
"f1": 63.863619507647456,
```

## UKP Square
This model can also be found on [UKP Square](https://square.ukp-lab.de/qa). This website from the [UKP lab at the TU Darmstadt](https://www.informatik.tu-darmstadt.de/ukp/ukp_home/index.en.jsp) is a platform to compare and evaluate cloud-hosted QA models via explainability techniques and behavioral tests.

## Author & Background
This model was created by Janik and Ben during the [DL4NLP course](https://github.com/dl4nlp-tuda/deep-learning-for-nlp-lectures) by [Ivan Habernal](https://www.trusthlt.org/)

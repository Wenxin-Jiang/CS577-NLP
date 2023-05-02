---
tags:
- generated_from_trainer
datasets:
- consumer_complaints
model-index:
- name: distilbert-complaints-product
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-complaints-product

This model was trained from the [CFBP](https://www.consumerfinance.gov/data-research/consumer-complaints/) dataset, also made available on the HuggingFace Datasets library. This model predicts the type of financial complaint based on the text provided

## Model description

A DistilBert Text Classification Model, with 18 possible classes to determine the nature of a financial customer complaint.

## Intended uses & limitations

This model is used as part of.a demonstration for E2E Machine Learning Projects focused on Contact Centre Automation:  

- **Infrastructure:** Terraform
- **ML Ops:** HuggingFace (Datasets, Hub, Transformers) 
- **Ml Explainability:** SHAP 
- **Cloud:** AWS 
     - Model Hosting: Lambda 
     - DB Backend: DynamoDB
     - Orchestration: Step-Functions
     - UI Hosting: EC2
     - Routing: API Gateway 
- **UI:** Budibase

## Training and evaluation data

consumer_complaints dataset

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3

### Framework versions

- Transformers 4.16.1
- Pytorch 1.10.0+cu111
- Datasets 1.18.2
- Tokenizers 0.11.0

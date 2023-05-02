---
language:
- en
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
- f1
model-index:
- name: roberta-base-mrpc
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE MRPC
      type: glue
      args: mrpc
    metrics:
    - type: accuracy
      value: 0.9019607843137255
      name: Accuracy
    - type: f1
      value: 0.9295774647887324
      name: F1
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: glue
      type: glue
      config: mrpc
      split: validation
    metrics:
    - type: accuracy
      value: 0.9019607843137255
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTgxMmY3ZTkyZmYyZTJhZjQzNzkxYWRhMzRkNjQ4MDU3NmRhNzJmNDUwMmI5NWQyYTQ1ODRmMGVhOGI3NzMxZCIsInZlcnNpb24iOjF9.E6AhJwh_S4LfzhJjvlUzGWDmJYzxwbzL0IKqIIiNhFGg-_N5G9_VJAgqiQz-6i9xGHB2fJM-G5XinjHRk4SeBA
    - type: precision
      value: 0.9134948096885813
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2NmZThjNDI0YThmMzE4MjdhNjM3OTFmYzAwNzY4ZTM4ZDc4ZDA3NTYzYWRhNTdlNWMyZWI1NTMwZmFhNzQ5NyIsInZlcnNpb24iOjF9.nOkbqzXVD3r9LrIePn7o9Ny8_GiPoSBskCx3ey3Hrexrx00Gj6B9wkVvc8EcV5bAsBTeAJSeqO7ncS_-WJjlCQ
    - type: recall
      value: 0.946236559139785
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzA2NDgzYTkzMTY4ZDQxYTdlZmM2ODY4YzM4N2E0ODk0YzRkNDI3YTFhMGIwNDZhNTI0MmIyNGU0YmFlMzRjYyIsInZlcnNpb24iOjF9.jNL0IQk6XnUd6zFfHwTSL41Ax35OdoE8xQA-2PqEFs9UtT2O9fo6cZyXDln6QPMGHOlwNgPp_PX6mLrmDHN6Cw
    - type: auc
      value: 0.9536411880747964
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYmE0ZWZlNGFkMzdhNTdjZjY0NDkzNDZhOTJmY2Q1MWU4MTc3NGMwYmRjNTlkMTZjOTBiNjIwOTUzZWZhZTcwNSIsInZlcnNpb24iOjF9.ZVekwshvwAi8K6gYJmKEDk8riyiOqDhsfzbSxXa-AWKvREksbNtsDo_u6iOEYImGLbcEFfgesDE-cBnEsmMdAg
    - type: f1
      value: 0.9295774647887324
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDQwMmE1Y2FhMGE4M2Q5YjU3NTAyZTljZWQ5ODRkMGEyZmI4M2FhNDJjYjlkMzllMzU5NDQ1ZWI2YjNiNmM0OCIsInZlcnNpb24iOjF9.a2jDnaSZhCJ_3f1rBJ8mXfyLCRR6Y9tYb_Hayi00NPWrejDML8Bc-LoobxlPdbd8x8LVJ2vOWhbH5LP4J9kOBg
    - type: loss
      value: 0.48942330479621887
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiODFkMWQ5NTQ0ODMwNjQ2MzcyODA1ODlhZGUzNTg4NjE2M2U5MmIzYjQ3NzgxNTQyZDkyMGNiM2ZhYzc4ZGY0MSIsInZlcnNpb24iOjF9.K6fAIi21ZNtOqKS5c9jlO7kXISNHb0DD4pzdgLsESVjjOYxqS4C9f_OBJjIV-KtuwQGbi3yNC5Y4jTWk2HvNCQ
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mrpc

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE MRPC dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4898
- Accuracy: 0.9020
- F1: 0.9296
- Combined Score: 0.9158

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 5.0

### Training results



### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1

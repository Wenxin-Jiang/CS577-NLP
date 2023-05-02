---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- accuracy
model-index:
- name: twitter-emotion-deberta-v3-base
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: emotion
      type: emotion
      args: default
    metrics:
    - type: accuracy
      value: 0.937
      name: Accuracy
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: emotion
      type: emotion
      config: default
      split: test
    metrics:
    - type: accuracy
      value: 0.9255
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTlhZDRlN2VkOGQ0OTg3Nzg2OWJmOTAzMDYxZjk5NzE4YmMyNDIxM2FhOTgyMDI2ZTQ3ZjkyNGMwYjI4Nzc2ZiIsInZlcnNpb24iOjF9.GaEt0ZAvLf30YcCff1mZtjms1XD57bY-b00IVak3WGtZJsgVshwAP_Vla2pylTAQvZITz4WESqSlEpyu6Bn-CA
    - type: precision
      value: 0.8915483806374028
      name: Precision Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTI4MTRlN2UyMDZhODM1NWIzNzdhZTUyZjNhYjdkMmZiODRjM2ViODMzOTU4MGE1NjQ4MjM1ZWUwODQzMzk3YyIsInZlcnNpb24iOjF9.qU0v868jMD8kFNrF8CqaP0jGxLzx_ExZTJ1BIBQKEHPSv59QyDLUt6ggjL09jUcmNj-gmps2XzFO16ape0O2Ag
    - type: precision
      value: 0.9255
      name: Precision Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTY3NzgyMmFkYmY1NzU0ODM4NWVjZmI0MTgwYWU3OGY1MzI5NWRhNWMyYjM3NTQ0MzEzOWZmYTk5NDYxMjI0ZSIsInZlcnNpb24iOjF9.fnBjSgKbcOk3UF3pfn1rPbr87adek5YDTeSCqgSaCI4zzEqP_PWPNAinS1eBispGxEVh5iolmbO3frSZZ-TzDw
    - type: precision
      value: 0.9286522707274408
      name: Precision Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTE2ZmMxYzE2Mzc4OGQ2MzA1MDA3OGQ5Y2E4N2VkZDUwN2VjYmVhZGRlZTA2Nzg5NWJlZGNlMGYwNjc4YmNlYyIsInZlcnNpb24iOjF9.gRsf37CBTZpLIaAPNfdhli5cUV6K2Rbi8gHWHZydKTse9H9bkV6K_R6o_cMPhuXAyCCWx6SI-RbzInSC9K5lBw
    - type: recall
      value: 0.875946770128528
      name: Recall Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTZkNjMwOTFkZmEyYmRjNTBiOGFjYmYzYmZiMmUyY2U0ZWNhNDNmY2M3ZWZhODRjZDQ2MmFhNzZmM2ZjZDQ5OSIsInZlcnNpb24iOjF9.UTNojxmP-lR4wu13HPt7DAtgzFskdsR8IyohDDhA4sLj2_AQG7-FHdE7eE_SZ4H4FOtp-F1V-g6UoyDtFF0YCQ
    - type: recall
      value: 0.9255
      name: Recall Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZjczZjBlNDhhM2YwZDJiNGEwNmMwMTE3ZDQwY2FkMjY5MGMzNjI2NDMyMmNkNTg2ZGRmMWZmOTk2OTEwNGQ0ZCIsInZlcnNpb24iOjF9.DXAXqasIV3OiJGuUGSFMIDVSsM3ailYD5rHDj9bkoDJ0duVyRQdD5l_Uxs2ILUtMYvy66HG8q9hT3oaQpDDFAQ
    - type: recall
      value: 0.9255
      name: Recall Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDZjNGRhNDhkOTY4NmU5ZWUwNTJkNTk3ZGUwZjQwMzYyZTQ3YTYxZTBjMzg3ZjY5YjUwZGM1ZmI4YzlhZmMwMiIsInZlcnNpb24iOjF9.0Jr2FqC3_4aCO7N_Cd-25rjzz2rtyI0w863DvQfVPJNPzkWrs8qaQ_3lcfcQaMbR9CiVfKYPsgWb7-dwrm-UDA
    - type: f1
      value: 0.8790048313120858
      name: F1 Macro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNGNmMzc1MjgxZjM4Njk5ODM2NzIzOWMwYTIyN2E2NWJhYzcwNzgzMTQ0NWZjOGJhZmFkZjg5ZmNkNzYyYzdjMSIsInZlcnNpb24iOjF9.M3qaWCQwpe1vNptl5r8M62VhNe9-0eXQBZ1gIGRaEWOx9aRoTTFAqz_pl3wlhER0dSAjZlUuKElbYCI_R0KQDw
    - type: f1
      value: 0.9255
      name: F1 Micro
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOGQzNWNhOWFhZjNmYTllZTliYjRjNWVkMzgyNzE4OTcyZWIwOWY0ZTFkMjVjZDgwOTQyYWI1YzhkZjFmNWY3MiIsInZlcnNpb24iOjF9.zLzGH5b86fzDqgyM-P31QEgpVCVNXRXIxsUzWN0NinSARJDmGp0hYAKu80GwRRnCPdavIoluet1FjQaDvt6aDA
    - type: f1
      value: 0.92449885920049
      name: F1 Weighted
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYTQ2OTM0ZTU1MTQyNzQxNjVkNjY3ODdkYmJhOTE0ZTYxYzhiNzM3NGFhZGRiN2FiNzM5ZjFiNzczOGZhMDU1NCIsInZlcnNpb24iOjF9.33hcbfNttHRTdGFIgtD18ywdBnihqA3W2bJnwozAnpz6A1Fh9w-kHJ7WQ51XMK_MfHBNrMOO_k_x6fNS-Wm5Dg
    - type: loss
      value: 0.16804923117160797
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZWYwMWY5MzFkYjM3YjZmNmE3MmFlYTI3OTQ1OWRhZTUzODM3MjYwNTgxY2IxMjQ5NmI0ZDk3NDExZjg5YjJjZiIsInZlcnNpb24iOjF9.bHYpW_rQcKjc0QsMe8yVgWo-toI-LxAZE307_8kUKxQwzzb4cvrjLR66ciel2dVSMsjt479vGpbbAXU_8vh6Dw
---

# twitter-emotion-deberta-v3-base

This model is a fine-tuned version of [DeBERTa-v3](https://huggingface.co/microsoft/deberta-v3-base). It achieves the following results on the evaluation set:
- Loss: 0.1474
- Accuracy: 0.937

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 80
- eval_batch_size: 80
- lr_scheduler_type: linear
- num_epochs: 6.0 

### Framework versions
- Transformers 4.12.5
- Pytorch 1.10.0+cu113
- Datasets 1.15.1
- Tokenizers 0.10.3
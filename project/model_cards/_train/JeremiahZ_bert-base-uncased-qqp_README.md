---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-qqp
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE QQP
      type: glue
      args: qqp
    metrics:
    - type: accuracy
      value: 0.9099925797674994
      name: Accuracy
    - type: f1
      value: 0.8788252139455897
      name: F1
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: glue
      type: glue
      config: qqp
      split: validation
    metrics:
    - type: accuracy
      value: 0.9099925797674994
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2RlZGIxNjAyYjRkMzg4N2FhMDEwYzk3NzNlNDEyNjc2ZTI4M2U4Mjk0ODU0NTk4NmNhNjUwZjAxNDBmNjdkMiIsInZlcnNpb24iOjF9.ftCigJiFH-iVFMBG5dSVIxdV4sgu3QVcQ0HGDjnxdI6nlWXRVAXEPkEFBeo2T-NfKNOV62HRYC7JgquMS00VDg
    - type: precision
      value: 0.8712531361415555
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMGM5MDdjZGY5YzE4OTg3YmJkYTgwYWMxOWY4NjhkNmE3N2YwMzc0OTc1ODQ0NjZhYjYzZDA3NTZkODczODMyYyIsInZlcnNpb24iOjF9.waQg4ueAVRbKStoFGrZrLBgWgsfmK-Ro-eHFYNLObmSbbi35hC46tjAGgNd1blHc6aNsLmpkfK-qtMCepPEEAQ
    - type: recall
      value: 0.8865300638226402
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzYyODkxZmU4ZDNjNmQ0ZGZiMTExZTA0Mjk2ZjZkMDRiNGFhOWFhNTBhNzNkMjE5YzE2MDRkN2I4YjVlMTYxZSIsInZlcnNpb24iOjF9.wXo-nBoBrXeunx-4yCbkNUfyqc8HhrJ0NeQA1d_cNBXlsNVeGEznVFduSu8aVwrrLqbRpDJWYshPEL9eAxQPAQ
    - type: auc
      value: 0.9690747048570257
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYmZjZTc3NmU3MTQ4OWVmMWMzNzIxYjU5YjRjOGIwMzQwNGIxZmJhODJjMDhkZjA1ZGJmYjAzNDM4ZGQxZmQxNiIsInZlcnNpb24iOjF9.KiQN8JfNNTB3lBV-58LoLhQnUZTixTzId_URIpCFENICV2ykYzwfR7WW9WrOc8dbRv79121xB46fjNLGHziBAQ
    - type: f1
      value: 0.8788252139455897
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNmYyNjYxYmJmNjg3ODA1MjZmYWMxODllZGMzODI1NGFjNGU5ZTIxNGI3MWI4NWZiZDUwMDExMTE0ODEyODgyMSIsInZlcnNpb24iOjF9.a-gyRh1_YMEWnCTypkwp3w39iy5_1PmFntHszwtTISqDJtDKQsl3FYFJGzujSzllHrXl9ILFTcjLSkamvZSECw
    - type: loss
      value: 0.28284332156181335
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzg5ZGJiM2E4MzI1MmZkNjAyOWFlYjU2OGI0NDJiNTI3YThiNzZkMDIwMTNhZDg1NzMwNjZmNTE5NDgzYTBiMSIsInZlcnNpb24iOjF9.CPKvNWzGTwAZf0PgU-rhQYS_sFnRmrBVor4fRzDuNQjz-QtjdCPxyfWpGVsuOzuAr_u71fdFS6tGyuVpasl1Bw
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-qqp

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the GLUE QQP dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2829
- Accuracy: 0.9100
- F1: 0.8788
- Combined Score: 0.8944

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     | Combined Score |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|:--------------:|
| 0.2511        | 1.0   | 11371 | 0.2469          | 0.8969   | 0.8641 | 0.8805         |
| 0.1763        | 2.0   | 22742 | 0.2379          | 0.9071   | 0.8769 | 0.8920         |
| 0.1221        | 3.0   | 34113 | 0.2829          | 0.9100   | 0.8788 | 0.8944         |


### Framework versions

- Transformers 4.20.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1

---
language: en
license: apache-2.0
datasets:
- squad
metrics:
- squad
model-index:
- name: questionanswering-v2
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: squad
      type: squad
      config: plain_text
      split: validation
    metrics:
    - type: exact_match
      value: 79.5998
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTViZDA2Y2E2NjUyMjNjYjkzNTUzODc5OTk2OTNkYjQxMDRmMDhlYjdmYWJjYWQ2N2RlNzY1YmI3OWY1NmRhOSIsInZlcnNpb24iOjF9.ZJHhboAMwsi3pqU-B-XKRCYP_tzpCRb8pEjGr2Oc-TteZeoWHI8CXcpDxugfC3f7d_oBcKWLzh3CClQxBW1iAQ
    - type: f1
      value: 86.9965
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZWZlMzY2MmE1NDNhOGNjNWRmODg0YjQ2Zjk5MjUzZDQ2MDYxOTBlMTNhNzQ4NTA2NjRmNDU3MGIzMTYwMmUyOSIsInZlcnNpb24iOjF9.z0ZDir87aT7UEmUeDm8Uw0oUdAqzlBz343gwnsQP3YLfGsaHe-jGlhco0Z7ISUd9NokyCiJCRc4NNxJQ83IuCw
---
---
language:
- en
license: apache-2.0
datasets:
- squad_v2
model-index:
- name: abhilash1910/albert-squad-v2
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
      value: 23.6563
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZTE5ZTM2YzIwZjBhYjM0ZDUyNzBiMjg1YjZhMGJiMGViMjYzYjQ5ZmI4MGFkYmU4YjY1OTNjYzAwZWRlZjIwNSIsInZlcnNpb24iOjF9.jlvV8WRPSPKJm6UdApoh-dXcAOmLPtF5smsHt39RoO4sFzzbH6elUz5yPF5Lt9Yc2YDIl6c8JDsODqMxmsD0Bg
    - type: f1
      value: 29.3808
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiN2ZjYWRlYTI1NDkwYzNhMzM5YTg2NjZmODg0NjNkOGM3YjM2NTlkYjVhZWI0MzlmNjNkMTMxODlkNTY3ODBkMiIsInZlcnNpb24iOjF9.CR1MYeU3uqld9bbI8CLupMtote4WEG9fIq9enwhFJfVpChIT9BGKm86zaPmXHg0yBaNHgkMaEt_a-DaIdiEwAg
---

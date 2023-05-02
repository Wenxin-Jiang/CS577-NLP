---
language: en
license: cc-by-4.0
datasets:
- squad_v2
model-index:
- name: Shobhank-iiitdwd/BERT-base-cased-squad2-QA
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
      value: 71.1517
      name: Exact Match
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZGZlNmQ1YzIzMWUzNTg4YmI4NWVhYThiMzE2ZGZmNWUzNDM3NWI0ZGJkNzliNGUxNTY2MDA5MWVkYjAwYWZiMCIsInZlcnNpb24iOjF9.iUvVdy5c4hoXkwlThJankQqG9QXzNilvfF1_4P0oL8X-jkY5Q6YSsZx6G6cpgXogqFpn7JlE_lP6_OT0VIamCg
    - type: f1
      value: 74.6714
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMWE5OGNjODhmY2Y0NWIyZDIzMmQ2NmRjZGYyYTYzOWMxZDUzYzg4YjBhNTRiNTY4NTc0M2IxNjI5NWI5ZDM0NCIsInZlcnNpb24iOjF9.IqU9rbzUcKmDEoLkwCUZTKSH0ZFhtqgnhOaEDKKnaRMGBJLj98D5V4VirYT6jLh8FlR0FiwvMTMjReBcfTisAQ
---

This is a BERT base cased model trained on SQuAD v2
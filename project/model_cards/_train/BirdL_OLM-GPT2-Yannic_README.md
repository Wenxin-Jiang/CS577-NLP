---
datasets:
- Whispering-GPT/yannic-kilcher-transcript
model-index:
- name: BirdL/OLM-GPT2-Yannic
  results:
  - task:
      type: zero-shot-classification
      name: Zero-Shot Text Classification
    dataset:
      name: mathemakitten/winobias_antistereotype_dev
      type: mathemakitten/winobias_antistereotype_dev
      config: mathemakitten--winobias_antistereotype_dev
      split: validation
    metrics:
    - type: accuracy
      value: 0.5
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNTAzZTVjMjllNDE4N2NhZjVmNWU5NGU5MmNmOGVmZWUwMDVmNTRlNDM2OTc2YzcwZjA1ZjMwMmM0OTVkYTgwNiIsInZlcnNpb24iOjF9.AYptBsoQxvVm8weMxGYfjmXaNOIrSSPkwSqMmCyxuSCpld8KmQksVzmf0fz1tmn16Mjh_rnT6a8pcOp5Otd_Ag
    - type: loss
      value: 1.1590285866899648
      name: Loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNWE1YmMxZWQ4NGNkZDE5MGI2OTFjYTU2MjhhNzY4MjhhYmVmMmFlZDc2ZGY1ZDJmNTI1ZWE2ZGEwNjk1ODliYyIsInZlcnNpb24iOjF9.0WbjBvdLgaF7NcG0TnSTgQ_-4blOCzdeW15comZNvylnm7sY7bjH_4soR_7LaBBrhiWiMImzU8YHRbXCKMDJDA
---
A LLM finetuned from [OLM's GPT model](https://huggingface.co/Tristan/olm-gpt2-oct-2022) on [Yannic K's Youtube Channel](https://huggingface.co/datasets/Whispering-GPT/yannic-kilcher-transcript)
Under [BirdL-AirL++](https://github.com/BIRD-Laboratories/BirdL/blob/main/LICENSE.md)
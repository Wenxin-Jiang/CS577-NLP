---
library_name: sample-factory
tags:
- deep-reinforcement-learning
- reinforcement-learning
- sample-factory
model-index:
- name: APPO
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: atari_bowling
      type: atari_bowling
    metrics:
    - type: mean_reward
      value: 33.20 +/- 2.84
      name: mean_reward
      verified: false
---

A(n) **APPO** model trained on the **atari_bowling** environment.
This model was trained using Sample Factory 2.0: https://github.com/alex-petrenko/sample-factory
    
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
      name: doom_basic
      type: doom_basic
    metrics:
    - type: mean_reward
      value: 0.75 +/- 0.10
      name: mean_reward
      verified: false
---

A(n) **APPO** model trained on the **doom_basic** environment.
This model was trained using Sample Factory 2.0: https://github.com/alex-petrenko/sample-factory
    
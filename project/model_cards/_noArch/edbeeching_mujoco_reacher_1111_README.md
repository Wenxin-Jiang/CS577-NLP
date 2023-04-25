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
      name: mujoco_reacher
      type: mujoco_reacher
    metrics:
    - type: mean_reward
      value: -6.10 +/- 2.78
      name: mean_reward
      verified: false
---

A(n) **APPO** model trained on the **mujoco_reacher** environment.
This model was trained using Sample Factory 2.0: https://github.com/alex-petrenko/sample-factory
    
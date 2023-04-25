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
      name: mujoco_swimmer
      type: mujoco_swimmer
    metrics:
    - type: mean_reward
      value: 95.68 +/- 3.27
      name: mean_reward
      verified: false
---

A(n) **APPO** model trained on the **mujoco_swimmer** environment.
This model was trained using Sample Factory 2.0: https://github.com/alex-petrenko/sample-factory
    
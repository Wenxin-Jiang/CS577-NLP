---
tags:
- Pixelcopter-PLE-v0
- reinforce
- reinforcement-learning
- custom-implementation
- deep-rl-class
model-index:
- name: Reinforce-Pixelcopter-PLE-v0
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Pixelcopter-PLE-v0
      type: Pixelcopter-PLE-v0
    metrics:
    - type: mean_reward
      value: 16.40 +/- 9.31
      name: mean_reward
      verified: false
---

  # **Reinforce** Agent playing **Pixelcopter-PLE-v0**
  This is a trained model of a **Reinforce** agent playing **Pixelcopter-PLE-v0** .
  To learn to use this model and train yours check Unit 4 of the Deep Reinforcement Learning Course: https://huggingface.co/deep-rl-course/unit4/introduction

  # **Training hyperparameters**

  ```python
  pixelcopter_hyperparameters = {
    "h_size": 32,
    "n_training_episodes": 40000,
    "n_evaluation_episodes": 10,
    "max_t": 5000,
    "gamma": 0.98,
    "lr": 1e-5,
    "env_id": env_id,
    "state_space": s_size,
    "action_space": a_size,
  }
  ```
  
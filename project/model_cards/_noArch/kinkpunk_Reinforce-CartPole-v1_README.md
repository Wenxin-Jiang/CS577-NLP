---
tags:
- CartPole-v1
- reinforce
- reinforcement-learning
- custom-implementation
- deep-rl-class
model-index:
- name: Reinforce-CartPole-v1
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: CartPole-v1
      type: CartPole-v1
    metrics:
    - type: mean_reward
      value: 500.00 +/- 0.00
      name: mean_reward
      verified: false
---

  # **Reinforce** Agent playing **CartPole-v1**
  This is a trained model of a **Reinforce** agent playing **CartPole-v1** .
  To learn to use this model and train yours check Unit 4 of the Deep Reinforcement Learning Course: https://huggingface.co/deep-rl-course/unit4/introduction

  # **Training hyperparameters**

  ```python
  cartpole_hyperparameters = {
    "h_size": 8,
    "n_training_episodes": 4000,
    "n_evaluation_episodes": 10,
    "max_t": 500,
    "gamma": 0.98,
    "lr": 1e-3,
    "env_id": env_id,
    "state_space": s_size,
    "action_space": a_size,
}
```
  
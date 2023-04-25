---
tags:
- Pong-PLE-v0
- reinforce
- reinforcement-learning
- custom-implementation
- deep-rl-class
model-index:
- name: pong-policy
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Pong-PLE-v0
      type: Pong-PLE-v0
    metrics:
    - type: mean_reward
      value: -16.00 +/- 0.00
      name: mean_reward
      verified: false
---
## parameters
pong_hyperparameters = { <br>
    "h_size": 64,<br>
    "n_training_episodes": 20000,<br>
    "n_evaluation_episodes": 10,<br>
    "max_t": 5000,<br>
    "gamma": 0.99,<br>
    "lr": 1e-2,<br>
    "env_id": env_id,<br>
    "state_space": s_size,<br>
    "action_space": a_size,<br>
}<br>
  
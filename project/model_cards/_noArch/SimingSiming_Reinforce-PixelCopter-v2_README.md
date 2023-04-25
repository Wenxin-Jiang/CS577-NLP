---
tags:
- Pixelcopter-PLE-v0
- reinforce
- reinforcement-learning
- custom-implementation
- deep-rl-class
model-index:
- name: Reinforce-PixelCopter-v2
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Pixelcopter-PLE-v0
      type: Pixelcopter-PLE-v0
    metrics:
    - type: mean_reward
      value: 18.50 +/- 21.02
      name: mean_reward
      verified: false
---
<br>
pixelcopter_hyperparameters = { <br>
    "h_size": 64, <br>
    "n_training_episodes": 50000, <br>
    "n_evaluation_episodes": 10, <br>
    "max_t": 10000, <br>
    "gamma": 0.99, <br>
    "lr": 1e-4, <br>
    "env_id": env_id, <br>
    "state_space": s_size, <br>
    "action_space": a_size, <br>
}<br>
  
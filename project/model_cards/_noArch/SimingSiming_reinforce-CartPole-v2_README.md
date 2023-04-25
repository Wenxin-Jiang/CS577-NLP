---
tags:
- CartPole-v1
- reinforce
- reinforcement-learning
- custom-implementation
- deep-rl-class
model-index:
- name: reinforce-CartPole-v2
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: CartPole-v1
      type: CartPole-v1
    metrics:
    - type: mean_reward
      value: 221.40 +/- 16.12
      name: mean_reward
      verified: false
---

## parameters
cartpole_hyperparameters = { <br>
    "h_size": 16,<br>
    "n_training_episodes": 1000, <br>
    "n_evaluation_episodes": 10, <br>
    "max_t": 1000, <br>
    "gamma": 1.0, <br>
    "lr": 1e-2, <br>
    "env_id": env_id, <br>
    "state_space": s_size, <br>
    "action_space": a_size, <br>
}
  
---
library_name: stable-baselines3
tags:
- BipedalWalkerHardcore-v3
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 7.09 +/- 2.73
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: BipedalWalkerHardcore-v3
      type: BipedalWalkerHardcore-v3
---

  # parameters <br>
  model = A2C(policy = "MlpPolicy", <br>
            env = env, <br>
            n_steps = 256, <br>
            learning_rate = 0.001, <br>
            gamma = 0.99, <br>
            verbose=1) <br>
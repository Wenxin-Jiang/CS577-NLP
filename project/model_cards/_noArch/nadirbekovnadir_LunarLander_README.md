---
library_name: stable-baselines3
tags:
- LunarLander-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 286.34 +/- 10.43
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLander-v2
      type: LunarLander-v2
---

  # **PPO** Agent playing **LunarLander-v2**
  This is a trained model of a **PPO** agent playing **LunarLander-v2** using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).
  
  ## Usage (with Stable-baselines3)
  ```model = PPO(
    policy = 'MlpPolicy',
    env = env,
    n_steps = 1024,
    batch_size = 32,
    n_epochs = 4,
    gamma = 0.9990,
    gae_lambda = 0.995,
    ent_coef = 0.005,
    verbose=1)
   
   model.learn(total_timesteps=2000000)```
  
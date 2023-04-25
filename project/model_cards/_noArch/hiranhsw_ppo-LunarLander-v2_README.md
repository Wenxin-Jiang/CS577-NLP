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
      value: 282.19 +/- 21.40
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
```
  env = make_vec_env('LunarLander-v2', n_envs=24)
  model = PPO(
    policy = 'MlpPolicy',
    env = env,
    n_steps = 1024,
    batch_size = 64,
    n_epochs = 16,
    gamma = 0.999,
    gae_lambda = 0.98,
    ent_coef = 0.01,
    verbose=1)
  model.learn(total_timesteps=500000)
```
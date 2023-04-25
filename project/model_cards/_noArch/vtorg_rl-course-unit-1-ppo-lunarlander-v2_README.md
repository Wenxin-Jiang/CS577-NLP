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
      value: 280.00 +/- 24.62
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
  model = PPO(
    policy = 'MlpPolicy',
    env = env,
    n_steps = 2048,
    batch_size = 512,
    n_epochs = 4,
    gamma = 0.099,
    gae_lambda = 0.98,
    ent_coef = 0.01,
    learning_rate=0.00001,
    verbose=1,
    tensorboard_log="./ppo_tensorboard/")
    
  model.learn(total_timesteps=int(10e6))
  ```
  
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
      value: 282.71 +/- 20.92
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
  ## Parameters 
  
   model = PPO( <br>
    policy = "MlpPolicy", <br> 
    env = env,  <br>
    learning_rate = 0.0001, <br>
    n_steps = 1024, <br>
    batch_size = 32, <br>
    n_epochs = 16, <br>
    gamma = 0.999, <br>
    ent_coef = 0.01, <br>
    verbose = 1 <br>
    ) <br>
    
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
      value: 282.88 +/- 14.89
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
  from typing import Callable

  def linear_schedule(initial_value: float) -> Callable[[float], float]:
      def func(progress_remaining: float) -> float:
          return progress_remaining * initial_value
  
      return func
  
  model = PPO(policy="MlpPolicy", env=env, verbose=1, n_epochs=10, learning_rate=linear_schedule(0.005), n_steps=1500)
```
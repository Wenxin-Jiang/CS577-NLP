---
library_name: stable-baselines3
tags:
- AntBulletEnv-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 2447.40 +/- 23.14
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: AntBulletEnv-v0
      type: AntBulletEnv-v0
---

# **PPO** Agent playing **AntBulletEnv-v0**
This is a trained model of a **PPO** agent playing **AntBulletEnv-v0**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## Usage (with Stable-baselines3)

```python
from stable_baselines3 import ...
from huggingface_sb3 import load_from_hub

...
```
MODEL
model = PPO(policy = "MlpPolicy",
            env = env,
            batch_size = 256,
            clip_range = 0.4,
            ent_coef = 0.0,
            gae_lambda = 0.92,
            gamma = 0.99,
            learning_rate = 3.0e-05,
            max_grad_norm = 0.5,
            n_epochs = 30,
            n_steps = 512,
            policy_kwargs = dict(log_std_init=-2, ortho_init=False, activation_fn=nn.ReLU, net_arch=[dict(pi=[256,
      256], vf=[256, 256])] ),
            use_sde = True,
            sde_sample_freq = 4,
            vf_coef = 0.5,
            tensorboard_log = "./tensorboard",
            verbose=1)
            
model.learn(1_000_000)
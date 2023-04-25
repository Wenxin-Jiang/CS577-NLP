---
library_name: stable-baselines3
tags:
- AntBulletEnv-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: A2C
  results:
  - metrics:
    - type: mean_reward
      value: 1218.38 +/- 203.74
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: AntBulletEnv-v0
      type: AntBulletEnv-v0
---

# **A2C** Agent playing **AntBulletEnv-v0**
This is a trained model of a **A2C** agent playing **AntBulletEnv-v0**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## Usage (with Stable-baselines3)
## parameters

```python
model = A2C(policy = "MlpPolicy",
            env = env,
            gae_lambda = 0.9,
            gamma = 0.99,
            learning_rate = 0.00096,
            max_grad_norm = 0.5,
            n_steps = 8,
            vf_coef = 0.4,
            ent_coef = 0.0,
            tensorboard_log = "./tensorboard",
            policy_kwargs=dict(
            log_std_init=-2, ortho_init=False),
            normalize_advantage=False,
            use_rms_prop= True,
            use_sde= True,
            verbose=1)
...
```

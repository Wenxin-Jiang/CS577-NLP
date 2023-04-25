---
library_name: skrl
tags:
- deep-reinforcement-learning
- reinforcement-learning
- skrl
model-index:
- name: PPO
  results:
  - metrics:
    - type: mean_reward
      value: 11336.27 +/- 182.79
      name: Total reward (mean)
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Isaac-Ant-v0
      type: Isaac-Ant-v0
---

# IsaacOrbit-Isaac-Ant-v0-PPO

Trained agent model for [NVIDIA Isaac Orbit](https://github.com/NVIDIA-Omniverse/Orbit) environment

- **Task:** Isaac-Ant-v0
- **Agent:** [PPO](https://skrl.readthedocs.io/en/latest/modules/skrl.agents.ppo.html)

# Usage (with skrl) 

```python
from skrl.utils.huggingface import download_model_from_huggingface

# assuming that there is an agent named `agent`
path = download_model_from_huggingface("skrl/IsaacOrbit-Isaac-Ant-v0-PPO")
agent.load(path)
```

# Hyperparameters

```python
# https://skrl.readthedocs.io/en/latest/modules/skrl.agents.ppo.html#configuration-and-hyperparameters
cfg_ppo = PPO_DEFAULT_CONFIG.copy()
cfg_ppo["rollouts"] = 16  # memory_size
cfg_ppo["learning_epochs"] = 8
cfg_ppo["mini_batches"] = 4  # 16 * 1024 / 4096
cfg_ppo["discount_factor"] = 0.99
cfg_ppo["lambda"] = 0.95
cfg_ppo["learning_rate"] = 3e-4
cfg_ppo["learning_rate_scheduler"] = KLAdaptiveRL
cfg_ppo["learning_rate_scheduler_kwargs"] = {"kl_threshold": 0.008}
cfg_ppo["random_timesteps"] = 0
cfg_ppo["learning_starts"] = 0
cfg_ppo["grad_norm_clip"] = 1.0
cfg_ppo["ratio_clip"] = 0.2
cfg_ppo["value_clip"] = 0.2
cfg_ppo["clip_predicted_values"] = True
cfg_ppo["entropy_loss_scale"] = 0.0
cfg_ppo["value_loss_scale"] = 1.0
cfg_ppo["kl_threshold"] = 0
cfg_ppo["rewards_shaper"] = lambda rewards, timestep, timesteps: rewards * 0.01
cfg_ppo["state_preprocessor"] = RunningStandardScaler
cfg_ppo["state_preprocessor_kwargs"] = {"size": env.observation_space, "device": device}
cfg_ppo["value_preprocessor"] = RunningStandardScaler
cfg_ppo["value_preprocessor_kwargs"] = {"size": 1, "device": device}
# logging to TensorBoard and writing checkpoints
cfg_ppo["experiment"]["write_interval"] = 40
cfg_ppo["experiment"]["checkpoint_interval"] = 400
```

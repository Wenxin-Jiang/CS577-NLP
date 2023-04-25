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
      value: 494.34 +/- 0.87
      name: Total reward (mean)
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: OmniIsaacGymEnvs-Cartpole
      type: OmniIsaacGymEnvs-Cartpole
---

# OmniIsaacGymEnvs-Cartpole-PPO

Trained agent model for [NVIDIA Omniverse Isaac Gym](https://github.com/NVIDIA-Omniverse/OmniIsaacGymEnvs) environment

- **Task:** Cartpole
- **Agent:** [PPO](https://skrl.readthedocs.io/en/latest/modules/skrl.agents.ppo.html)

# Usage (with skrl) 

```python
from skrl.utils.huggingface import download_model_from_huggingface

# assuming that there is an agent named `agent`
path = download_model_from_huggingface("skrl/OmniIsaacGymEnvs-Cartpole-PPO")
agent.load(path)
```

# Hyperparameters

```python
# https://skrl.readthedocs.io/en/latest/modules/skrl.agents.ppo.html#configuration-and-hyperparameters
cfg_agent = PPO_DEFAULT_CONFIG.copy()
cfg_agent["rollouts"] = 16  # memory_size
cfg_agent["learning_epochs"] = 8
cfg_agent["mini_batches"] = 1  # 16 * 512 / 8192
cfg_agent["discount_factor"] = 0.99
cfg_agent["lambda"] = 0.95
cfg_agent["learning_rate"] = 3e-4
cfg_agent["learning_rate_scheduler"] = KLAdaptiveRL
cfg_agent["learning_rate_scheduler_kwargs"] = {"kl_threshold": 0.008}
cfg_agent["random_timesteps"] = 0
cfg_agent["learning_starts"] = 0
cfg_agent["grad_norm_clip"] = 1.0
cfg_agent["ratio_clip"] = 0.2
cfg_agent["value_clip"] = 0.2
cfg_agent["clip_predicted_values"] = True
cfg_agent["entropy_loss_scale"] = 0.0
cfg_agent["value_loss_scale"] = 2.0
cfg_agent["kl_threshold"] = 0
cfg_agent["rewards_shaper"] = lambda rewards, timestep, timesteps: rewards * 0.1
cfg_agent["state_preprocessor"] = RunningStandardScaler
cfg_agent["state_preprocessor_kwargs"] = {"size": env.observation_space, "device": device}
cfg_agent["value_preprocessor"] = RunningStandardScaler
cfg_agent["value_preprocessor_kwargs"] = {"size": 1, "device": device}
# logging to TensorBoard and writing checkpoints
cfg_agent["experiment"]["write_interval"] = 16
cfg_agent["experiment"]["checkpoint_interval"] = 80
```

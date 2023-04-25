---
library_name: stable-baselines3
tags:
- Sailing-v1
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: DQN
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Sailing-v1
      type: Sailing-v1
    metrics:
    - type: mean_reward
      value: 100.00 +/- 100.00
      name: mean_reward
      verified: false
---

# **DQN** Agent playing **Sailing-v1**
This is a trained model of a **DQN** agent playing **Sailing-v1**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3)
and the [RL Zoo](https://github.com/DLR-RM/rl-baselines3-zoo).

The RL Zoo is a training framework for Stable Baselines3
reinforcement learning agents,
with hyperparameter optimization and pre-trained agents included.

## Usage (with SB3 RL Zoo)

RL Zoo: https://github.com/DLR-RM/rl-baselines3-zoo<br/>
SB3: https://github.com/DLR-RM/stable-baselines3<br/>
SB3 Contrib: https://github.com/Stable-Baselines-Team/stable-baselines3-contrib

```
# Download model and save it into the logs/ folder
python -m rl_zoo3.load_from_hub --algo dqn --env Sailing-v1 -orga justinlangseth -f logs/
python enjoy.py --algo dqn --env Sailing-v1  -f logs/
```

If you installed the RL Zoo3 via pip (`pip install rl_zoo3`), from anywhere you can do:
```
python -m rl_zoo3.load_from_hub --algo dqn --env Sailing-v1 -orga justinlangseth -f logs/
rl_zoo3 enjoy --algo dqn --env Sailing-v1  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo dqn --env Sailing-v1 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo dqn --env Sailing-v1 -f logs/ -orga justinlangseth
```

## Hyperparameters
```python
OrderedDict([('batch_size', 128),
             ('buffer_size', 125000),
             ('exploration_final_eps', 0.01),
             ('exploration_fraction', 0.25),
             ('gamma', 0.99),
             ('gradient_steps', 1),
             ('learning_rate', 0.00063),
             ('learning_starts', 0),
             ('n_envs', 24),
             ('n_timesteps', 50000),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              'dict(net_arch=[512, 256, 128, 128], activation_fn=nn.ReLU)'),
             ('target_update_interval', 250),
             ('train_freq', 4),
             ('vec_env_wrapper', 'stable_baselines3.common.vec_env.VecMonitor'),
             ('normalize', False)])
```

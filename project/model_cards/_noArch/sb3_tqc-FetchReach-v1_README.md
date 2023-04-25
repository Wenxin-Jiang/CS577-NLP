---
library_name: stable-baselines3
tags:
- FetchReach-v1
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: TQC
  results:
  - metrics:
    - type: mean_reward
      value: -2.40 +/- 0.49
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: FetchReach-v1
      type: FetchReach-v1
---

# **TQC** Agent playing **FetchReach-v1**
This is a trained model of a **TQC** agent playing **FetchReach-v1**
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
python -m rl_zoo3.load_from_hub --algo tqc --env FetchReach-v1 -orga sb3 -f logs/
python enjoy.py --algo tqc --env FetchReach-v1  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo tqc --env FetchReach-v1 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo tqc --env FetchReach-v1 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('batch_size', 256),
             ('buffer_size', 1000000),
             ('ent_coef', 'auto'),
             ('env_wrapper', 'sb3_contrib.common.wrappers.TimeFeatureWrapper'),
             ('gamma', 0.95),
             ('learning_rate', 0.001),
             ('learning_starts', 1000),
             ('n_timesteps', 20000.0),
             ('normalize', True),
             ('policy', 'MultiInputPolicy'),
             ('policy_kwargs', 'dict(net_arch=[64, 64], n_critics=1)'),
             ('replay_buffer_class', 'HerReplayBuffer'),
             ('replay_buffer_kwargs',
              "dict( online_sampling=True, goal_selection_strategy='future', "
              'n_sampled_goal=4 )'),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```

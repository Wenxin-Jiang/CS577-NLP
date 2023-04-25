---
library_name: stable-baselines3
tags:
- FetchSlide-v1
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: TQC
  results:
  - metrics:
    - type: mean_reward
      value: -29.00 +/- 9.66
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: FetchSlide-v1
      type: FetchSlide-v1
---

# **TQC** Agent playing **FetchSlide-v1**
This is a trained model of a **TQC** agent playing **FetchSlide-v1**
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
python -m rl_zoo3.load_from_hub --algo tqc --env FetchSlide-v1 -orga sb3 -f logs/
python enjoy.py --algo tqc --env FetchSlide-v1  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo tqc --env FetchSlide-v1 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo tqc --env FetchSlide-v1 -f logs/ -orga sb3
```

## Hyperparameters
```python
OrderedDict([('batch_size', 512),
             ('buffer_size', 1000000),
             ('env_wrapper', 'sb3_contrib.common.wrappers.TimeFeatureWrapper'),
             ('gamma', 0.98),
             ('learning_rate', 0.001),
             ('n_timesteps', 3000000.0),
             ('policy', 'MultiInputPolicy'),
             ('policy_kwargs', 'dict(net_arch=[512, 512, 512], n_critics=2)'),
             ('replay_buffer_class', 'HerReplayBuffer'),
             ('replay_buffer_kwargs',
              "dict( online_sampling=True, goal_selection_strategy='future', "
              'n_sampled_goal=4, max_episode_length=100 )'),
             ('tau', 0.005),
             ('normalize', False)])
```

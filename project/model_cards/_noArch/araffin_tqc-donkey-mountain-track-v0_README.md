---
library_name: stable-baselines3
tags:
- donkey-mountain-track-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: TQC
  results:
  - metrics:
    - type: mean_reward
      value: 363.88 +/- 0.94
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: donkey-mountain-track-v0
      type: donkey-mountain-track-v0
---

# **TQC** Agent playing **donkey-mountain-track-v0**
This is a trained model of a **TQC** agent playing **donkey-mountain-track-v0**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3)
and the [RL Zoo](https://github.com/DLR-RM/rl-baselines3-zoo).

The RL Zoo is a training framework for Stable Baselines3
reinforcement learning agents,
with hyperparameter optimization and pre-trained agents included.

## Usage (with SB3 RL Zoo)

RL Zoo: https://github.com/DLR-RM/rl-baselines3-zoo<br/>
SB3: https://github.com/DLR-RM/stable-baselines3<br/>
SB3 Contrib: https://github.com/Stable-Baselines-Team/stable-baselines3-contrib

Autoencoder: https://github.com/araffin/aae-train-donkeycar branch: `feat/race_june` <br/>
Gym env: https://github.com/araffin/gym-donkeycar-1 branch: `feat/race_june` <br/>
RL Zoo branch: `feat/gym-donkeycar`

**Pretrained autoencoder** can be downloaded here: https://github.com/araffin/aae-train-donkeycar/releases/download/live-twitch-2/ae-32_mountain.pkl

```
export AE_PATH=/path/to/ae-32_mountain.pkl
# Download model and save it into the logs/ folder
python -m rl_zoo3.load_from_hub --algo tqc --env donkey-mountain-track-v0 -orga araffin -f logs/
python enjoy.py --algo tqc --env donkey-mountain-track-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo tqc --env donkey-mountain-track-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo tqc --env donkey-mountain-track-v0 -f logs/ -orga araffin
```

## Hyperparameters
```python
OrderedDict([('batch_size', 256),
             ('buffer_size', 200000),
             ('callback',
              [{'rl_zoo3.callbacks.ParallelTrainCallback': {'gradient_steps': 200}},
               'rl_zoo3.callbacks.LapTimeCallback']),
             ('ent_coef', 'auto'),
             ('env_wrapper',
              [{'gym.wrappers.time_limit.TimeLimit': {'max_episode_steps': 10000}},
               'ae.wrapper.AutoencoderWrapper',
               {'rl_zoo3.wrappers.HistoryWrapper': {'horizon': 2}}]),
             ('gamma', 0.99),
             ('gradient_steps', 256),
             ('learning_rate', 0.00073),
             ('learning_starts', 500),
             ('n_timesteps', 2000000.0),
             ('normalize', "{'norm_obs': True, 'norm_reward': False}"),
             ('policy', 'MlpPolicy'),
             ('policy_kwargs',
              'dict(log_std_init=-3, net_arch=[256, 256], n_critics=2, '
              'use_expln=True)'),
             ('sde_sample_freq', 16),
             ('tau', 0.02),
             ('train_freq', 200),
             ('use_sde', True),
             ('use_sde_at_warmup', True),
             ('normalize_kwargs', {'norm_obs': True, 'norm_reward': False})])
```

# Environment Arguments
```python
{'conf': {'cam_resolution': (120, 160, 3),
          'car_config': {'body_rgb': (226, 112, 18),
                         'body_style': 'donkey',
                         'car_name': 'Toni',
                         'font_size': 40},
          'frame_skip': 1,
          'host': 'localhost',
          'level': 'mountain_track',
          'log_level': 20,
          'max_cte': 16,
          'port': 9091,
          'start_delay': 5.0},
 'min_throttle': -0.2,
 'steer': 0.3}
```

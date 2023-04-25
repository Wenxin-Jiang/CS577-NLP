---
library_name: stable-baselines3
tags:
- RocketLander-v0
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: TQC
  results:
  - metrics:
    - type: mean_reward
      value: -0.00 +/- 0.16
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: RocketLander-v0
      type: RocketLander-v0
---

# **TQC** Agent playing **RocketLander-v0**
This is a trained model of a **TQC** agent playing **RocketLander-v0**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3)
and the [RL Zoo](https://github.com/DLR-RM/rl-baselines3-zoo).

The RL Zoo is a training framework for Stable Baselines3
reinforcement learning agents,
with hyperparameter optimization and pre-trained agents included.

## Usage (with SB3 RL Zoo)

RL Zoo: https://github.com/DLR-RM/rl-baselines3-zoo<br/>
SB3: https://github.com/DLR-RM/stable-baselines3<br/>
SB3 Contrib: https://github.com/Stable-Baselines-Team/stable-baselines3-contrib

Gym env: https://github.com/sdsubhajitdas/Rocket_Lander_Gym

```
# Download model and save it into the logs/ folder
python -m rl_zoo3.load_from_hub --algo tqc --env RocketLander-v0 -orga araffin -f logs/
python enjoy.py --algo tqc --env RocketLander-v0  -f logs/
```

## Training (with the RL Zoo)
```
python train.py --algo tqc --env RocketLander-v0 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo tqc --env RocketLander-v0 -f logs/ -orga araffin
```

## Hyperparameters
```python
OrderedDict([('env_wrapper',
              [{'rl_zoo3.wrappers.FrameSkip': {'skip': 4}},
               {'rl_zoo3.wrappers.HistoryWrapper': {'horizon': 2}}]),
             ('n_timesteps', 3000000.0),
             ('policy', 'MlpPolicy'),
             ('normalize', False)])
```

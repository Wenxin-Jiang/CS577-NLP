---
library_name: stable-baselines3
tags:
- MsPacmanNoFrameskip-v4
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
      name: MsPacmanNoFrameskip-v4
      type: MsPacmanNoFrameskip-v4
    metrics:
    - type: mean_reward
      value: 109.00 +/- 25.87
      name: mean_reward
      verified: false
---

# **DQN** Agent playing **MsPacmanNoFrameskip-v4**
This is a trained model of a **DQN** agent playing **MsPacmanNoFrameskip-v4**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3)
and the [RL Zoo](https://github.com/DLR-RM/rl-baselines3-zoo).

The RL Zoo is a training framework for Stable Baselines3
reinforcement learning agents,
with hyperparameter optimization and pre-trained agents included.

## Usage (with SB3 RL Zoo)

RL Zoo: https://github.com/DLR-RM/rl-baselines3-zoo<br/>
SB3: https://github.com/DLR-RM/stable-baselines3<br/>
SB3 Contrib: https://github.com/Stable-Baselines-Team/stable-baselines3-contrib

Install the RL Zoo (with SB3 and SB3-Contrib):
```bash
pip install rl_zoo3
```

```
# Download model and save it into the logs/ folder
python -m rl_zoo3.load_from_hub --algo dqn --env MsPacmanNoFrameskip-v4 -orga ljicvedera -f logs/
python -m rl_zoo3.enjoy --algo dqn --env MsPacmanNoFrameskip-v4  -f logs/
```

If you installed the RL Zoo3 via pip (`pip install rl_zoo3`), from anywhere you can do:
```
python -m rl_zoo3.load_from_hub --algo dqn --env MsPacmanNoFrameskip-v4 -orga ljicvedera -f logs/
python -m rl_zoo3.enjoy --algo dqn --env MsPacmanNoFrameskip-v4  -f logs/
```

## Training (with the RL Zoo)
```
python -m rl_zoo3.train --algo dqn --env MsPacmanNoFrameskip-v4 -f logs/
# Upload the model and generate video (when possible)
python -m rl_zoo3.push_to_hub --algo dqn --env MsPacmanNoFrameskip-v4 -f logs/ -orga ljicvedera
```

## Hyperparameters
```python
OrderedDict([('batch_size', 32),
             ('buffer_size', 100000),
             ('env_wrapper',
              ['stable_baselines3.common.atari_wrappers.AtariWrapper']),
             ('exploration_final_eps', 0.01),
             ('exploration_fraction', 0.1),
             ('frame_stack', 4),
             ('gradient_steps', 1),
             ('learning_rate', 0.0001),
             ('learning_starts', 100000),
             ('n_timesteps', 100000),
             ('optimize_memory_usage', False),
             ('policy', 'CnnPolicy'),
             ('target_update_interval', 1000),
             ('train_freq', 4),
             ('normalize', False)])
```

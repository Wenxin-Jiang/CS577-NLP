---
tags:
- BreakoutNoFrameskip-v4
- deep-reinforcement-learning
- reinforcement-learning
- custom-implementation
library_name: cleanrl
model-index:
- name: C51
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: BreakoutNoFrameskip-v4
      type: BreakoutNoFrameskip-v4
    metrics:
    - type: mean_reward
      value: 381.00 +/- 56.35
      name: mean_reward
      verified: false
---

# (CleanRL) **C51** Agent Playing **BreakoutNoFrameskip-v4**

This is a trained model of a C51 agent playing BreakoutNoFrameskip-v4.
The model was trained by using [CleanRL](https://github.com/vwxyzjn/cleanrl) and the most up-to-date training code can be
found [here](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/c51_atari.py).

## Get Started

To use this model, please install the `cleanrl` package with the following command:

```
pip install "cleanrl[c51_atari]"
python -m cleanrl_utils.enjoy --exp-name c51_atari --env-id BreakoutNoFrameskip-v4
```

Please refer to the [documentation](https://docs.cleanrl.dev/get-started/zoo/) for more detail.


## Command to reproduce the training

```bash
curl -OL https://huggingface.co/kinalmehta/BreakoutNoFrameskip-v4-c51_atari-seed1/raw/main/c51_atari.py
curl -OL https://huggingface.co/kinalmehta/BreakoutNoFrameskip-v4-c51_atari-seed1/raw/main/pyproject.toml
curl -OL https://huggingface.co/kinalmehta/BreakoutNoFrameskip-v4-c51_atari-seed1/raw/main/poetry.lock
poetry install --all-extras
python c51_atari.py --save-model --upload-model --hf-entity kinalmehta --env-id BreakoutNoFrameskip-v4
```

# Hyperparameters
```python
{'batch_size': 32,
 'buffer_size': 1000000,
 'capture_video': False,
 'cuda': True,
 'end_e': 0.01,
 'env_id': 'BreakoutNoFrameskip-v4',
 'exp_name': 'c51_atari',
 'exploration_fraction': 0.1,
 'gamma': 0.99,
 'hf_entity': 'kinalmehta',
 'learning_rate': 0.00025,
 'learning_starts': 80000,
 'n_atoms': 51,
 'save_model': True,
 'seed': 1,
 'start_e': 1,
 'target_network_frequency': 10000,
 'torch_deterministic': True,
 'total_timesteps': 10000000,
 'track': False,
 'train_frequency': 4,
 'upload_model': True,
 'v_max': 10,
 'v_min': -10,
 'wandb_entity': None,
 'wandb_project_name': 'cleanRL'}
```
    
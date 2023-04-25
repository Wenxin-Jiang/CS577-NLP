---
tags:
- MountainCar-v0
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
      name: MountainCar-v0
      type: MountainCar-v0
    metrics:
    - type: mean_reward
      value: -165.70 +/- 37.64
      name: mean_reward
      verified: false
---

# (CleanRL) **C51** Agent Playing **MountainCar-v0**

This is a trained model of a C51 agent playing MountainCar-v0.
The model was trained by using [CleanRL](https://github.com/vwxyzjn/cleanrl) and the most up-to-date training code can be
found [here](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/c51.py).

## Command to reproduce the training

```bash
curl -OL https://huggingface.co/cleanrl/MountainCar-v0-c51-seed1/raw/main/c51.py
curl -OL https://huggingface.co/cleanrl/MountainCar-v0-c51-seed1/raw/main/pyproject.toml
curl -OL https://huggingface.co/cleanrl/MountainCar-v0-c51-seed1/raw/main/poetry.lock
poetry install --all-extras
python c51.py --save-model --upload-model --hf-entity cleanrl --cuda False --env-id MountainCar-v0
```

# Hyperparameters
```python
{'batch_size': 128,
 'buffer_size': 10000,
 'capture_video': False,
 'cuda': False,
 'end_e': 0.05,
 'env_id': 'MountainCar-v0',
 'exp_name': 'c51',
 'exploration_fraction': 0.5,
 'gamma': 0.99,
 'hf_entity': 'cleanrl',
 'learning_rate': 0.00025,
 'learning_starts': 10000,
 'n_atoms': 101,
 'save_model': True,
 'seed': 1,
 'start_e': 1,
 'target_network_frequency': 500,
 'torch_deterministic': True,
 'total_timesteps': 500000,
 'track': False,
 'train_frequency': 10,
 'upload_model': True,
 'v_max': 100,
 'v_min': -100,
 'wandb_entity': None,
 'wandb_project_name': 'cleanRL'}
```
    
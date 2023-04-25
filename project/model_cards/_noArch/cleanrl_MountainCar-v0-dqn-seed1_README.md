---
tags:
- MountainCar-v0
- deep-reinforcement-learning
- reinforcement-learning
- custom-implementation
library_name: cleanrl
model-index:
- name: DQN
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: MountainCar-v0
      type: MountainCar-v0
    metrics:
    - type: mean_reward
      value: -200.00 +/- 0.00
      name: mean_reward
      verified: false
---

# (CleanRL) **DQN** Agent Playing **MountainCar-v0**

This is a trained model of a DQN agent playing MountainCar-v0.
The model was trained by using [CleanRL](https://github.com/vwxyzjn/cleanrl) and the most up-to-date training code can be
found [here](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/dqn.py).

## Command to reproduce the training

```bash
curl -OL https://huggingface.co/cleanrl/MountainCar-v0-dqn-seed1/raw/main/dqn.py
curl -OL https://huggingface.co/cleanrl/MountainCar-v0-dqn-seed1/raw/main/pyproject.toml
curl -OL https://huggingface.co/cleanrl/MountainCar-v0-dqn-seed1/raw/main/poetry.lock
poetry install --all-extras
python dqn.py --cuda False --track --capture-video --save-model --upload-model --hf-entity cleanrl --env-id MountainCar-v0 --seed 1
```

# Hyperparameters
```python
{'batch_size': 128,
 'buffer_size': 10000,
 'capture_video': True,
 'cuda': False,
 'end_e': 0.05,
 'env_id': 'MountainCar-v0',
 'exp_name': 'dqn',
 'exploration_fraction': 0.5,
 'gamma': 0.99,
 'hf_entity': 'cleanrl',
 'learning_rate': 0.00025,
 'learning_starts': 10000,
 'save_model': True,
 'seed': 1,
 'start_e': 1,
 'target_network_frequency': 500,
 'torch_deterministic': True,
 'total_timesteps': 500000,
 'track': True,
 'train_frequency': 10,
 'upload_model': True,
 'wandb_entity': None,
 'wandb_project_name': 'cleanRL'}
```
    
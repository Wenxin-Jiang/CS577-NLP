---
tags:
- BeamRiderNoFrameskip-v4
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
      name: BeamRiderNoFrameskip-v4
      type: BeamRiderNoFrameskip-v4
    metrics:
    - type: mean_reward
      value: 7155.60 +/- 2103.76
      name: mean_reward
      verified: false
---

# (CleanRL) **DQN** Agent Playing **BeamRiderNoFrameskip-v4**

This is a trained model of a DQN agent playing BeamRiderNoFrameskip-v4.
The model was trained by using [CleanRL](https://github.com/vwxyzjn/cleanrl) and the most up-to-date training code can be
found [here](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/dqn_atari.py).

## Command to reproduce the training

```bash
curl -OL https://huggingface.co/cleanrl/BeamRiderNoFrameskip-v4-dqn_atari-seed1/raw/main/dqn.py
curl -OL https://huggingface.co/cleanrl/BeamRiderNoFrameskip-v4-dqn_atari-seed1/raw/main/pyproject.toml
curl -OL https://huggingface.co/cleanrl/BeamRiderNoFrameskip-v4-dqn_atari-seed1/raw/main/poetry.lock
poetry install --all-extras
python dqn_atari.py --track --capture-video --save-model --upload-model --hf-entity cleanrl --env-id BeamRiderNoFrameskip-v4 --seed 1
```

# Hyperparameters
```python
{'batch_size': 32,
 'buffer_size': 1000000,
 'capture_video': True,
 'cuda': True,
 'end_e': 0.01,
 'env_id': 'BeamRiderNoFrameskip-v4',
 'exp_name': 'dqn_atari',
 'exploration_fraction': 0.1,
 'gamma': 0.99,
 'hf_entity': 'cleanrl',
 'learning_rate': 0.0001,
 'learning_starts': 80000,
 'save_model': True,
 'seed': 1,
 'start_e': 1,
 'target_network_frequency': 1000,
 'torch_deterministic': True,
 'total_timesteps': 10000000,
 'track': True,
 'train_frequency': 4,
 'upload_model': True,
 'wandb_entity': None,
 'wandb_project_name': 'cleanRL'}
```
    
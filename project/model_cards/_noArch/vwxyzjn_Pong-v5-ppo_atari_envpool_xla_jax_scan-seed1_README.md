---
tags:
- Pong-v5
- deep-reinforcement-learning
- reinforcement-learning
- custom-implementation
library_name: cleanrl
model-index:
- name: PPO
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Pong-v5
      type: Pong-v5
    metrics:
    - type: mean_reward
      value: -20.30 +/- 0.78
      name: mean_reward
      verified: false
---

# (CleanRL) **PPO** Agent Playing **Pong-v5**

This is a trained model of a PPO agent playing Pong-v5.
The model was trained by using [CleanRL](https://github.com/vwxyzjn/cleanrl) and the most up-to-date training code can be
found [here](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_atari_envpool_xla_jax_scan.py).

## Command to reproduce the training

```bash
curl -OL https://huggingface.co/vwxyzjn/Pong-v5-ppo_atari_envpool_xla_jax_scan-seed1/raw/main/ppo_atari_envpool_xla_jax_scan.py
curl -OL https://huggingface.co/vwxyzjn/Pong-v5-ppo_atari_envpool_xla_jax_scan-seed1/raw/main/pyproject.toml
curl -OL https://huggingface.co/vwxyzjn/Pong-v5-ppo_atari_envpool_xla_jax_scan-seed1/raw/main/poetry.lock
poetry install --all-extras
python ppo_atari_envpool_xla_jax_scan.py --save-model --total-timesteps 1025 --upload-model
```

# Hyperparameters
```python
{'anneal_lr': True,
 'batch_size': 1024,
 'capture_video': False,
 'clip_coef': 0.1,
 'cuda': True,
 'ent_coef': 0.01,
 'env_id': 'Pong-v5',
 'exp_name': 'ppo_atari_envpool_xla_jax_scan',
 'gae_lambda': 0.95,
 'gamma': 0.99,
 'hf_entity': '',
 'learning_rate': 0.00025,
 'max_grad_norm': 0.5,
 'minibatch_size': 256,
 'norm_adv': True,
 'num_envs': 8,
 'num_minibatches': 4,
 'num_steps': 128,
 'num_updates': 1,
 'save_model': True,
 'seed': 1,
 'target_kl': None,
 'torch_deterministic': True,
 'total_timesteps': 1025,
 'track': False,
 'update_epochs': 4,
 'upload_model': True,
 'vf_coef': 0.5,
 'wandb_entity': None,
 'wandb_project_name': 'cleanRL'}
```
    
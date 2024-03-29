---
tags:
- DemonAttack-v5
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
      name: DemonAttack-v5
      type: DemonAttack-v5
    metrics:
    - type: mean_reward
      value: 88490.00 +/- 45858.13
      name: mean_reward
      verified: false
---

# (CleanRL) **PPO** Agent Playing **DemonAttack-v5**

This is a trained model of a PPO agent playing DemonAttack-v5.
The model was trained by using [CleanRL](https://github.com/vwxyzjn/cleanrl) and the most up-to-date training code can be
found [here](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_atari_envpool_async_jax_scan_impalanet_machado.py).

## Get Started

To use this model, please install the `cleanrl` package with the following command:

```
pip install "cleanrl[ppo_atari_envpool_async_jax_scan_impalanet_machado]"
python -m cleanrl_utils.enjoy --exp-name ppo_atari_envpool_async_jax_scan_impalanet_machado --env-id DemonAttack-v5
```

Please refer to the [documentation](https://docs.cleanrl.dev/get-started/zoo/) for more detail.


## Command to reproduce the training

```bash
curl -OL https://huggingface.co/cleanrl/DemonAttack-v5-ppo_atari_envpool_async_jax_scan_impalanet_machado-seed1/raw/main/ppo_atari_envpool_async_jax_scan_impalanet_machado.py
curl -OL https://huggingface.co/cleanrl/DemonAttack-v5-ppo_atari_envpool_async_jax_scan_impalanet_machado-seed1/raw/main/pyproject.toml
curl -OL https://huggingface.co/cleanrl/DemonAttack-v5-ppo_atari_envpool_async_jax_scan_impalanet_machado-seed1/raw/main/poetry.lock
poetry install --all-extras
python ppo_atari_envpool_async_jax_scan_impalanet_machado.py --track --wandb-project-name envpool-atari --save-model --upload-model --hf-entity cleanrl --env-id DemonAttack-v5 --seed 1
```

# Hyperparameters
```python
{'anneal_lr': True,
 'async_batch_size': 16,
 'batch_size': 2048,
 'capture_video': False,
 'clip_coef': 0.1,
 'cuda': True,
 'ent_coef': 0.01,
 'env_id': 'DemonAttack-v5',
 'exp_name': 'ppo_atari_envpool_async_jax_scan_impalanet_machado',
 'gae': True,
 'gae_lambda': 0.95,
 'gamma': 0.99,
 'hf_entity': 'cleanrl',
 'learning_rate': 0.00025,
 'max_grad_norm': 0.5,
 'minibatch_size': 1024,
 'norm_adv': True,
 'num_envs': 64,
 'num_minibatches': 2,
 'num_steps': 32,
 'num_updates': 24414,
 'save_model': True,
 'seed': 1,
 'target_kl': None,
 'torch_deterministic': True,
 'total_timesteps': 50000000,
 'track': True,
 'update_epochs': 2,
 'upload_model': True,
 'vf_coef': 0.5,
 'wandb_entity': None,
 'wandb_project_name': 'envpool-atari'}
```
    
---
tags:
- CartPole-v1
- deep-reinforcement-learning
- reinforcement-learning
- custom-implementation
---

# (CleanRL) **PPO** Agent Playing **CartPole-v1**

This is a trained model of a PPO agent playing CartPole-v1.
The model was trained by using [CleanRL](https://github.com/vwxyzjn/cleanrl) and the training code can be
found [here](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo.py).


# Hyperparameters
```python
{'anneal_lr': True,
 'batch_size': 512,
 'capture_video': True,
 'clip_coef': 0.2,
 'clip_vloss': True,
 'cuda': False,
 'ent_coef': 0.01,
 'env_id': 'CartPole-v1',
 'exp_name': 'ppo',
 'gae_lambda': 0.95,
 'gamma': 0.99,
 'hf_repo_id': 'cleanrl/ppo',
 'learning_rate': 0.00025,
 'max_grad_norm': 0.5,
 'minibatch_size': 128,
 'norm_adv': True,
 'num_envs': 4,
 'num_minibatches': 4,
 'num_steps': 128,
 'save_model': True,
 'seed': 1,
 'target_kl': None,
 'torch_deterministic': True,
 'total_timesteps': 500000,
 'track': False,
 'update_epochs': 4,
 'vf_coef': 0.5,
 'wandb_entity': None,
 'wandb_project_name': 'cleanRL'}
```
    
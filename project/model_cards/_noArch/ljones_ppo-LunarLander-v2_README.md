---
tags:
- LunarLander-v2
- ppo
- deep-reinforcement-learning
- reinforcement-learning
- custom-implementation
- deep-rl-course
model-index:
- name: PPO
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLander-v2
      type: LunarLander-v2
    metrics:
    - type: mean_reward
      value: -199.29 +/- 90.62
      name: mean_reward
      verified: false
---

  # PPO Agent Playing LunarLander-v2

  This is a trained model of a PPO agent playing LunarLander-v2.
    
  # Hyperparameters
  ```python
  {'exp_name': 'content'
'seed': 1
'torch_deterministic': True
'cuda': True
'track': False
'wandb_project_name': 'cleanRL'
'wandb_entity': None
'capture_video': False
'f': '/root/.local/share/jupyter/runtime/kernel-b252e6ab-0275-4a60-b972-785086eee67d.json'
'env_id': 'LunarLander-v2'
'total_timesteps': 25000
'learning_rate': 0.00025
'num_envs': 4
'num_steps': 128
'anneal_lr': True
'gae': True
'gamma': 0.99
'gae_lambda': 0.95
'num_minibatches': 4
'update_epochs': 4
'norm_adv': True
'clip_coef': 0.2
'clip_vloss': True
'ent_coef': 0.01
'vf_coef': 0.5
'max_grad_norm': 0.5
'target_kl': None
'repo_id': 'ljones/ppo-LunarLander-v2'
'batch_size': 512
'minibatch_size': 128}
  ```
  
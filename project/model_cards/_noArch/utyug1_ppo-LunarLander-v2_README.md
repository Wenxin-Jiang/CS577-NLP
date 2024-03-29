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
      value: 271.06 +/- 21.00
      name: mean_reward
      verified: false
---

    # PPO Agent Playing LunarLander-v2

    This is a trained model of a PPO agent playing LunarLander-v2.
        
    # Hyperparameters
    ```python
    {'exp_name': 'ppo'
'seed': 1
'torch_deterministic': True
'cuda': True
'track': False
'wandb_project_name': 'cleanRL'
'wandb_entity': None
'capture_video': False
'env_id': 'LunarLander-v2'
'total_timesteps': 5000000
'learning_rate': 0.001
'num_envs': 32
'num_steps': 512
'anneal_lr': True
'gae': True
'gamma': 0.999
'gae_lambda': 0.97
'num_minibatches': 128
'update_epochs': 4
'norm_adv': True
'clip_coef': 0.2
'clip_vloss': True
'ent_coef': 0.01
'vf_coef': 0.5
'max_grad_norm': 0.5
'target_kl': None
'repo_id': 'utyug1/ppo-LunarLander-v2'
'batch_size': 16384
'minibatch_size': 128}
    ```
    
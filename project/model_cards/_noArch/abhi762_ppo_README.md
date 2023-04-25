---
tags:
- CartPole-v1
- ppo
- deep-reinforcement-learning
- reinforcement-learning
- custom-implementation
- deep-rl-class
model-index:
- name: PPO
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: CartPole-v1
      type: CartPole-v1
    metrics:
    - type: mean_reward
      value: 198.20 +/- 79.94
      name: mean_reward
      verified: false
---

  # PPO Agent Playing CartPole-v1

  This is a trained model of a PPO agent playing CartPole-v1.
  To learn to code your own PPO agent and train it Unit 8 of the Deep Reinforcement Learning Class: https://github.com/huggingface/deep-rl-class/tree/main/unit8
  
  # Hyperparameters
  ```python
  {'exp_name': 'train_new'
'seed': 1
'torch_deterministic': True
'cuda': True
'track': False
'wandb_project_name': 'cleanRL'
'wandb_entity': None
'capture_video': False
'env_id': 'CartPole-v1'
'total_timesteps': 50000
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
'repo_id': 'abhi762/ppo'
'batch_size': 512
'minibatch_size': 128}
  ```
  
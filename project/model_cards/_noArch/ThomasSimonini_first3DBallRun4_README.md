
---
      tags:
      - unity-ml-agents
      - ml-agents
      - deep-reinforcement-learning
      - reinforcement-learning
      - 3DBall
---
    
  # **ppo** Agent playing **3DBall**
  This is a trained model of a **ppo** agent playing **3DBall** using the [Unity ML-Agents Library](https://github.com/Unity-Technologies/ml-agents).
  
  ## Usage (with ML-Agents)
  TODO: Add your code
  
      ## Configuration file
      {'default_settings': None, 'behaviors': {'3DBall': {'trainer_type': 'ppo', 'hyperparameters': {'batch_size': 64, 'buffer_size': 12000, 'learning_rate': 0.0003, 'beta': 0.001, 'epsilon': 0.2, 'lambd': 0.99, 'num_epoch': 3, 'learning_rate_schedule': 'linear', 'beta_schedule': 'linear', 'epsilon_schedule': 'linear'}, 'network_settings': {'normalize': True, 'hidden_units': 128, 'num_layers': 2, 'vis_encode_type': 'simple', 'memory': None, 'goal_conditioning_type': 'hyper', 'deterministic': False}, 'reward_signals': {'extrinsic': {'gamma': 0.99, 'strength': 1.0, 'network_settings': {'normalize': False, 'hidden_units': 128, 'num_layers': 2, 'vis_encode_type': 'simple', 'memory': None, 'goal_conditioning_type': 'hyper', 'deterministic': False}}}, 'init_path': None, 'keep_checkpoints': 5, 'checkpoint_interval': 500000, 'max_steps': 500000, 'time_horizon': 1000, 'summary_freq': 12000, 'threaded': False, 'self_play': None, 'behavioral_cloning': None}}, 'env_settings': {'env_path': None, 'env_args': None, 'base_port': 5005, 'num_envs': 1, 'num_areas': 1, 'seed': -1, 'max_lifetime_restarts': 10, 'restarts_rate_limit_n': 1, 'restarts_rate_limit_period_s': 60}, 'engine_settings': {'width': 84, 'height': 84, 'quality_level': 5, 'time_scale': 20, 'target_frame_rate': -1, 'capture_frame_rate': 60, 'no_graphics': False}, 'environment_parameters': None, 'checkpoint_settings': {'run_id': 'first3DBallRun', 'initialize_from': None, 'load_model': False, 'resume': False, 'force': False, 'train_model': False, 'inference': False, 'results_dir': 'results'}, 'torch_settings': {'device': None}, 'debug': False}
      

---
      tags:
      - unity-ml-agents
      - ml-agents
      - deep-reinforcement-learning
      - reinforcement-learning
      - ML-Agents-SnowballTarget
      library_name: ml-agents
---
    
  # **ppo** Agent playing **SnowballTarget**
  This is a trained model of a **ppo** agent playing **SnowballTarget** using the [Unity ML-Agents Library](https://github.com/Unity-Technologies/ml-agents).
  
  ## Usage (with ML-Agents)
  The Documentation: https://github.com/huggingface/ml-agents#get-started
  We wrote a complete tutorial to learn to train your first agent using ML-Agents and publish it to the Hub:


  ### Resume the training
  ```
  mlagents-learn ./config/ppo/SnowballTarget.yaml --run-id="SnowballTarget-v1" --resume
  ```
  ### Training hyperparameters
  ```python
  behaviors:
  SnowballTarget:
    trainer_type: ppo
    summary_freq: 10000
    keep_checkpoints: 5
    checkpoint_interval: 50000
    max_steps: 900000
    time_horizon: 128
    threaded: true
    hyperparameters:
      learning_rate: 0.0001
      learning_rate_schedule: linear
      batch_size: 128
      buffer_size: 4096
      beta: 0.005
      epsilon: 0.2
      lambd: 0.95
      num_epoch: 5
    network_settings:
      normalize: false
      hidden_units: 256
      num_layers: 3
      vis_encode_type: simple
    reward_signals:
      extrinsic:
        gamma: 0.99
        strength: 1.0
  ```

  ### Watch your Agent play
  You can watch your agent **playing directly in your browser:**.
  
  1. Go to https://huggingface.co/spaces/unity/ML-Agents-SnowballTarget
  2. Step 1: Write your model_id: kinkpunk/PPO-SnowballTarget
  3. Step 2: Select your *.nn /*.onnx file
  4. Click on Watch the agent play 👀
  
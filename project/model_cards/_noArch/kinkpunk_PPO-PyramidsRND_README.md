
---
      tags:
      - unity-ml-agents
      - ml-agents
      - deep-reinforcement-learning
      - reinforcement-learning
      - ML-Agents-Pyramids
      library_name: ml-agents
---
    
  # **ppo** Agent playing **Pyramids**
  This is a trained model of a **ppo** agent playing **Pyramids** using the [Unity ML-Agents Library](https://github.com/Unity-Technologies/ml-agents).
  
  ## Usage (with ML-Agents)
  The Documentation: https://github.com/huggingface/ml-agents#get-started
  We wrote a complete tutorial to learn to train your first agent using ML-Agents and publish it to the Hub:


  ### Resume the training
  ```
  mlagents-learn ./config/ppo/PyramidsRND.yaml --run-id="Pyramids-Training" --resume
  ```
  ### Training hyperparameters
  ```python
  behaviors:
  Pyramids:
    trainer_type: ppo
    hyperparameters:
      batch_size: 128
      buffer_size: 4096
      learning_rate: 0.0003
      beta: 0.01
      epsilon: 0.2
      lambd: 0.95
      num_epoch: 3
      learning_rate_schedule: linear
    network_settings:
      normalize: false
      hidden_units: 512
      num_layers: 3
      vis_encode_type: simple
    reward_signals:
      extrinsic:
        gamma: 0.99
        strength: 1.0
      rnd:
        gamma: 0.99
        strength: 0.01
        network_settings:
          hidden_units: 128
          num_layers: 3
        learning_rate: 0.0001
    keep_checkpoints: 5
    max_steps: 900000
    time_horizon: 256
    summary_freq: 30000
  ```

  ### Watch your Agent play
  You can watch your agent **playing directly in your browser:**.
  
  1. Go to https://huggingface.co/spaces/unity/ML-Agents-Pyramids
  2. Step 1: Write your model_id: kinkpunk/PPO-PyramidsRND
  3. Step 2: Select your *.nn /*.onnx file
  4. Click on Watch the agent play 👀
  
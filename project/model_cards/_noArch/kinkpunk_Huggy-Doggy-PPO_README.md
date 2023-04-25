
---
      tags:
      - unity-ml-agents
      - ml-agents
      - deep-reinforcement-learning
      - reinforcement-learning
      - ML-Agents-Huggy
      library_name: ml-agents
---
    
  # **ppo** Agent playing **Huggy**
  This is a trained model of a **ppo** agent playing **Huggy** using the [Unity ML-Agents Library](https://github.com/Unity-Technologies/ml-agents).
  
  ## Usage (with ML-Agents)
  The Documentation: https://github.com/huggingface/ml-agents#get-started
  We wrote a complete tutorial to learn to train your first agent using ML-Agents and publish it to the Hub:


  ### Resume the training
  ```
  mlagents-learn "./Huggy-Doggy-PPO/configuration.yaml" --run-id="Huggy-Doggy" --resume
  ```
  ### Watch my Agent play
  You can watch my agent **playing directly in your browser:**.
  
  1. Go to https://huggingface.co/spaces/ThomasSimonini/Huggy
  2. Step 1: Write my model_id: **kinkpunk/Huggy-Doggy-PPO**
  3. Step 2: Select any *.nn /*.onnx file
  4. Click on Watch the agent play 👀
  
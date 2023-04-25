
---
      tags:
      - unity-ml-agents
      - ml-agents
      - deep-reinforcement-learning
      - reinforcement-learning
      - ML-Agents-PushBlock
      library_name: ml-agents
---
    
  # **ppo** Agent playing **PushBlock**
  This is a trained model of a **ppo** agent playing **PushBlock** using the [Unity ML-Agents Library](https://github.com/Unity-Technologies/ml-agents).
  
  ## Usage (with ML-Agents)
  The Documentation: https://github.com/huggingface/ml-agents#get-started
  We wrote a complete tutorial to learn to train your first agent using ML-Agents and publish it to the Hub:


  ### Resume the training
  ```
  mlagents-learn <your_configuration_file_path.yaml> --run-id=<run_id> --resume
  ```
  ### Watch your Agent play
  You can watch your agent **playing directly in your browser:**.
  
  1. Go to https://huggingface.co/spaces/unity/ML-Agents-PushBlock
  2. Step 1: Write your model_id: rebolforces/ppo-pushblock-9M
  3. Step 2: Select your *.nn /*.onnx file
  4. Click on Watch the agent play 👀
  
  ### Stats
  ```
"final_checkpoint": {
    "steps": 9000019,
    "file_path": "results/PushBlock Training 2/PushBlock.onnx",
    "reward": 4.981160132090251,
    "creation_time": 1661076513.4570658,
    "auxillary_file_paths": [
      "results/PushBlock Training 2/PushBlock/PushBlock-9000019.pt"
    ]
}
 ```       
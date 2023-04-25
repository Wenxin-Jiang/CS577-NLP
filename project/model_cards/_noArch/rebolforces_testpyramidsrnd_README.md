
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
  mlagents-learn <your_configuration_file_path.yaml> --run-id=<run_id> --resume
  ```
  ### Watch your Agent play
  You can watch your agent **playing directly in your browser:**.
  
  1. Go to https://huggingface.co/spaces/unity/ML-Agents-Pyramids
  2. Step 1: Write your model_id: rebolforces/testpyramidsrnd
  3. Step 2: Select your *.nn /*.onnx file
  4. Click on Watch the agent play 👀
  
  ### Stats
```
"final_checkpoint": {
     "steps": 3000022,
     "file_path": "results/Pyramids Training2/Pyramids.onnx",
     "reward": 1.87466665605704,
     "creation_time": 1660985715.2452054,
     "auxillary_file_paths": [
         "results/Pyramids Training2/Pyramids/Pyramids-3000022.pt"
     ]
}
```
  
  
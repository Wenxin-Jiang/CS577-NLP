
---
      tags:
      - unity-ml-agents
      - ml-agents
      - deep-reinforcement-learning
      - reinforcement-learning
      - ML-Agents-Huggy
      library_name: ml-agents
---
    
  # **ppo** Agent playing **Huggy** 🐶
  This is a trained model of a **ppo** agent playing **Huggy** using the [Unity ML-Agents Library](https://github.com/Unity-Technologies/ml-agents).
  
  ## Usage (with ML-Agents)
  ### Resume the training
  ```
  mlagents-learn <your_configuration_file_path.yaml> --run-id=<run_id> --resume
  ```
  ### Watch your Agent
  1. Move your model file into the environment Project
  2. Open the Unity Editor, and select the scene.
  3. Select the prefab Agent object.
  4. Drag the <behavior_name>.onnx file from the Project window of the Editor to the Model placeholder in the Agent inspector window.
  5. Press the Play button at the top of the Editor.
  
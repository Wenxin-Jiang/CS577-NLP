---
tags:
- Taxi-v3
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: Taxi-v3
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Taxi-v3
      type: Taxi-v3
    metrics:
    - type: mean_reward
      value: 7.56 +/- 2.71
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing **Taxi-v3**
  This is a trained model of a **Q-Learning** agent playing **Taxi-v3** .

  ## Usage

  ```python
  from huggingface_hub import hf_hub_download
  import pickle5 as pickle

  model_file = hf_hub_download(repo_id="atorre/Taxi-v3", filename="q-learning.pkl")
  with open(model_file, 'rb') as f:
      model = pickle.load(f)
  
  env = gym.make(model["env_id"])
  ```
  
---
tags:
- Taxi-v3-4x4-no_slippery
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: q-Taxi-v3
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Taxi-v3-4x4-no_slippery
      type: Taxi-v3-4x4-no_slippery
    metrics:
    - type: mean_reward
      value: 1.00 +/- 0.00
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing1 **Taxi-v3**
  This is a trained model of a **Q-Learning** agent playing **Taxi-v3** .

  ## Usage

  ```python
  
  model = load_from_hub(repo_id="huam/q-Taxi-v3", filename="q-learning.pkl")

  # Don't forget to check if you need to add additional attributes (is_slippery=False etc)
  env = gym.make(model["env_id"])
  ```
  
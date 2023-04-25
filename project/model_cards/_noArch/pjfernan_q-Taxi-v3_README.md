---
tags:
- FrozenLake-v1
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
      name: FrozenLake-v1
      type: FrozenLake-v1
    metrics:
    - type: mean_reward
      value: 7.88 +/- 2.70
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing1 **FrozenLake-v1**
  This is a trained model of a **Q-Learning** agent playing **FrozenLake-v1** .

  ## Usage

  ```python
  
  model = load_from_hub(repo_id="pjfernan/q-Taxi-v3", filename="q-learning.pkl")

  # Don't forget to check if you need to add additional attributes (is_slippery=False etc)
  env = gym.make(model["env_id"])
  ```
  
---
tags:
- q-learning
- reinforcement-learning
- custom-implementation
- FrozenLake-v1-4x4-no_slippery
model-index:
- name: QLearning_FrozenLake-v1
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: FrozenLake-v1-4x4-no_slippery
      type: FrozenLake-v1-4x4-no_slippery
    metrics:
    - type: mean_reward
      value: 1.00 +/- 0.00
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing1 **FrozenLake-v1**
  This is a trained model of a **Q-Learning** agent playing **FrozenLake-v1** .

  ## Usage

  ```python
  
  model = load_from_hub(repo_id="chavicoski/QLearning-FrozenLake-v1-4x4-noSlippery", filename="QLearning_FrozenLake-v1-4x4-noSlippery.pkl")

  # Don't forget to check if you need to add additional attributes (is_slippery=False etc)
  env = gym.make("FrozenLake-v1")
  ```
  
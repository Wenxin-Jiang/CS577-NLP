---
tags:
- FrozenLake-v1-8x8-no_slippery
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: q-FrozenLake-v1-8x8-noSlippery
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: FrozenLake-v1-8x8-no_slippery
      type: FrozenLake-v1-8x8-no_slippery
    metrics:
    - type: mean_reward
      value: 1.00 +/- 0.00
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing **FrozenLake-v1**
  This is a trained model of a **Q-Learning** agent playing **FrozenLake-v1** .

  ## Usage

  ```python
  
  model = load_from_hub(repo_id="MichalJ/q-FrozenLake-v1-8x8-noSlippery", filename="q-learning.pkl")

  ```
  
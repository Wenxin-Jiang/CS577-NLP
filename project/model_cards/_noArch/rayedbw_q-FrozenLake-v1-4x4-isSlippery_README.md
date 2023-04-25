---
tags:
- FrozenLake-v1-4x4-is_slippery
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: q-FrozenLake-v1-4x4-isSlippery
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: FrozenLake-v1-4x4-is_slippery
      type: FrozenLake-v1-4x4-is_slippery
    metrics:
    - type: mean_reward
      value: 0.62 +/- 0.49
      name: mean_reward
      verified: false
---

    # **Q-Learning** Agent playing1 **FrozenLake-v1**
    This is a trained model of a **Q-Learning** agent playing **FrozenLake-v1** .

    ## Usage

    ```python

    model = load_from_hub(repo_id="rayedbw/q-FrozenLake-v1-4x4-isSlippery", filename="q-learning.pkl")

    # Don't forget to check if you need to add additional attributes (is_slippery=False etc)
    env = gym.make(model["env_id"])
    ```
    
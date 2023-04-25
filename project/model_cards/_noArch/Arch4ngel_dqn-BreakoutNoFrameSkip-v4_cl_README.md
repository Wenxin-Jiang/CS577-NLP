---
tags:
- BreakoutNoFrameskip-v4
- dqn
- reinforcement-learning
- custom-implementation
model-index:
- name: dqn-BreakoutNoFrameSkip-v4_cl
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: BreakoutNoFrameskip-v4
      type: BreakoutNoFrameskip-v4
    metrics:
    - type: mean_reward
      value: 3.20 +/- 1.99
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing1 **BreakoutNoFrameskip-v4**
  This is a trained model of a **Q-Learning** agent playing **BreakoutNoFrameskip-v4** .

  ## Usage

  ```python
  
  model = load_from_hub(repo_id="Arch4ngel/dqn-BreakoutNoFrameSkip-v4_cl", filename="dqn.pkl")

  # Don't forget to check if you need to add additional attributes (is_slippery=False etc)
  env = gym.make(model["env_id"])
  ```
  
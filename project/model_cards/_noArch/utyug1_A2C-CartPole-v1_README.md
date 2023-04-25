---
tags:
- CartPole-v1
- reinforcement-learning
model-index:
- name: A2C-CartPole-v1
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: CartPole-v1
      type: CartPole-v1
    metrics:
    - type: mean_reward
      value: 500.00 +/- 0.00
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing1 **CartPole-v1**
  This is a trained model of a **Q-Learning** agent playing **CartPole-v1** .

  ## Usage

  ```python
  
  model = load_from_hub(repo_id="utyug1/A2C-CartPole-v1", filename="model.pt")

  ```
  
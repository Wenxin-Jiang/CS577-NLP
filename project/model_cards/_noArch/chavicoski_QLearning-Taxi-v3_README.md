---
tags:
- q-learning
- reinforcement-learning
- custom-implementation
- Taxi-v3
model-index:
- name: QLearning_Taxi-v3
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

  # **Q-Learning** Agent playing1 **Taxi-v3**
  This is a trained model of a **Q-Learning** agent playing **Taxi-v3** .

  ## Usage

  ```python
  
  model = load_from_hub(repo_id="chavicoski/QLearning-Taxi-v3", filename="QLearning_Taxi-v3.pkl")

  # Don't forget to check if you need to add additional attributes (is_slippery=False etc)
  env = gym.make("Taxi-v3")
  ```
  
---
tags:
- Taxi-v3
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: hf-drl-course-2-q-Taxi-v3_1
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Taxi-v3
      type: Taxi-v3
    metrics:
    - type: mean_reward
      value: 7.52 +/- 2.62
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing1 **Taxi-v3**
  This is a trained model of a **Q-Learning** agent playing **Taxi-v3** .

  ## Usage

  ```python
  
  model = load_from_hub(repo_id="mbertheau/hf-drl-course-2-q-Taxi-v3_1", filename="q-learning.pkl")

  # Don't forget to check if you need to add additional attributes (is_slippery=False etc)
  env = gym.make(model["env_id"])
  ```
  
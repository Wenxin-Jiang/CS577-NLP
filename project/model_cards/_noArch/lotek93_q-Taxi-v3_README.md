---
tags:
- Taxi-v3
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
      name: Taxi-v3
      type: Taxi-v3
    metrics:
    - type: mean_reward
      value: 7.54 +/- 2.73
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing **Taxi-v3**
  This is a trained model of a **Q-Learning** agent playing **Taxi-v3** .
  
  ## Usage
  ```python
  model = load_from_hub(repo_id="lotek93/q-Taxi-v3", filename="q-learning.pkl")

  # Don't forget to check if you need to add additional attributes (is_slippery=False etc)
  env = gym.make(model["env_id"])

  evaluate_agent(env, model["max_steps"], model["n_eval_episodes"], model["qtable"], model["eval_seed"])
  
  ```
  
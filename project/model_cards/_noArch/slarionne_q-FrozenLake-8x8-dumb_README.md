---
tags:
- FrozenLake-v1-8x8
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: q-FrozenLake-8x8-dumb
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: FrozenLake-v1-8x8
      type: FrozenLake-v1-8x8
    metrics:
    - type: mean_reward
      value: 0.00 +/- 0.00
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing **FrozenLake-v1**
  This is a trained model of a **Q-Learning** agent playing **FrozenLake-v1** .
  
  ## Usage
  ```python
  model = load_from_hub(repo_id="slarionne/q-FrozenLake-8x8-dumb", filename="q-learning.pkl")

  # Don't forget to check if you need to add additional attributes (is_slippery=False etc)
  env = gym.make(model["env_id"])

  evaluate_agent(env, model["max_steps"], model["n_eval_episodes"], model["qtable"], model["eval_seed"])
  
  ```
  
---
tags:
- FrozenLake-v1-8x8-no_slippery
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: q-FrozenLake-v1-8x8-no_slippery
  results:
  - metrics:
    - type: mean_reward
      value: nan +/- nan
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: FrozenLake-v1-8x8-no_slippery
      type: FrozenLake-v1-8x8-no_slippery
---

  # **Q-Learning** Agent playing **FrozenLake-v1**
  This is a trained model of a **Q-Learning** agent playing **FrozenLake-v1** .
  
  ## Usage
  ```python
  model = load_from_hub(repo_id="DBusAI/q-FrozenLake-v1-8x8-no_slippery", filename="q-learning.pkl")

  # Don't forget to check if you need to add additional attributes (is_slippery=False etc)
  env = gym.make(model["env_id"])

  evaluate_agent(env, model["max_steps"], model["n_eval_episodes"], model["qtable"], model["eval_seed"])
  
  ```
  
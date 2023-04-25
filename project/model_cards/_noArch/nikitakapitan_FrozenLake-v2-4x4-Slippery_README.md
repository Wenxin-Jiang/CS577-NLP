---
tags:
- FrozenLake-v1-4x4
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: FrozenLake-v2-4x4-Slippery
  results:
  - metrics:
    - type: mean_reward
      value: 0.73 +/- 0.45
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: FrozenLake-v1-4x4
      type: FrozenLake-v1-4x4
---

  # **Q-Learning** Agent playing **FrozenLake-v2-4x4-Slippery**
  This is a trained model of a **Q-Learning** agent playing **FrozenLake-v2-4x4-Slippery** .
  
  ## Usage
  ```python
  model = load_from_hub(repo_id="nikitakapitan/FrozenLake-v2-4x4-Slippery", filename="q-learning.pkl")

  # Don't forget to check if you need to add additional attributes (is_slippery=False etc)
  env = gym.make(model["env_id"])

  evaluate_agent(env, model["max_steps"], model["n_eval_episodes"], model["qtable"], model["eval_seed"])
  
  ```
  
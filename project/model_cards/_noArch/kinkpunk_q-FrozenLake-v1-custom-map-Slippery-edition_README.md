---
tags:
- FrozenLake-v1-4x4
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: q-FrozenLake-v1-custom-map-Slippery-edition
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: FrozenLake-v1-4x4
      type: FrozenLake-v1-4x4
    metrics:
    - type: mean_reward
      value: 0.89 +/- 0.31
      name: mean_reward
      verified: false
---

  # **Q-Learning** Agent playing1 **FrozenLake-v1**
  This is a trained model of a **Q-Learning** agent playing **FrozenLake-v1** .

  ## Usage

  ```python
  
  model = load_from_hub(repo_id="kinkpunk/q-FrozenLake-v1-custom-map-Slippery-edition",
                        filename="q-learning.pkl")

  # Don't forget to change additional attributes
  # when you create environment using 4x4 map
  env = gym.make('FrozenLake-v1',
                  desc=["SFFF", "FHHF", "FFHF", "HFFG"],
                  is_slippery=True)
  ```
  
  ## Training parameters

  ```python
  # Training parameters
  n_training_episodes = 105000  # Total training episodes
  learning_rate = 0.8          # Learning rate

  # Evaluation parameters
  n_eval_episodes = 100        # Total number of test episodes

  # Environment parameters
  env_id = "FrozenLake-v1"     # Name of the environment
  max_steps = 99               # Max steps per episode
  gamma = 0.98                 # Discounting rate
  eval_seed = []               # The evaluation seed of the environment

  # Exploration parameters
  max_epsilon = 0.99            # Exploration probability at start
  min_epsilon = 0.02            # Minimum exploration probability 
  decay_rate = 0.009            # Exponential decay rate for exploration prob
  
  ```
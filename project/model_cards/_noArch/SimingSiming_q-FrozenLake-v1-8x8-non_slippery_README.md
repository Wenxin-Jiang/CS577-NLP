---
tags:
- FrozenLake-v1-8x8-no_slippery
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: q-FrozenLake-v1-8x8-non_slippery
  results:
  - metrics:
    - type: mean_reward
      value: 1.00 +/- 0.00
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
  

n_training_episodes = 200000  # Total training episodes <br>
learning_rate = 0.8          # Learning rate <br>

# Evaluation parameters
n_eval_episodes = 100        # Total number of test episodes <br>

# Environment parameters <br>
env_id = "FrozenLake-v1"     # Name of the environment <br>
max_steps = 100               # Max steps per episode <br>
gamma = 0.99                 # Discounting rate <br>
eval_seed = []               # The evaluation seed of the environment <br>

# Exploration parameters <br>
epsilon = 1.0                 # Exploration rate <br>
max_epsilon = 1.0             # Exploration probability at start <br>
min_epsilon = 0.05            # Minimum exploration probability <br>
decay_rate = 0.00005            # Exponential decay rate for exploration prob <br>
  
  ```
  
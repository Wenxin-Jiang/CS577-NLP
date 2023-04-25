---
tags:
- FrozenLake-v1-4x4-no_slippery
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: q-FrozenLake-v1-4x4-noSlippery
  results:
  - metrics:
    - type: mean_reward
      value: 1.00 +/- 0.00
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: FrozenLake-v1-4x4-no_slippery
      type: FrozenLake-v1-4x4-no_slippery
---

      # 使用**Q-Learning**智能体来玩**FrozenLake-v1**
      这是一个使用**Q-Learning**训练有素的模型玩**FrozenLake-v1**.
      
      ## 用法
      ```python
      model = load_from_hub(repo_id='sun1638650145/q-FrozenLake-v1-4x4-noSlippery', filename='q-learning.pkl')

      # 不要忘记检查是否需要添加额外的参数(例如is_slippery=False)
      env = gym.make(model['env_id'])

      evaluate_agent(env, model['max_steps'], model['n_eval_episodes'], model['qtable'], model['eval_seed'])
      
      ```
      
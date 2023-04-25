---
tags:
- Taxi-v3
- q-learning
- reinforcement-learning
- custom-implementation
model-index:
- name: q-Taxi-v3
  results:
  - metrics:
    - type: mean_reward
      value: 7.54 +/- 2.73
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Taxi-v3
      type: Taxi-v3
---

      # 使用**Q-Learning**智能体来玩**Taxi-v3**
      这是一个使用**Q-Learning**训练有素的模型玩**Taxi-v3**.
      
      ## 用法
      ```python
      model = load_from_hub(repo_id='sun1638650145/q-Taxi-v3', filename='q-learning.pkl')

      # 不要忘记检查是否需要添加额外的参数(例如is_slippery=False)
      env = gym.make(model['env_id'])

      evaluate_agent(env, model['max_steps'], model['n_eval_episodes'], model['qtable'], model['eval_seed'])
      
      ```
      
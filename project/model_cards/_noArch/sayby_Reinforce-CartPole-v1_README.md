---
tags:
- CartPole-v1
- reinforce
- reinforcement-learning
- custom-implementation
- deep-rl-class
model-index:
- name: Reinforce-CartPole-v1
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: CartPole-v1
      type: CartPole-v1
    metrics:
    - type: mean_reward
      value: 109.92 +/- 16.87
      name: mean_reward
      verified: false
---
# **Q-Learning** Agent playing **CartPole-v1**

This is a trained model of a **Reinforce** agent playing **CartPole-v1** .

## Usage

```python

model = load_from_hub(repo_id="sayby/Reinforce-CartPole-v1", filename="model.pt")

# Don't forget to check if you need to add additional attributes (is_slippery=False etc)

env = gym.make(model["env_id"])

evaluate_agent(env, model["max_steps"], model["n_eval_episodes"], model["eval_seed"])

 
```
      
---
tags:
- LunarLanderContinuous-v2
- reinforce
- reinforcement-learning
- custom-implementation
model-index:
- name: REINFORCE-LunarLanderContinuous-v2
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLanderContinuous-v2
      type: LunarLanderContinuous-v2
    metrics:
    - type: mean_reward
      value: 264.10 +/- 37.17
      name: mean_reward
      verified: false
---

# **Reinforce** Agent playing **LunarLanderContinuous-v2**
This is a custom REINFORCE RL agent. Performance has been measured over 900 episodes.
To try the agent, user needs to import the `ParameterisedPolicy` class from the agent_class.py file. </br>
Training progress:
![training](training_graph.jpg)

Numbers on X axis are average over 40 episodes, each lasting for about 500 timesteps on average. So in total the agent was trained over about 5e6 timesteps.
Learning rate decay schedule: <code>torch.optim.lr_scheduler.StepLR(opt, step_size=4000, gamma=0.7)</code>. Training code is shown in the training.py file for reference.

In case video demo does not work, here's a gif:
![replay](replay.gif)

Minimal code to use the agent:</br>
```
import gym
from agent_class import ParameterisedPolicy

env_name = 'LunarLanderContinuous-v2'
env = gym.make(env_name)
agent = torch.load('best_reinforce_lunar_lander_cont_model_269.402.pt')
render = True

observation = env.reset()
while True:
    if render:
        env.render()
    action = agent.act(observation)
    observation, reward, done, info = env.step(action)
    
    if done:
        break
env.close()
```
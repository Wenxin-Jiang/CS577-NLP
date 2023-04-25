---
tags:
- gym
- reinforcement-learning
---


# TestSB3/ppo-CartPole-v1

This is a trained model of a PPO agent playing CartPole-v1 using the [rl-baselines3-zoo](https://github.com/DLR-RM/rl-baselines3-zoo) library.

## Usage (with RL-baselines3-zoo)

Just clone the [rl-baselines3-zoo](https://github.com/DLR-RM/rl-baselines3-zoo) library.

Then run:

```python
python  enjoy.py --algo ppo --env CartPole-v1
```
## Evaluation Results

Mean Reward: 500.0 +/- 0.0 (300 test episodes)

## Citing the Project
To cite this repository in publications:

```
@misc{rl-zoo3,
  author = {Raffin, Antonin},
  title = {RL Baselines3 Zoo},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/DLR-RM/rl-baselines3-zoo}},
}
```
---
library_name: stable-baselines3
tags:
- SpaceInvadersNoFrameskip-v4
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: DQN
  results:
  - metrics:
    - type: mean_reward
      value: 581.50 +/- 104.72
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: SpaceInvadersNoFrameskip-v4
      type: SpaceInvadersNoFrameskip-v4
---

# **DQN** Agent playing **SpaceInvadersNoFrameskip-v4**
This is a trained model of a **DQN** agent playing **SpaceInvadersNoFrameskip-v4**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## Usage (with Stable-baselines3)

```python
 from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from huggingface_sb3 import load_from_hub, package_to_hub
from stable_baselines3.common.utils import set_random_seed

env_id = "SpaceInvadersNoFrameskip-v4"

env = make_atari_env(env_id,
                     n_envs=12,
                     # Improving reproducibility
                     seed=1)
env = VecFrameStack(env, n_stack=4)  # Stack last four images

# Improving reproducibility
set_random_seed(42)

# Using these parameters as default: https://huggingface.co/micheljperez/dqn-SpaceInvadersNoFrameskip-v4
model = DQN(policy = "CnnPolicy",
            env = env,
            batch_size = 32,
            buffer_size = 100_000,
            exploration_final_eps = 0.01,
            exploration_fraction = 0.025,
            gradient_steps = 1,
            learning_rate = 1e-4,
            learning_starts = 100_000,
            optimize_memory_usage = True,
            replay_buffer_kwargs = {"handle_timeout_termination": False},
            target_update_interval = 1000,
            train_freq = 4,
            # normalize = False,
            tensorboard_log = "./tensorboard",
            verbose=1
           )
           
f = load_from_hub('masterdezign/dqn2-SpaceInvadersNoFrameskip-v4', 'dqn-SpaceInvadersNoFrameskip-v4.zip')
model = model.load(f)

mean_reward, std_reward = evaluate_policy(model, env)
print(f"Mean reward = {mean_reward:.2f} +/- {std_reward:.2f}")
```

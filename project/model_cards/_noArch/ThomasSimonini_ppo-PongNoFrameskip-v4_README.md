---
tags:
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
- atari
model-index:
- name: PPO Agent
  results:
  - task: 
      type: reinforcement-learning  # Required. Example: automatic-speech-recognition
    dataset:
      type: PongNoFrameskip-v4  # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: PongNoFrameskip-v4  # Required. Example: Common Voice zh-CN
    metrics:
      - type: mean_reward    # Required. Example: wer
        value: 21  # Required. Example: 20.90
---
# PPO Agent playing PongNoFrameskip-v4
This is a trained model of a **PPO agent playing PongNoFrameskip-v4 using the [stable-baselines3 library](https://stable-baselines3.readthedocs.io/en/master/index.html)** (our agent is the 🟢 one).

The training report: https://wandb.ai/simoninithomas/HFxSB3/reports/Atari-HFxSB3-Benchmark--VmlldzoxNjI3NTIy


## Evaluation Results
Mean_reward: `21.00 +/- 0.0`

# Usage (with Stable-baselines3)
- You need to use `gym==0.19` since it **includes Atari Roms**.
- The Action Space is 6 since we use only **possible actions in this game**.


Watch your agent interacts :

```python
# Import the libraries
import os 

import gym

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import VecNormalize

from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack

from huggingface_sb3 import load_from_hub, push_to_hub

# Load the model
checkpoint = load_from_hub("ThomasSimonini/ppo-PongNoFrameskip-v4", "ppo-PongNoFrameskip-v4.zip")

# Because we using 3.7 on Colab and this agent was trained with 3.8 to avoid Pickle errors:
custom_objects = {
            "learning_rate": 0.0,
            "lr_schedule": lambda _: 0.0,
            "clip_range": lambda _: 0.0,
        }

model= PPO.load(checkpoint, custom_objects=custom_objects)

env = make_atari_env('PongNoFrameskip-v4', n_envs=1)
env = VecFrameStack(env, n_stack=4)

obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
```


## Training Code
```python
import wandb
import gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack, VecVideoRecorder
from stable_baselines3.common.callbacks import CheckpointCallback

from wandb.integration.sb3 import WandbCallback

from huggingface_sb3 import load_from_hub, push_to_hub

config = {
    "env_name": "PongNoFrameskip-v4",
    "num_envs": 8,
    "total_timesteps": int(10e6),
    "seed": 4089164106,    
}

run = wandb.init(
    project="HFxSB3",
    config = config,
    sync_tensorboard = True,  # Auto-upload sb3's tensorboard metrics
    monitor_gym = True, # Auto-upload the videos of agents playing the game
    save_code = True, # Save the code to W&B
    )

# There already exists an environment generator
# that will make and wrap atari environments correctly.
# Here we are also multi-worker training (n_envs=8 => 8 environments)
env = make_atari_env(config["env_name"], n_envs=config["num_envs"], seed=config["seed"]) #PongNoFrameskip-v4

print("ENV ACTION SPACE: ", env.action_space.n)

# Frame-stacking with 4 frames
env = VecFrameStack(env, n_stack=4)
# Video recorder
env = VecVideoRecorder(env, "videos", record_video_trigger=lambda x: x % 100000 == 0, video_length=2000)

# https://github.com/DLR-RM/rl-trained-agents/blob/10a9c31e806820d59b20d8b85ca67090338ea912/ppo/PongNoFrameskip-v4_1/PongNoFrameskip-v4/config.yml
model = PPO(policy = "CnnPolicy",
            env = env,
            batch_size = 256,
            clip_range = 0.1,
            ent_coef = 0.01,
            gae_lambda = 0.9,
            gamma = 0.99,
            learning_rate = 2.5e-4,
            max_grad_norm = 0.5,
            n_epochs = 4,
            n_steps = 128,
            vf_coef = 0.5,
            tensorboard_log = f"runs",
            verbose=1,
            )
    
model.learn(
    total_timesteps = config["total_timesteps"],
    callback = [
        WandbCallback(
        gradient_save_freq = 1000,
        model_save_path = f"models/{run.id}",
        ), 
        CheckpointCallback(save_freq=10000, save_path='./pong',
                                         name_prefix=config["env_name"]),
        ]
)

model.save("ppo-PongNoFrameskip-v4.zip")
push_to_hub(repo_id="ThomasSimonini/ppo-PongNoFrameskip-v4", 
    filename="ppo-PongNoFrameskip-v4.zip",
    commit_message="Added Pong trained agent")
```
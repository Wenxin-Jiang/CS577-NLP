---
library_name: stable-baselines3
tags:
- LunarLander-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: PPO
  results:
  - task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLander-v2
      type: LunarLander-v2
    metrics:
    - type: mean_reward
      value: 298.48 +/- 12.14
      name: mean_reward
      verified: false
---

# Train your first Deep Reinforcement Learning Agent 🤖
![Cover](https://github.com/huggingface/deep-rl-class/blob/main/unit1/assets/img/thumbnail.png?raw=true)

This is a trained model of a **PPO** agent playing **LunarLander-v2**
using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).

## 1. Install package
```python
from IPython.display import clear_output
!apt install swig cmake
!pip install -r https://raw.githubusercontent.com/huggingface/deep-rl-class/main/notebooks/unit1/requirements-unit1.txt
!sudo apt-get update
!apt install python-opengl
!apt install ffmpeg
!apt install xvfb
!pip3 install pyvirtualdisplay
clear_output()
```

Restart notebook
```
import os
os.kill(os.getpid(), 9)
```

## 2. Use model

```python
from huggingface_sb3 import load_from_hub
repo_id = "thien1892/LunarLander-v2-ppo-5m"
filename = "ppo-LunarLander-v2-5m.zip" # The model filename.zip

# When the model was trained on Python 3.8 the pickle protocol is 5
# But Python 3.6, 3.7 use protocol 4
# In order to get compatibility we need to:
# 1. Install pickle5 (we done it at the beginning of the colab)
# 2. Create a custom empty object we pass as parameter to PPO.load()
custom_objects = {
            "learning_rate": 0.0,
            "lr_schedule": lambda _: 0.0,
            "clip_range": lambda _: 0.0,
}

checkpoint = load_from_hub(repo_id, filename)
model = PPO.load(checkpoint, custom_objects=custom_objects, print_system_info=True)
```
Evaluate
```python
eval_env = gym.make("LunarLander-v2")
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True)
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")
```

## 3. Re-train model (Optional 1)

```python
# Load a saved LunarLander model from the Hub and retrain
import gym
from huggingface_sb3 import load_from_hub, package_to_hub, push_to_hub
from huggingface_hub import notebook_login # To log to our Hugging Face account to be able to upload models to the Hub.
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import DummyVecEnv

repo_id = "thien1892/LunarLander-v2-ppo-v5"
filename = "ppo-LunarLander-v2.zip" # The model filename.zip
checkpoint = load_from_hub(repo_id, filename)

myenv = make_vec_env('LunarLander-v2', n_envs=16)
custom_objects = {
            "learning_rate": 1e-5,
            "clip_range": lambda _: 0.15,
}
model = PPO.load(checkpoint, reset_num_timesteps=True, print_system_info=True,custom_objects = custom_objects, env = myenv)

# Train it for 1,000,000 timesteps
model.learn(total_timesteps=1000000)
# Save the model
model_name = "ppo-LunarLander-v2-5m"
model.save(model_name)

# Evaluate
eval_env = gym.make("LunarLander-v2")
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10, deterministic=True)
print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")
```

Pust to HF hub

```python
notebook_login()
!git config --global credential.helper store
```

```
## repo_id is the id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name} for instance ThomasSimonini/ppo-LunarLander-v2
repo_id = "thien1892/LunarLander-v2-ppo-5m"

# TODO: Define the name of the environment
env_id = "LunarLander-v2"

# Create the evaluation env
eval_env = DummyVecEnv([lambda: gym.make(env_id)])


# TODO: Define the model architecture we used
model_architecture = "PPO"

## TODO: Define the commit message
commit_message = "Upload PPO LunarLander-v2 trained agent"

# method save, evaluate, generate a model card and record a replay video of your agent before pushing the repo to the hub
package_to_hub(model=model, # Our trained model
               model_name=model_name, # The name of our trained model 
               model_architecture=model_architecture, # The model architecture we used: in our case PPO
               env_id=env_id, # Name of the environment
               eval_env=eval_env, # Evaluation Environment
               repo_id=repo_id, # id of the model repository from the Hugging Face Hub (repo_id = {organization}/{repo_name} for instance ThomasSimonini/ppo-LunarLander-v2
               commit_message=commit_message)
```

## 4. Re-train model (Optional 2)
- Change `--repo_id` become your repo id :)
- `--id_retrain` and `--filename_retrain` in order to load my trained model, you can change to your trained model
```python
!python train_and_push.py --repo_id "thien1892/LunarLander-v2-ppo-v3" \
--commit_message "retrain model from hub 5m" \
--id_retrain "thien1892/LunarLander-v2-ppo-v5" \
--filename_retrain "ppo-LunarLander-v2.zip" \
--total_timesteps 2000000 \
--learning_rate 3e-5 \
--n_envs 64
```
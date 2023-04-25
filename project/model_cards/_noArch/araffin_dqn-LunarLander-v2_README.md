---
library_name: stable-baselines3
tags:
- LunarLander-v2
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: DQN
  results:
  - metrics:
    - type: mean_reward
      value: 280.22 +/- 13.03
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: LunarLander-v2
      type: LunarLander-v2
---

  # **DQN** Agent playing **LunarLander-v2**
  This is a trained model of a **DQN** agent playing **LunarLander-v2** using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).
  
## Usage (with Stable-Baselines3)
  
```python
from huggingface_sb3 import load_from_hub
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy

# Download checkpoint
checkpoint = load_from_hub("araffin/dqn-LunarLander-v2", "dqn-LunarLander-v2.zip")
# Remove warning
kwargs = dict(target_update_interval=30)
# Load the model
model = DQN.load(checkpoint, **kwargs)

env = make_vec_env("LunarLander-v2", n_envs=1)

# Evaluate
print("Evaluating model")
mean_reward, std_reward = evaluate_policy(
    model,
    env,
    n_eval_episodes=20,
    deterministic=True,
)
print(f"Mean reward = {mean_reward:.2f} +/- {std_reward:.2f}")

# Start a new episode
obs = env.reset()

try:
    while True:
        action, _states = model.predict(obs, deterministic=True)
        obs, rewards, dones, info = env.step(action)
        env.render()
except KeyboardInterrupt:
    pass
```    
    
  ## Training Code (with Stable-baselines3)

```python
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import EvalCallback

# Create the environment
env_id = "LunarLander-v2"
n_envs = 8
env = make_vec_env(env_id, n_envs=n_envs)

# Create the evaluation envs
eval_envs = make_vec_env(env_id, n_envs=5)

# Adjust evaluation interval depending on the number of envs
eval_freq = int(1e5)
eval_freq = max(eval_freq // n_envs, 1)

# Create evaluation callback to save best model
# and monitor agent performance
eval_callback = EvalCallback(
    eval_envs,
    best_model_save_path="./logs/",
    eval_freq=eval_freq,
    n_eval_episodes=10,
)

# Instantiate the agent
# Hyperparameters from https://github.com/DLR-RM/rl-baselines3-zoo
model = DQN(
    "MlpPolicy",
    env,
    learning_starts=0,
    batch_size=128,
    buffer_size=100000,
    learning_rate=7e-4,
    target_update_interval=250,
    train_freq=1,
    gradient_steps=4,
    # Explore for 40_000 timesteps
    exploration_fraction=0.08,
    exploration_final_eps=0.05,
    policy_kwargs=dict(net_arch=[256, 256]),
    verbose=1,
)

# Train the agent (you can kill it before using ctrl+c)
try:
    model.learn(total_timesteps=int(5e5), callback=eval_callback)
except KeyboardInterrupt:
    pass

# Load best model
model = DQN.load("logs/best_model.zip")
```
  
---
library_name: stable-baselines3
tags:
- BipedalWalker-v3
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: TQC
  results:
  - metrics:
    - type: mean_reward
      value: 332.83 +/- 0.42
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: BipedalWalker-v3
      type: BipedalWalker-v3
---

  # **TQC** Agent playing **BipedalWalker-v3**
  This is a trained model of a **TQC** agent playing **BipedalWalker-v3** using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).
  
## Usage (with Stable-baselines3)

```python
from huggingface_sb3 import load_from_hub
from sb3_contrib import TQC
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy

# Download checkpoint
checkpoint = load_from_hub("araffin/tqc-BipedalWalker-v3", "tqc-BipedalWalker-v3.zip")
# Load the model
model = TQC.load(checkpoint)

env = make_vec_env("BipedalWalker-v3", n_envs=1)

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

## Training code (with SB3)

```python
from sb3_contrib import TQC
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import EvalCallback

# Create the environment
env_id = "BipedalWalker-v3"
n_envs = 2
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
model = TQC(
    "MlpPolicy",
    env,
    learning_starts=10000,
    batch_size=256,
    buffer_size=300000,
    learning_rate=7.3e-4,
    # gSDE is from https://proceedings.mlr.press/v164/raffin22a.html
    use_sde=True,
    train_freq=8,
    gradient_steps=8,
    gamma=0.98,
    tau=0.02,
    policy_kwargs=dict(log_std_init=-3, net_arch=[400, 300]),
    verbose=1,
)

# Train the agent (you can kill it before using ctrl+c)
try:
    model.learn(total_timesteps=int(5e5), callback=eval_callback, log_interval=10)
except KeyboardInterrupt:
    pass
```
  
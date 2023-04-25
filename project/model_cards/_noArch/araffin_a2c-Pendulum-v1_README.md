---
library_name: stable-baselines3
tags:
- Pendulum-v1
- deep-reinforcement-learning
- reinforcement-learning
- stable-baselines3
model-index:
- name: A2C
  results:
  - metrics:
    - type: mean_reward
      value: -141.19 +/- 122.27
      name: mean_reward
    task:
      type: reinforcement-learning
      name: reinforcement-learning
    dataset:
      name: Pendulum-v1
      type: Pendulum-v1
---

  # **A2C** Agent playing **Pendulum-v1**
  This is a trained model of a **A2C** agent playing **Pendulum-v1**
  using the [stable-baselines3 library](https://github.com/DLR-RM/stable-baselines3).
  
## Usage (with Stable-baselines3)

```python
from huggingface_sb3 import load_from_hub
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import VecNormalize

# Download checkpoint and stats
env_id = "Pendulum-v1"
checkpoint = load_from_hub(f"araffin/a2c-{env_id}", f"a2c-{env_id}.zip")
vec_normalize_stats = load_from_hub(f"araffin/a2c-{env_id}", f"vec_normalize.pkl")

# Load the model
model = A2C.load(checkpoint)

env = make_vec_env(env_id, n_envs=1)
env = VecNormalize.load(vec_normalize_stats, env)
#  do not update them at test time
env.training = False
# reward normalization is not needed at test time
env.norm_reward = False

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

## Training Code

```python
from huggingface_sb3 import package_to_hub
from stable_baselines3 import A2C
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import VecNormalize, sync_envs_normalization

# Create the environment
env_id = "Pendulum-v1"
env = make_vec_env(env_id, n_envs=8)
# Normalize
env = VecNormalize(env, gamma=0.9)

# Create the evaluation env (could be used in `EvalCallback`)
eval_env = make_vec_env(env_id, n_envs=1)
eval_env = VecNormalize(eval_env, gamma=0.9, training=False, norm_reward=False)

# Instantiate the agent
model = A2C(
    "MlpPolicy",
    env,
    n_steps=8,
    gamma=0.9,
    gae_lambda=0.9,
    use_sde=True,
    policy_kwargs=dict(log_std_init=-2),
    verbose=1,
)

# Train the agent
try:
    model.learn(total_timesteps=int(1e6))
except KeyboardInterrupt:
    pass


# Synchronize stats (done automatically in `EvalCallback`)
sync_envs_normalization(env, eval_env)

package_to_hub(
    model=model,
    model_name=f"a2c-{env_id}",
    model_architecture="A2C",
    env_id=env_id,
    eval_env=eval_env,
    repo_id=f"araffin/a2c-{env_id}",
    commit_message="Initial commit",
)
```
  
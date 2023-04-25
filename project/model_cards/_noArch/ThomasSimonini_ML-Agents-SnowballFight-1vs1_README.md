---
license: apache-2.0
tags:
- deep-reinforcement-learning
- reinforcement-learning
- ml-agents

environment:
- SnowballFight-1vs1


---

# Snowball Fight ☃️, a multi-agent environment for ML-Agents made by Hugging Face 
![Snowball Fight 1vs1](http://simoninithomas.com/hf/snowballfight.gif)
A multi-agent environment using Unity ML-Agents Toolkit where two agents compete in a 1vs1 snowball fight game.

👉 You can [play  it online at this link](https://huggingface.co/spaces/ThomasSimonini/SnowballFight).

⚠️ You need to have some skills in ML-Agents if you want to use it if it's not the case [check the documentation](https://github.com/Unity-Technologies/ml-agents/tree/main/docs)



## The Environment
- Two agents compete **in a 1 vs 1 snowball fight game**.
- The goal is to **hit the opponent team while avoiding the opponent's snowballs ❄️**.

### Observation Space
- Ray-casts:
	- **10 ray-casts forward** distributed over 100 degrees: detecting opponent.
	- **10 ray-casts forward** distributed over 100 degrees: detecting walls, shelter and frontier.
	- **10 ray-casts forward** distributed over 100 degrees: detecting snowballs.
	-  **3 ray-casts backward** distributed over 45 degrees: detecting wall and shelter.

- Vector Observations:
	- **Bool canShoot** (you can only shoot a snowball every 2 seconds).
	- **Float currentHealth**: normalized [0, 1]
	- **Vector3 vertical speed**
	- **Vector3 horizontal speed**
	- **Vector3 "home" position**

### Action Space (Discrete) 
- Vector Action space:
  - **Four branched actions** corresponding to forward, backward, sideways movement, rotation, and snowball shoot. 

### Agent Reward Function (dependant):
- If the team is **injured**:
    - 0.1 to the shooter.
- If the team is **dead**:
    - (1 - accumulated time penalty): when a snowball hits the
    opponent, the accumulated time penalty decreases by (1 / MaxStep) every fixed update and is reset to 0 at the beginning of an episode.
    - (-1) When a snowball hit our team.

### Addendum
- There **is no friendly fire**, which means that an agent can't shoot himself, or in the future, in a 2vs2 game can't shoot a teammate.


## How to use it 
### Set-up the environment
1. Clone this project `git clone https://huggingface.co/ThomasSimonini/ML-Agents-SnowballFight-1vs1`
2. Open Unity Hub and create a new 3D Project
3. In the cloned project folder, open `.\ML-Agents-SnowballFight-1vs1\packages` and copy manifest.json and package.lock.json
4. Paste these two files in `Your Unity Project\Packages` => this will install the required packages.
5. Drop the SnowballFight-1vs1 unity package to your Unity Project.

### Watch the trained agents
6. If you want to watch the trained agents, open `Assets\1vs1\Scenes\1vs1_v2_Training.` place the `\ML-Agents-SnowballFight-1vs1\saved_model\SnowballFight1vs1-4999988.onnx` into BlueAgent and PurpleAgent Model.

### Train, the agent
6. If you want to train it again, the scene is `Assets\1vs1\Scenes\1vs1_v2_Training.`


## Training info
- SnowballFight1vs1 was trained with 5100000 steps.
- The final ELO score was 1766.452.

### Config File
`behaviors:
  SnowballFight1vs1:
    trainer_type: ppo
    hyperparameters:
      batch_size: 2048
      buffer_size: 20480
      learning_rate: 0.0003
      beta: 0.005
      epsilon: 0.2
      lambd: 0.95
      num_epoch: 3
      learning_rate_schedule: constant
    network_settings:
      normalize: false
      hidden_units: 512
      num_layers: 2
      vis_encode_type: simple
    reward_signals:
      extrinsic:
        gamma: 0.99
        strength: 1.0
    keep_checkpoints: 40
    checkpoint_interval: 200000
    max_steps: 50000000
    time_horizon: 1000
    summary_freq: 50000
    self_play:
      save_steps: 50000
      team_change: 200000
      swap_steps: 2000
      window: 10
      play_against_latest_model_ratio: 0.5
      initial_elo: 1200.0
`


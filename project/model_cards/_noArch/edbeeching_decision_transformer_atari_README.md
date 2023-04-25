---
tags:
- deep-reinforcement-learning
- reinforcement-learning

---

Find here pretrained model weights for the [Decision Transformer] (https://github.com/kzl/decision-transformer).
Weights are available for 4 Atari games: Breakout, Pong, Qbert and Seaquest. Found in the checkpoints directory.
We share models trained for one seed (123), whereas the paper contained weights for 3 random seeds.


### Usage

```
git clone https://huggingface.co/edbeeching/decision_transformer_atari
conda env create -f conda_env.yml
```

Then, you can use the model like this:

```python

from decision_transform_atari import GPTConfig, GPT

vocab_size = 4
block_size = 90
model_type = "reward_conditioned"
timesteps = 2654

mconf = GPTConfig(
    vocab_size,
    block_size,
    n_layer=6,
    n_head=8,
    n_embd=128,
    model_type=model_type,
    max_timestep=timesteps,
)
model = GPT(mconf)

checkpoint_path = "checkpoints/Breakout_123.pth"  # or Pong, Qbert, Seaquest
checkpoint = torch.load(checkpoint_path)
model.load_state_dict(checkpoint)
```

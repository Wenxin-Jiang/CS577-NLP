---
license: mit
---

# A model based on UberHaxorNova's Twitch chat  

Trained on over 700 vods worth of chat and with some scuffed filtering it became a 300mb dataset.  

## Dataset

The dataset was created by downloading all the available vods at the time of creation as a json file and stripping out all the chat messages into a simple line-by-line text file.

## Training

This was trained using [aitextgen](https://github.com/minimaxir/aitextgen), created by [Max Woolf](https://github.com/minimaxir), using the example notebook found [here](https://colab.research.google.com/drive/15qBZx5y9rdaQSyWpsreMDnTiZ5IlN0zD?usp=sharing). Using GPT-2's 124M model as the base, it was trained for 3000 steps and produces an output scuffed enough to look like a real Twitch chat user.

## Use

This was created as a fun little project for the discord server and as such, should only be used for fun and not to harm people. This model must also follow the ethics guide of the tool that created it https://docs.aitextgen.io/ethics/

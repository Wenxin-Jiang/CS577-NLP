---
language: en
thumbnail: https://github.com/borisdayma/huggingtweets/blob/master/img/logo.png?raw=true
tags:
- huggingtweets
widget:
- text: "My dream is"
---

<div>
<div style="width: 132px; height:132px; border-radius: 50%; background-size: cover; background-image: url('https://pbs.twimg.com/profile_images/1343999703776518144/ZWju8o9V_400x400.jpg')">
</div>
<div style="margin-top: 8px; font-size: 19px; font-weight: 800">Evan Knox 🤖 AI Bot </div>
<div style="font-size: 15px">@evandknox bot</div>
</div>

I was made with [huggingtweets](https://github.com/borisdayma/huggingtweets).

Create your own bot based on your favorite user with [the demo](https://colab.research.google.com/github/borisdayma/huggingtweets/blob/master/huggingtweets-demo.ipynb)!

## How does it work?

The model uses the following pipeline.

![pipeline](https://github.com/borisdayma/huggingtweets/blob/master/img/pipeline.png?raw=true)

To understand how the model was developed, check the [W&B report](https://wandb.ai/wandb/huggingtweets/reports/HuggingTweets-Train-a-Model-to-Generate-Tweets--VmlldzoxMTY5MjI).

## Training data

The model was trained on [@evandknox's tweets](https://twitter.com/evandknox).

| Data | Quantity |
| --- | --- |
| Tweets downloaded | 848 |
| Retweets | 98 |
| Short tweets | 53 |
| Tweets kept | 697 |

[Explore the data](https://wandb.ai/wandb/huggingtweets/runs/1oe57zgg/artifacts), which is tracked with [W&B artifacts](https://docs.wandb.com/artifacts) at every step of the pipeline.

## Training procedure

The model is based on a pre-trained [GPT-2](https://huggingface.co/gpt2) which is fine-tuned on @evandknox's tweets.

Hyperparameters and metrics are recorded in the [W&B training run](https://wandb.ai/wandb/huggingtweets/runs/1zossq8w) for full transparency and reproducibility.

At the end of training, [the final model](https://wandb.ai/wandb/huggingtweets/runs/1zossq8w/artifacts) is logged and versioned.

## How to use

You can use this model directly with a pipeline for text generation:

```python
from transformers import pipeline
generator = pipeline('text-generation',
                     model='huggingtweets/evandknox')
generator("My dream is", num_return_sequences=5)
```

## Limitations and bias

The model suffers from [the same limitations and bias as GPT-2](https://huggingface.co/gpt2#limitations-and-bias).

In addition, the data present in the user's tweets further affects the text generated by the model.

## About

*Built by Boris Dayma*

[![Follow](https://img.shields.io/twitter/follow/borisdayma?style=social)](https://twitter.com/intent/follow?screen_name=borisdayma)

For more details, visit the project repository.

[![GitHub stars](https://img.shields.io/github/stars/borisdayma/huggingtweets?style=social)](https://github.com/borisdayma/huggingtweets)
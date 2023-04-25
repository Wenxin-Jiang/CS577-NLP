---
tags:
- text-to-image
- torch
inference: false
datasets:
- laion/laion_100m_vqgan_f8
---

This model is trained collaboratively — it is a part of the NeurIPS 2021 demonstration ["Training Transformers Together"](https://training-transformers-together.github.io/).

The latest model checkpoint will be uploaded to this repository every 6 hours until the training stops.

# Model Description 

We train a model similar to [OpenAI DALL-E](https://openai.com/blog/dall-e/) — a Transformer model that generates images from text descriptions. Training happens collaboratively — volunteers from all over the Internet contribute to the training using hardware available to them. We use [LAION-400M](https://laion.ai/laion-400-open-dataset/), the world's largest openly available image-text-pair dataset with 400 million samples. Our model is based on the [dalle‑pytorch](https://github.com/lucidrains/DALLE-pytorch) implementation by [Phil Wang](https://github.com/lucidrains) with a few tweaks to make it communication-efficient. 

# Training

You can check our [dashboard](https://huggingface.co/spaces/training-transformers-together/Dashboard)  to see what is happening during the collaborative training (loss over time, number of active sessions over time, contribution of each participant, leaderboard, etc. ).

# How to Use 

You can start from our [Colab notebook for running inference](https://colab.research.google.com/drive/1Vkb-4nhEEH1a5vrKtpL4MTNiUTPdpPUl?usp=sharing).

#  Limitations

This model is created only as a demonstration of the new distributed training methods. **It should not be used for anything besides research purposes.**

The authors have done only the most basic dataset filtering, so the model may be susceptible to biases in the training data and/or generate inappropriate content.

At the moment, the model's generative capabilities are limited due to the absence of extensive experiments with the architecture and incomplete training.

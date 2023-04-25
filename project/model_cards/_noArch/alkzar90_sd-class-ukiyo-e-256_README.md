---
license: mit
tags:
- pytorch
- diffusers
- unconditional-image-generation
- diffusion-models-class
---

# Example Fine-Tuned Model for Unit 2 of the [Diffusion Models Class 🧨](https://github.com/huggingface/diffusion-models-class)

This model is a diffusion model for unconditional image generation of Ukiyo-e images ✍ 🎨.  The model was train using fine-tuning with the google/ddpm-celebahq-256 pretrain-model and the dataset: https://huggingface.co/datasets/huggan/ukiyoe2photo

![](https://huggingface.co/alkzar90/sd-class-ukiyo-e-256/resolve/main/ukyo-e-portrait.jpeg)

* Google Colab notebook for experiment with the model and the sampling process using a Gradio App: https://colab.research.google.com/drive/1F7SH4T9y5fJKxj5lU9HqTzadv836Zj_G?usp=sharing
* Weights&Biases dashboard with training information: https://wandb.ai/alcazar90/fine-tuning-a-diffusion-model?workspace=user-alcazar90


## Usage

```python
from diffusers import DDPMPipeline

pipeline = DDPMPipeline.from_pretrained('alkzar90/sd-class-ukiyo-e-256')
image = pipeline().images[0]
image
```

## Guidance

**Prompt:** _A sakura tree_

![](https://huggingface.co/alkzar90/sd-class-ukiyo-e-256/resolve/main/ukyo-e-sakura-tree.jpeg)


**Prompt:** _An island with sunset at background_

![](https://huggingface.co/alkzar90/sd-class-ukiyo-e-256/resolve/main/ukyo-e-sunset-island.jpeg)


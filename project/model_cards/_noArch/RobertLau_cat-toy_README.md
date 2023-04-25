---
license: creativeml-openrail-m
tags:
- text-to-image
---
### Cat toy on Stable Diffusion via Dreambooth
#### model by RobertLau
This your the Stable Diffusion model fine-tuned the Cat toy concept taught to Stable Diffusion with Dreambooth.
It can be used by modifying the `instance_prompt`: **<cat-toy> toy**

You can also train your own concepts and upload them to the library by using [this notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_training.ipynb).
And you can run your new concept via `diffusers`: [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb), [Spaces with the Public Concepts loaded](https://huggingface.co/spaces/sd-dreambooth-library/stable-diffusion-dreambooth-concepts)

#### Usage:
If you want to use this concept, please add &lt;cat-toy&gt; in your prompt, for example: "A &lt;cat-toy&gt; in mad max fury road"
![image 0](https://huggingface.co/RobertLau/cat-toy/resolve/main/0_0.jpeg)

Here are the images used for training this concept:
![image 0](https://huggingface.co/RobertLau/cat-toy/resolve/main/concept_images/0.jpeg)
![image 1](https://huggingface.co/RobertLau/cat-toy/resolve/main/concept_images/1.jpeg)
![image 2](https://huggingface.co/RobertLau/cat-toy/resolve/main/concept_images/2.jpeg)
![image 3](https://huggingface.co/RobertLau/cat-toy/resolve/main/concept_images/3.jpeg)


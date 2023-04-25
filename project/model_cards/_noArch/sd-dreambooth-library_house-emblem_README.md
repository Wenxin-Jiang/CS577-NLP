---
license: creativeml-openrail-m
tags:
- text-to-image
---
### house-emblem on Stable Diffusion via Dreambooth
#### model by chenweiwu
This your the Stable Diffusion model fine-tuned the house-emblem concept taught to Stable Diffusion with Dreambooth.
It can be used by modifying the `instance_prompt`: **a photo of sks house-emblem**

You can also train your own concepts and upload them to the library by using [this notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_training.ipynb).
And you can run your new concept via `diffusers`: [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb), [Spaces with the Public Concepts loaded](https://huggingface.co/spaces/sd-dreambooth-library/stable-diffusion-dreambooth-concepts)

Here are the images used for training this concept:
![image 0](https://huggingface.co/sd-dreambooth-library/house-emblem/resolve/main/concept_images/1.jpeg)
![image 1](https://huggingface.co/sd-dreambooth-library/house-emblem/resolve/main/concept_images/0.jpeg)
![image 2](https://huggingface.co/sd-dreambooth-library/house-emblem/resolve/main/concept_images/3.jpeg)
![image 3](https://huggingface.co/sd-dreambooth-library/house-emblem/resolve/main/concept_images/2.jpeg)


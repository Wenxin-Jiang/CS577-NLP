---
license: mit
language: en
tags:
  - text-to-image
---

# Zack Fox Stable Diffusion

Stable Diffusion v1.5 model fine-tuned to generate pictures of Zack Fox with Dreambooth.

It can be used by modifying the `instance_prompt`: **a photo of sks zach fox**. Yea...I misspelled his name when I made the prompt. My bad lol.

You can also train your own concepts and upload them to the library by using [this notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_training.ipynb).
And you can run your new concept via `diffusers`: [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb), [Spaces with the Public Concepts loaded](https://huggingface.co/spaces/sd-dreambooth-library/stable-diffusion-dreambooth-concepts)


## Usage

To use this model, you can run the following...

```python
import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "nateraw/zack-fox",
    torch_dtype=torch.float16
).to("cuda")

prompt = "a photo of sks zach fox, oil on canvas"
image = pipe(prompt).images[0]
```

Here are the images used for training this concept:
![image 0](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/8.jpeg)
![image 1](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/13.jpeg)
![image 2](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/20.jpeg)
![image 3](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/12.jpeg)
![image 4](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/15.jpeg)
![image 5](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/6.jpeg)
![image 6](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/17.jpeg)
![image 7](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/16.jpeg)
![image 8](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/1.jpeg)
![image 9](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/3.jpeg)
![image 10](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/0.jpeg)
![image 11](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/19.jpeg)
![image 12](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/10.jpeg)
![image 13](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/2.jpeg)
![image 14](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/4.jpeg)
![image 15](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/24.jpeg)
![image 16](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/5.jpeg)
![image 17](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/21.jpeg)
![image 18](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/9.jpeg)
![image 19](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/14.jpeg)
![image 20](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/22.jpeg)
![image 21](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/23.jpeg)
![image 22](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/7.jpeg)
![image 23](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/18.jpeg)
![image 24](https://huggingface.co/nateraw/zack-fox/resolve/main/concept_images/11.jpeg)


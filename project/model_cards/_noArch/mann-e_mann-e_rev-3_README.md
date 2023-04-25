---
license: mit
tags:
- text-to-image
---

![Sample](https://huggingface.co/mann-e/mann-e_rev-3/resolve/main/revision-3-artwork.png)

# Mann-E 3 revision 3 "Prompt Muse"

__Mann-E__ is a _text to image_ model which has been developed by [Muhammadreza Haghiri](https://haghiri75.com/en) in order to be part of the [Cognitive Web](https://opencognitives.com) movement and projects.
This is revision 3 of the model and it's the first one to have a code name. The code name is _Prompt Muse_.

### What does _Mann-E_ mean?

It's a play with the name [Mani](https://en.wikipedia.org/wiki/Mani_(prophet)), who was a Persian religious leader at the early Sassanian era and also a painter and he's famous for both his religious and artistic works. His artistic side was more considered for naming the model of course.

## How to use the model

### Colab

You easily can click on [this link](https://colab.research.google.com/github/prp-e/mann-e/blob/main/Mann_E.ipynb) and use model's inference notebook. 

### Code

The following code is written for _CUDA_ supported devices. If you use UI's or inference tools on other devices, you may need to tweak them in order to get them to the work. Otherwise, it will be fine.

First, you need to install required libraries:

```
pip3 install diffusers transformers scipy ftfy accelerate
```

_NOTE: installation of `accelerate` library makes the inference process amazingly faster. but it's totally optional_. 

Then, you need to import required libraries:

```python
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler, DiffusionPipeline, DPMSolverMultistepScheduler
import torch
```

and then, create a pipeline (this pipeline is made with Euler Scheduler):

```python
model_id = "mann-e/mann-e_rev-3"

scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")

pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
```

and of course, since you may get NSFW filteration warnings even on simplest prompts, you may consider disabling it:

```python
def dummy(images, **kwargs): 
    return images, False 

pipe.safety_checker = dummy
```

_NOTE: Please consider consequences of disabling this filter as well. we do not want people to get any sort of damage or injury from the image generation results_. 

And after that, you easily can start inference:

```python
prompt = "Concept art of a hostile alien planet with unbreathable purple air and toxic clouds, sinister atmosphere, deep shadows, sharp details" 
negative_prompt = "low quality, blurry" 
width = 768 
height = 512 
```

then: 

```python
image = pipe(prompt=prompt, negative_prompt=negative_prompt, num_inference_steps=100, width=width, height=height, guidance_scale=10).images[0]
image.save("My_image.png")
```

---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
---
### islamicdiffusion Dreambooth model trained by Falah 

With Stable Diffusion DreamBooth, we can now create AI art generation images using our own trained images.
in this model, we can generate images with Islamic landscapes or female or male ones as popular images  or just about anything you can think of 
Test the concept via A1111 Colab [fast-Colab-A1111](https://colab.research.google.com/github/TheLastBen/fast-stable-diffusion/blob/main/fast_stable_diffusion_AUTOMATIC1111.ipynb)

Sample pictures of this concept with the simple and easy prompts:

any prompt and add word islamidiffusion style :

"home islamicdiffusion" 

<img src="https://huggingface.co/Falah/islamicdiffusion/resolve/main/00626-3710065853-Islamic%20home.png" style="max-width: 800px;" width="100%"/>

"home islamicdiffusion" 

<img src ="https://huggingface.co/Falah/islamicdiffusion/resolve/main/00629-3710065856-Islamic%20home.png" style="max-width: 800px;" width="100%"/>

"Bearded old man, handsome, rugged, sadness + crying, Arabic, award-winning photography, nikon d750 islamicdiffusion" 

<img src ="https://huggingface.co/Falah/islamicdiffusion/resolve/main/00722-913347333-islamicdiffusion%20%20Bearded%20old%20man%2C%20handsome%2C%20rugged%2C%20sadness%20%2B%20crying%2C%20Arabic%2C%20award-winning%20photography%2C%20nikon%20d750.png" style="max-width: 800px;" width="100%"/>

"Bearded old man, handsome, rugged, sadness + crying, Arabic, award-winning photography, nikon d750 islamicdiffusion" 

<img src="https://huggingface.co/Falah/islamicdiffusion/resolve/main/00725-913347336-islamicdiffusion%20%20Bearded%20old%20man%2C%20handsome%2C%20rugged%2C%20sadness%20%2B%20crying%2C%20Arabic%2C%20award-winning%20photography%2C%20nikon%20d750.png" style="max-width: 800px;" width="100%"/>

<img src="https://huggingface.co/Falah/islamicdiffusion/resolve/main/1.png" style="max-width: 800px;" width="100%"/>

<img src="https://huggingface.co/Falah/islamicdiffusion/resolve/main/2.png" style="max-width: 800px;" width="100%"/>


<img src="https://huggingface.co/Falah/islamicdiffusion/resolve/main/3.png" style="max-width: 800px;" width="100%"/>

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion Pipeline](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

```python
from diffusers import StableDiffusionPipeline
import torch
model_id = "Falah/islamicdiffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = ""Bearded old man, handsome, rugged, sadness + crying, Arabic, award-winning photography, nikon d750 islamicdiffusion" 
image = pipe(prompt).images[0]
image.save("./result.jpg")
```


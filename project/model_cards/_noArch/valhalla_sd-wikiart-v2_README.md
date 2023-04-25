---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: bigscience-bloom-rail-1.0
inference: true

---

# stable-diffusion-wikiart

sd-wikiart-v2 is a stable diffusion model that has been fine-tuned on the [wikiart dataset](https://huggingface.co/datasets/fusing/wikiart_captions) to generate artistic images in different style and genres.

<img src="https://huggingface.co/valhalla/sd-wikiart-v2/resolve/main/wikiart.png">

# Gradio

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1i7HJlTzVPEirNedDV-TcR5Ok2_8QI6zC?usp=sharing)


## Model Description

The model originally used for fine-tuning is [Stable Diffusion V1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4), which is a latent image diffusion model trained on [LAION2B-en](https://huggingface.co/datasets/laion/laion2B-en).

The current model has been fine-tuned with a learning rate of 1e-05 for 1 epoch on 81K text-image pairs from wikiart dataset. Only the attention layers of the model are fine-tuned. This is done to avoid catastrophic forgetting, the model can generate artistic images given specific prompts but still retains most of its previous knowledge.

## Training Data 
TODO

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

## Downstream Uses

This model can be used for entertainment purposes and as a generative art assistant.

## Example Code

```python
import torch
from diffusers import StableDiffusionPipeline

model_id = "valhalla/sd-wikiart-v2"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
)
pipe = pipe.to(device)

prompt = "a painting of eiffel tower in the style of surrealism"
with torch.autocast("cuda"):
    image = pipe(prompt, guidance_scale=7.5).images[0]
    
image.save("eiffel_impressionism.png")
```
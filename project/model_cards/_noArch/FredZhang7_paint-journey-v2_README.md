---
license: creativeml-openrail-m
language:
- en
tags:
- text-to-image
- midjourney
- stable-diffusion
- disco-diffusion
- art
- arxiv:2208.12242
inference: true
library_name: diffusers
---
## Paint Journey V2 is [V1](https://huggingface.co/FredZhang7/paint-journey-v1) fine-tuned on 768x768 oil paintings by Midjourney V4, Open Journey V2, Disco Diffusion, and artists given permission

Begin the prompt with **((oil painting))** to add the oil paint effect. For digital and other painting styles, use similar prompts as you would for Midjourney V4 (with some tweaks), Stable Diffusion v1.5 (add more styles), Open Journey V2, or Disco Diffusion.

[![Open with Camenduru's WebUI in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AMLA-UBC/100-Exploring-the-World-of-Modern-Machine-Learning/blob/main/assets/PaintJourneyV2.ipynb)

## Examples

*All examples were generated using Camenduru's WebUI (see the Colab file)*

![](./assets/characters.png)
*⬆️ 768x1136 portraits, generated using descriptive prompts and without face restoration, [generation parameters](https://huggingface.co/FredZhang7/paint-journey-v2/raw/main/assets/character_settings.txt)*

![](./assets/nature.png)
*⬆️ 1280x768 (mostly) natural landscapes, used shorter prompts, [generation parameters](https://huggingface.co/FredZhang7/paint-journey-v2/raw/main/assets/nature_settings.txt)*

![](./assets/outerspace.png)
*⬆️ 1152x768 outerspace landscapes, used descriptive prompts, [generation parameters](https://huggingface.co/FredZhang7/paint-journey-v2/raw/main/assets/outerspace_settings.txt)*

![](./assets/lamborghini.png)
*⬆️ 1280x768 lamborghini, [generation parameters](https://huggingface.co/FredZhang7/paint-journey-v2/raw/main/assets/lamborghini_settings.txt)*

![](./assets/eevee.png)
*⬆️ 960x768 Eevee, [generation parameters](https://huggingface.co/FredZhang7/paint-journey-v2/raw/main/assets/eevee_settings.txt)*


## Comparisons

Paint Journey V2's paintings are closer to human-drawn art than Open Journey V2.
Compared to models like Dreamlike Diffusion 1.0, PJ V2 tends to generate 768x768 or higher resolution images with reduced noise levels.
This model is also capable of generating stunning portraits at 768x1136 resolution without duplicated faces (with [Camenduru's WebUI](https://github.com/camenduru/stable-diffusion-webui)), a difficult task to models like DreamShaper 3.3.

At lower resolutions, DreamShaper 3.3 tends to generate higher quality portraits than PJ V2 in terms of noise levels, given the same (short) postive and negative prompts.
However, PJ V2 can craft more stunning masterpieces with more descriptive positive and negative prompts and can still generate beautiful landscapes with shorter prompts.


## Training
Instead of solely fine-tuning its Unet, Paint Journey V2 focuses on fine-tuning its text encoder with a diverse range of prompts.
This allows for a seamless blend of the digital and oil painting styles into various other types of prompts, resulting in a more natural and dynamic output.

This model was trained on a curated dataset of roughly 300 images hand-picked from Midjourney, [Prompt Hero](https://prompthero.com/), [PixaBay](https://pixabay.com/images/search/paintings/), Open Journey V2, and Reddit.
Before training, I used R-ESRGAN 4x on many images to increase their resolution and reduce noise.


## Running out of prompts?
Useful resources: [Lexica.art](https://lexica.art/), [Fast GPT PromptGen](https://huggingface.co/FredZhang7/distilgpt2-stable-diffusion-v2), [Prompt Hero](https://prompthero.com/)


## Output Dimensions
Portrait sizes include, but are not limited to, `512x768`, `768x768`, and `768x1136`.
Landscape sizes include, but are not limited to, `768x512`, `768x768`, `1152x768`, and `1280x768`.


## Camenduru's WebUI

```
git clone -b v1.6 https://github.com/camenduru/stable-diffusion-webui
```

<details>
<summary> Click to use Automatic1111's Webui instead, but may not output images as artistic </summary>

```
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

</details>


Download [checkpoint](./paint_journey_v2.ckpt) and [vae](./paint_journey_v2.vae.pt) to the `./stable-diffusion-webui/models/Stable-diffusion` folder. Run `webui-user.bat`.


## 🧨 Diffusers

*Tip: using double, tripple, or quadriple brackets around some letters WORD (e.g. "((WORD))") will put an 'emphasis' on WORD*

```bash
pip install --upgrade diffusers transformers
```
```python
# see more sampling algorithms at https://huggingface.co/docs/diffusers/using-diffusers/schedulers#changing-the-scheduler

from diffusers import StableDiffusionPipeline, EulerAncestralDiscreteScheduler
import torch, random, datetime

pipe = StableDiffusionPipeline.from_pretrained("FredZhang7/paint-journey-v2")
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

def random_seed():
  return random.randint(0, 2**32 - 1)


prompt = "((oil painting)), gentle waves, bright blue sky, white sails billowing, sun glistening on the surface, salty sea air, distant horizon, calm breeze, birds soaring overhead, vibrant colors, artstation digital painting, high resolution, uhd, 4 k, 8k wallpaper"   # what you want to see
negative_prompt = "low-res, blurry, haze, dark clouds looming, choppy waves, engine failing, sails tattered, stormy winds".split(", ")   # what you don't want to see
seed = random_seed()               # replace with the desired seed if needed
width, height = 1280, 768          # width and height of the generated image
cfg_scale = 7.5                    # classifer free guidance scale, smaller means more creative, 7 to 11 is usually a good range
num_inference_steps = 40           # sampling steps, 30 to 40 is usually good for Euler Ancestral


generator = torch.Generator("cuda").manual_seed(seed)
with torch.autocast("cuda"):
    image = pipe(prompt=prompt,
                  num_inference_steps=num_inference_steps,
                  width=width, height=height,
                  generator=generator,
                  guidance_scale=cfg_scale).images[0]

def generate_filename(string, seed):
    invalid_chars = ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]
    for char in invalid_chars:
        string = string.replace(char, "")
    return f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{seed}_{string}"

image.save(f"./{generate_filename(prompt, seed)}.png")
```

## Safety Checker V2

The official [stable diffusion safety checker](https://huggingface.co/CompVis/stable-diffusion-safety-checker) uses up 1.22GB VRAM.
I recommend using [Google Safesearch Mini V2](https://huggingface.co/FredZhang7/google-safesearch-mini-v2) (220MB) to save 1.0GB VRAM.
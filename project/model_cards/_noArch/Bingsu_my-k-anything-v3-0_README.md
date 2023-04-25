---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
inference: true
language: ko
---

# my-k-anything-v3-0

[Bingsu/my-korean-stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)와 같은 방법으로 만든 k-아무거나 3.0 모델.

생각보다 잘 안되고, 특히 캐릭터에 관한 정보는 다 잊어버린 걸로 보입니다.

# Usage

```sh
pip install transformers accelerate>=0.14.0 diffusers>=0.7.2
```

```python
import torch
from diffusers import StableDiffusionPipeline

repo = "Bingsu/my-k-anything-v3-0"
pipe = StableDiffusionPipeline.from_pretrained(
    repo, torch_dtype=torch.float16,
)
pipe.to("cuda")
pipe.safety_checker = None
```

```python
from typing import Optional
import torch


def gen_image(
    prompt: str,
    negative_prompt: Optional[str] = None,
    seed: Optional[int] = None,
    scale: float = 7.5,
    steps: int = 30,
):
    if seed is not None:
        generator = torch.Generator("cuda").manual_seed(seed)
    else:
        generator = None

    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        generator=generator,
        guidance_scale=scale,
        num_inference_steps=steps,
    ).images[0]

    return image
```

```python
prompt = "파란색 포니테일 헤어, 브로치, 정장을 입은 성인 여성, 고퀄리티, 최고품질"
negative = "저화질, 저품질, 텍스트"
seed = 42467781
scale = 12.0
gen_image(prompt, negative, seed, scale)
```

![Imgur](https://i.imgur.com/24G8n1m.png)

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage. The CreativeML OpenRAIL License specifies:

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content

2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully) [Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

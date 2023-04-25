---
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/dallinmackay/Van-Gogh-diffusion/resolve/main/preview1.jpg"
tags:
- stable-diffusion
- text-to-image
---
### Van Gogh Diffusion

v2 - fixed and working

This is a fine-tuned Stable Diffusion model (based on v1.5) trained on screenshots from the film **_Loving Vincent_**. Use the token **_lvngvncnt_** at the BEGINNING of your prompts to use the style (e.g., "lvngvncnt, beautiful woman at sunset"). This model works best with the Euler sampler (NOT Euler_a).

_Download the ckpt file from "files and versions" tab into the stable diffusion models folder of your web-ui of choice._

If you get too many yellow faces or you dont like the strong blue bias, simply put them in the negative prompt (e.g., "Yellow face, blue").

--

**Characters rendered with this model:**
![Character Samples](https://huggingface.co/dallinmackay/Van-Gogh-diffusion/resolve/main/preview1.jpg)
  _prompt and settings used: **lvngvncnt, [person], highly detailed** | **Steps: 25, Sampler: Euler, CFG scale: 6**_

--

**Landscapes/miscellaneous rendered with this model:**
![Landscape Samples](https://huggingface.co/dallinmackay/Van-Gogh-diffusion/resolve/main/preview2.jpg)
  _prompt and settings used: **lvngvncnt, [subject/setting], highly detailed** | **Steps: 25, Sampler: Euler, CFG scale: 6**_

--

This model was trained with Dreambooth, using TheLastBen colab notebook
--
### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "dallinmackay/Van-Gogh-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "lvngvncnt, beautiful woman at sunset"
image = pipe(prompt).images[0]

image.save("./sunset.png")
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

--
[![Become A Patreon](https://badgen.net/badge/become/a%20patron/F96854)](https://www.patreon.com/dallinmackay)
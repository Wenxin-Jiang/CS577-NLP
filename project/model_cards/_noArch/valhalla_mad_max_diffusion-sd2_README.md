---
language:
- en
license: openrail++
thumbnail: "https://huggingface.co/valhalla/mad_max_diffusion-sd2/resolve/main/mad-max-fr.png"
tags:
- stable-diffusion
- text-to-image
- image-to-image
- diffusers

---
### Mad Max: Fury Road Diffusion (SD 2.0, 768x768)

This is the fine-tuned Stable Diffusion model trained on images from Mad Max: Fury Road.
Use the tokens **_mad_max_fr_** in your prompts for the effect.


**Images rendered with the model:**
Turn your favorite cars, city's, characters in fury road style.

![Samples](https://huggingface.co/valhalla/mad_max_diffusion-sd2/resolve/main/mad-max-fr.png)


### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
model_id = "valhalla/mad_max_diffusion-sd2"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")
pipe.enable_attention_slicing()
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

prompt = "The streets of Paris with eiffel tower in the background in the style of mad_max_fr"
image = pipe(prompt, num_inference_steps=30).images[0]
image.save("./paris-mad-max-fr.png")
```
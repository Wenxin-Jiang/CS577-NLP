---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/Qilex/magic-diffusion/resolve/main/guys.png"
tags:
- stable-diffusion
- text-to-image

---
### Magic Diffusion

This is a fine-tuned Stable Diffusion model trained on scans of Magic: the Gathering card artworks.
Use the tokens **_mtg style_** in your prompts.


It does not have additional knowledge of Magic-specific terms.

**Characters rendered with the model:**
![Samples](https://huggingface.co/Qilex/magic-diffusion/resolve/main/guys.png)
**Non-characters rendered with the model:**
![More Samples](https://huggingface.co/Qilex/magic-diffusion/resolve/main/things.png)



### 🧨 Diffusers

This model can be used like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
import torch
from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("Qilex/magic-diffusion", torch_dtype=torch.half).to("cuda")
prompt = "mtg style Tony Stark, in a city"
with torch.cuda.amp.autocast(True):
    image = pipeline(prompt, num_inference_steps=40, guidance_scale=8, height = 512, width = 712, scheduler = "DDIM").images[0]
image.save(f"img.png")

```
You can try it out on the [Colab example](https://colab.research.google.com/drive/1wlvbTnVxm3bfFwW793cEEVeOYtB0mRG3?usp=sharing), which should work on the free GPU tier.


This model was trained using the diffusers dreambooth training example script using prior-preservation loss and finetuning the text encoder on roughly 120 images in 8.000 steps.

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)


Fine-tuning data was provided by Wizards of the Coast under their [Fan Content Policy](https://company.wizards.com/en/legal/fancontentpolicy)

## Acknowledgements
Thanks to [nitrosocke](https://huggingface.co/nitrosocke) for the inspiration and readme template.
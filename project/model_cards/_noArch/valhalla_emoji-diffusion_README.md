---
language:
- en
tags:
- stable-diffusion
- text-to-image
widget:
- text: "a unicorn Llama emoji"
  example_title: Llama Emoji
- text: "emoji pokemon"
  example_title: Pokemon Emoji
- text: "snowy montain emoji"
  example_title: snowy montain emoji
- text: "a snail shaped harp emoji"
  example_title: Snail-shaped harp Emoji
license: bigscience-bloom-rail-1.0

---

# stable diffusion finetuned on emoji dataset

emoji-diffusion is a stable diffusion model fine-tuned on the [russian-emoji dataset](https://www.kaggle.com/datasets/shonenkov/russian-emoji) to generate emoji images.
Below are some samples generated using the model.

<img src="https://huggingface.co/valhalla/emoji-diffusion/resolve/main/emoji.png">


## Usage

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

**To get the best result use the text "emoji" at beginning or end of the prompt.**

```python
import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler

pipe = StableDiffusionPipeline.from_pretrained(
    "valhalla/emoji-diffusion",
    torch_dtype=torch.float16,
).to("cuda")
euler = EulerDiscreteScheduler.from_config(pipe.scheduler.config)
pipe.scheduler = euler

prompt = "a unicorn lama emoji" 
image = pipe(prompt, num_inference_steps=30).images[0]
    
image.save("lama_emoji.png")
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

## Downstream Uses

This model can be used for entertainment purposes and as a generative art assistant.
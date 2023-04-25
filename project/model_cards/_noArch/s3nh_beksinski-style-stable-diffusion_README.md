---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---

Buy me a coffee if you like this project ;)
<a href="https://www.buymeacoffee.com/s3nh"><img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-1.svg" alt=""></a>

### Zdzislaw Beksinski Art Diffusion Model

I present you fine tuned model of stable-diffusion-v1-5, which heavily based of 
work of great artist, Zdzislaw Beksinski.
Use the tokens **_beksinski style_** in your prompts for the effect.

Model was trained using the diffusers library, which based on Dreambooth implementation. 
Training steps included: 

- prior preservation loss
- train-text-encoder fine tuning 

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
#!pip install diffusers transformers scipy torch
from diffusers import StableDiffusionPipeline
import torch
model_id = "s3nh/beksinski-style-stable-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "Bus riding to school, beksinski style"
image = pipe(prompt).images[0]
image.save("./example_output.png")
```

# Gallery 

## Bus riding to school, beksinski style.
![image](https://huggingface.co/s3nh/beksinski-style-stable-diffusion/resolve/main/bus1.png)
![image](https://huggingface.co/s3nh/beksinski-style-stable-diffusion/resolve/main/bus2.png)
![image](https://huggingface.co/s3nh/beksinski-style-stable-diffusion/resolve/main/bus3.png)

## Car traffic, beksinski style
![image](https://huggingface.co/s3nh/beksinski-style-stable-diffusion/resolve/main/_cartraffic.png)
![image](https://huggingface.co/s3nh/beksinski-style-stable-diffusion/resolve/main/car_traffic.png)
![image](https://huggingface.co/s3nh/beksinski-style-stable-diffusion/resolve/main/car_traffic2.png)
## Eating breakfast on sunny day, beksinski style 

![image](https://huggingface.co/s3nh/beksinski-style-stable-diffusion/resolve/main/ebsd.png)

## Dog drinking coffee, beksinski style

![image](https://huggingface.co/s3nh/beksinski-style-stable-diffusion/resolve/main/dog_drinking_coffee.png)

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
---
language: 
  - en
thumbnail: "https://huggingface.co/nousr/robo-diffusion/resolve/main/robo_example.png"
tags:
- robots
- stable-diffusion
- aiart
- text-to-image
license: "openrail++"
---
# Robo-Diffusion 2 (base)
A dreambooth-method finetune of stable diffusion that will output cool looking robots when prompted.

<img src="https://huggingface.co/nousr/robo-diffusion-2-base/resolve/main/example_grid.png"/>

# Usage
Keep the words `nousr robot` towards the beginning of your prompt to invoke the finetuned style. Use negative prompts to achieve the best result.

```python
import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler

scheduler = EulerDiscreteScheduler.from_pretrained("nousr/robo-diffusion-2-base", subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained("nousr/robo-diffusion-2-base", scheduler=scheduler, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "A realistic photograph of a 3d nousr robot in a modern city. A glossy white and orange nousr robot."
negative_prompt = "black and white robot, picture frame, a children's drawing in crayon. #Wholesale, Abstract Metal Sculpture. i'm leaving a bad review."
image = pipe(prompt, negative_prompt=negative_prompt, num_inference_steps=32, guidance_scale=5.0).images[0]

image.save("robo.png")
```

# Original Model
Based on stable diffusion 1.4 can be found [here](https://huggingface.co/nousr/robo-diffusion)

# Socials
Use the #robodiffusion so i can see the cool stuff you make!

If you enjoy the model i'd appreciate a follow on [twitter](https://twitter.com/nousr_)

If you are feeling especially generous, you can sponsor me on [github](https://github.com/nousr)

---
*NOTE: ensure you have read the license and agree to the terms
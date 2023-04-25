---
license: cc-by-nc-sa-4.0

language:
- en

thumbnail: "https://huggingface.co/GeneralAwareness/Mirrormask/resolve/main/mm1.png"

tags:
- stable-diffusion
- text-to-image
- image-to-image
- diffusers
---

### Mirror Mask

Welcome to MirrorMask - This is a fine-tuned Stable Diffusion model trained from the 2005 dark fantasy film MirrorMask.

Use the token mirrormask in your prompts for the style to show. Examples down below:



![Single Samples](https://huggingface.co/GeneralAwareness/MirrorMask/resolve/main/mm1.png)![Single Samples](https://huggingface.co/GeneralAwareness/MirrorMask/resolve/main/mm2.png)![Single Samples](https://huggingface.co/GeneralAwareness/MirrorMask/resolve/main/mm3.png)


#### Prompt

An example of calling mirrormask before the prompt (mirrormask a woman)
![Single Samples](https://huggingface.co/GeneralAwareness/MirrorMask/resolve/main/mm.png)

An example of calling mirrormask with a comma before the prompt (mirrormask, a woman)
![Single Samples](https://huggingface.co/GeneralAwareness/MirrorMask/resolve/main/mmcomma.png)

An example of calling mirrormask with the additional word of "by" before the prompt (mirrormask by a woman)
![Single Samples](https://huggingface.co/GeneralAwareness/MirrorMask/resolve/main/mmby.png)

An example of calling mirrormask with the additional word of "in" before the prompt (mirrormask in a woman)
![Single Samples](https://huggingface.co/GeneralAwareness/MirrorMask/resolve/main/mmin.png)

An example of calling the prompt then mirrormask (a woman mirrormask)
![Single Samples](https://huggingface.co/GeneralAwareness/MirrorMask/resolve/main/_mm.png)

An example of calling the prompt then adding a comma before mirrormask (a woman, mirrormask)
![Single Samples](https://huggingface.co/GeneralAwareness/MirrorMask/resolve/main/commamm.png)

An example of calling the prompt then adding the word "in" before mirrormask (a woman in mirrormask)
![Single Samples](https://huggingface.co/GeneralAwareness/MirrorMask/resolve/main/inmm.png)

An example of calling the prompt then adding the word "by" before mirrormask (a woman by mirrormask)
![Single Samples](https://huggingface.co/GeneralAwareness/MirrorMask/resolve/main/bymm.png)

For more variety try adding the word "style" after the token word mirrormask (no examples given to save space).

### 🧨 Diffusers

This model can be used just as you would any other Stable Diffusion style model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
from diffusers import StableDiffusionPipeline
import torch
model_id = "GeneralAwareness/MirrorMask"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "a woman by mirrormask"
image = pipe(prompt).images[0]
image.save("./awoman.png")
```

## License

This model is under a creative commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).

To see what rights you have under this licence follow this link - https://creativecommons.org/licenses/by-nc-sa/4.0/
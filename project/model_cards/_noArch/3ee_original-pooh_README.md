---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- art
- pooh
- artistic
- diffusers
---

# 🐻 Original Pooh Diffusion

Fine-tuned Stable Diffusion model, based of ```F222```, trained with pictures illustrated by ```E. H. Shepard``` from the book "Winnie-the-Pooh", by A. A. Milne, originally published in Canada by McClelland & Stewart, Ltd., 1926. Released into the public domain on January 3, 2022.  

📗 [Winnie-the-Pooh, by A. A. Milne](https://www.gutenberg.org/cache/epub/67098/pg67098-images.html)

![Detailed Samples](https://huggingface.co/3ee/original-pooh/resolve/main/pooh_grid1.png)

## Model Usage

✨ Use the tokens **_original pooh_** in your prompts to activate the model.

![Detailed Samples](https://huggingface.co/3ee/original-pooh/resolve/main/pooh_grid2.png)

![Detailed Samples](https://huggingface.co/3ee/original-pooh/resolve/main/pooh_grid3.png)

![Detailed Samples](https://huggingface.co/3ee/original-pooh/resolve/main/pooh_grid4.png)

![Detailed Samples](https://huggingface.co/3ee/original-pooh/resolve/main/pooh_grid5.png)

![Detailed Samples](https://huggingface.co/3ee/original-pooh/resolve/main/pooh_grid6.png)

![Detailed Samples](https://huggingface.co/3ee/original-pooh/resolve/main/pooh_grid7.png)

---

☕ If you enjoy this model, buy a coffee [![Buy a coffee](https://badgen.net/badge/icon/kofi?icon=kofi&amp;label=buy%20us%20a%20coffee)](https://ko-fi.com/3eegames)

---


## 🧾 Prompt examples:

**Basic starting point**

```original pooh, illustrated by eh shepard ```

[Negative prompt](#❎-negative-prompt-template)

---

**House of Pooh**

```Perfectly-centered portrait deep in a forest with bee nest hanging original pooh, stars, concept art, artstation, illustrated by eh shepard```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 102, Sampler: LMS, CFG scale: 8.5, Seed: 2469061657, Size: 512x512, Model hash: b7ba5b22_

---

**Hanging out at the Hive**

```Perfectly-centered portrait deep in a forest with bee nest hanging original pooh, stars, concept art, artstation, illustrated by eh shepard```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 102, Sampler: LMS, CFG scale: 8.5, Seed: 2469061635, Size: 512x512, Model hash: b7ba5b22_

---


## ❎ Negative Prompt Template

All images were rendered with the negative prompt below:

```text, error, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry, ((ugly)), ((duplicate)), ((morbid)), ((mutilated)), out of frame, red coat, (((red jacket)))```

## 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

Export the model:
- [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx)
- [MPS](https://huggingface.co/docs/diffusers/optimization/mps)
- [FLAX/JAX](https://huggingface.co/blog/stable_diffusion_jax)

```python
from diffusers import StableDiffusionPipeline
import torch

model_id = "3ee/original-pooh"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "original pooh sneaking into a bee nest"
image = pipe(prompt).images[0]

image.save("./pooh_pooh.png")
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

-  You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
-  The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
-  You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
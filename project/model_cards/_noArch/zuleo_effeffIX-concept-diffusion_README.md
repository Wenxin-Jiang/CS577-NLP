---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- art
- artistic
- diffusers
- final fantasy
---

# effeffIX Concept Diffusion


Fine-tuned Stable Diffusion model, based of ```F222```, trained with concept art from a high quality role playing game.

![Detailed Samples](https://huggingface.co/zuleo/effeffIX-concept-diffusion/resolve/main/booth5.png)

## Model Usage

This model was trained on multiple concepts.  Use the tokens below:

| Token                | Description                                          |
|----------------------|------------------------------------------------------|
| effeff9 woman        | Uses concepts trained on female designs.             |
| effeff9 man          | Uses concepts trained on male designs.               |
| effeff9 creature     | Uses concepts trained on different creature designs. |
| effeff9 architecture | Uses concepts trained on architecture design.        |

---

### Examples: effeff9 woman

![Detailed Samples](https://huggingface.co/zuleo/effeffIX-concept-diffusion/resolve/main/booth1.png)

### Examples: effeff9 man

![Detailed Samples](https://huggingface.co/zuleo/effeffIX-concept-diffusion/resolve/main/booth2.png)

### Examples: effeff9 creature

![Detailed Samples](https://huggingface.co/zuleo/effeffIX-concept-diffusion/resolve/main/booth3.png)

### Examples: effeff9 architecture

![Detailed Samples](https://huggingface.co/zuleo/effeffIX-concept-diffusion/resolve/main/booth4.png)


---

☕ If you enjoy this model, buy us a coffee [![Buy a coffee](https://badgen.net/badge/icon/kofi?icon=kofi&amp;label=buy%20us%20a%20coffee)](https://ko-fi.com/3eegames)

---


## 🧾 Prompt examples:

**The amazing Aubrey Plaza**

```Wide shot of a effeff9 woman warrior aubrey plaza with shining armor descending from heaven, lifelike, (highly detailed eyes), super highly detailed face, professional digital painting, artstation, concept art, Unreal Engine 5, HD quality, 8k resolution, beautiful, cinematic, art by artgerm and greg rutkowski and alphonse mucha and loish and WLOP```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 82, Sampler: DPM++ 2M, CFG scale: 8.5, Seed: 695884347, Size: 512x512, Model hash: b7ba5b22_

---

**The Wise Giraffe**

```portrait of a effeff9 creature Giraffe, artstation, concept art, Unreal Engine 5, HD quality, 4k resolution, beautiful, cinematic, art by artgerm and greg rutkowski and alphonse mucha and loish and WLOP```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 90, Sampler: DPM++ 2M Karras, CFG scale: 8.5, Seed: 2821955656, Size: 512x512, Model hash: b7ba5b22_

---

**The drag of the kingdom**

```Wide shot of a grand kingdom, lifelike, super highly detailed, professional digital painting, artstation, concept art, Unreal Engine 5, HD quality, 8k resolution, beautiful, cinematic, art by artgerm and greg rutkowski and alphonse mucha and loish and WLOP, (effeff9 architecture)```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 90, Sampler: DDIM, CFG scale: 13.5, Seed: 2625868484, Size: 512x512, Model hash: b7ba5b22_

---

**The steamy momoa**

```Perfectly-centered portrait of a effeff9 MAN jason momoa with shining scales descending from heaven, concept art, ART STATION, BEAUTIFUL PERFECT detailed MANGA EYES, art by artgerm and greg rutkowski and alphonse mucha and loish and WLOP```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 56, Sampler: DPM++ 2M Karras, CFG scale: 11, Seed: 3257609354, Size: 512x512, Model hash: b7ba5b22_


---


## ❎ Negative Prompt Template

This model offers a unique style where characters typically have larger, exaggerated sleeves and hands.  To supress this style, add more variants to adjust the hand style.

All images were rendered with the negative prompt below:

```Negative prompt: ((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), ((extra limbs)), cloned face, (((disfigured))), out of frame, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))),  (fused fingers), (too many fingers), (((long neck)))```

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

model_id = "zuleo/effeffIX-concept-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "effeff9 woman aubrey plaza"
image = pipe(prompt).images[0]

image.save("./i_luv_aubrey_plaza.png")
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

-  You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
-  The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
-  You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
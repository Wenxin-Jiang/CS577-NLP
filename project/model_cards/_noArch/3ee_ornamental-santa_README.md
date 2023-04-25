---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- art
- artistic
- diffusers
- santa claus
---

# 🎁 Ornamental Santa Diffusion

When you close your eyes and think about what Santa would look like - he’s different for everyone and the hope is this model captures that sense of wonder Santa Claus brought us when we were children.

Fine-tuned Stable Diffusion model, based of ```F222```, trained with pictures from over two hundred Santa Claus themed ornaments and knick-knacks.

![Detailed Samples](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth1.png)

## Model Usage

✨ Use the tokens **_orna santa_** in your prompts to activate the model.

The model was trained on a wide variety of different ornaments, we encourage you to try different variations of vivid prompts.  Below are examples of the model's output.

![Detailed Samples](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth2.png)

![Detailed Samples](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth3.png)

![Detailed Samples](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth4.png)

![Detailed Samples](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth5.png)

![Detailed Samples](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth6.png)

---

☕ If you enjoy this model, buy us a coffee [![Buy a coffee](https://badgen.net/badge/icon/kofi?icon=kofi&amp;label=buy%20us%20a%20coffee)](https://ko-fi.com/3eegames)

---

## 🎨 Using or building a merged model

Merging models is similar to mixing paint.  By adding different models and using multiplers, you can further fine tune models with different styles.

![Detailed Samples](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth_merged1.png)

 **Add more depth: Use the merged model that we've already compiled**:

- Download ```ornasanta_AnythingV3.0_fp16_0.3.ckpt``` located https://huggingface.co/3ee/ornamental-santa/tree/main
- Add ```ornasanta_AnythingV3.0_fp16_0.3.ckpt``` to your Stable Diffusion models.
- Activate merged models with the prompt table below.

| Model      | Prompts                                                                                                                    |
|------------|----------------------------------------------------------------------------------------------------------------------------|
| ornasanta  | orna santa                                                                                                                 |
| AnythingV3 | 1girl, white hair, golden eyes, beautiful eyes, detail, flower meadow, cumulonimbus clouds, lighting, detailed sky, garden |
| Mo Di      | modern disney style                                                                                                        |

This model is merged with [Anythingv3](https://huggingface.co/Linaqruf/anything-v3.0) as the secondary model and [Mo Di Diffusion](https://huggingface.co/nitrosocke/mo-di-diffusion) as the tertiary model.

**Settings to merge these models youself**

You can also merge these models yourself.  See the table below:

| Model      | Weight | Prompts             | Type       |
|------------|--------|---------------------|------------|
| ornasanta  | 0.3    | orna santa          | Primary    |
| AnythingV3 | 0.3    | 1man                | Secondary  |
| Mo Di      | 0.3    | modern disney style | tertiary   |

### Sample Output

**Beefing up the Anything model for anime style:**
![Basic Samples](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth_merged2.png)
**Balacing between MoDi and Anything models:**
![Ornamental Style](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth_merged3.png)
**More weight towards the MoDi model:**
![Landscapes](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth_merged4.png)
**Additional illustration:**
![Landscapes](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth_merged5.png)
**More high detail:**
![Landscapes](https://huggingface.co/3ee/ornamental-santa/resolve/main/booth_merged6.png)


## 🧾 Prompt examples:

**Basic starting point**

```orna santa with cookies```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 18, Sampler: Euler a, CFG scale: 11.5, Seed: 2480441584, Size: 512x512, Model hash: b7ba5b22_

---

**Santa ornament illustration**

```Perfectly-centered of  orna santa mighty warrior standing in flower meadow, ((beautiful eyes)), highly detailed beard, ((dark fantasy)), dynamic lighting, stars,  high quality, 4k, cover photo```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 60, Sampler: DDIM, CFG scale: 15, Seed: 3617510030, Size: 512x512, Model hash: b7ba5b22_

---

**Jolly Santa**

```orna santa, detailed face,trending on artstation, dark fantasy, illustrated by Alex Horley, Sophie Anderson```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 75, Sampler: Heun, CFG scale: 9, Seed: 1852604274, Size: 512x512, Model hash: b7ba5b22_

---

**Fantasy Santa Ornament**

```Perfectly-centered portrait-photograph of a real life godly orna santa with cookies descending from heaven, lifelike, super highly detailed, professional digital painting, artstation, concept art, Unreal Engine 5, Photorealism, HD quality, 8k resolution, cinema 4d, 3D, beautiful, cinematic, art by artgerm and greg rutkowski and alphonse mucha and loish and WLOP```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 80, Sampler: Heun, CFG scale: 8.5, Seed: 2837640579, Size: 512x512, Model hash: b7ba5b22_

---


**Santa face Ornament**

```orna santa standing in a park```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 17, Sampler: Euler a, CFG scale: 7, Seed: 577494771, Size: 512x512, Model hash: b7ba5b22_

---


**Santa face illustration**

```Perfectly-centered portrait-photograph of a real life godly orna santa with cookies descending from heaven, lifelike, super highly detailed, professional digital painting, artstation, concept art, Unreal Engine 5, Photorealism, HD quality, 8k resolution, cinema 4d, 3D, beautiful, cinematic, art by artgerm and greg rutkowski and alphonse mucha and loish and WLOP```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 74, Sampler: DDIM, CFG scale: 4, Seed: 3376117548, Size: 512x512, Model hash: b7ba5b22_

---


### Merged model prompts

These prompts use the merged model: ```ornasanta_AnythingV3.0_fp16_0.3.ckpt``` at located https://huggingface.co/3ee/ornamental-santa/tree/main

**Activate F222 and Mo-Di models**

```Perfectly-centered portrait-photograph of a real life godly 1man orna santa with cookies descending from heaven, stars, lifelike, super highly detailed, professional digital painting, artstation, christmas decor, Unreal Engine 5, Photorealism, HD quality, 8k resolution, cinema 4d, 3D, beautiful, cinematic, modern disney style, white hair, golden eyes, beautiful eyes, detail, flower meadow, cumulonimbus clouds, lighting, detailed sky, garden,art by artgerm and greg rutkowski and alphonse mucha and loish and WLOP_```

_Steps: 32, Sampler: DPM adaptive, CFG scale: 12, Seed: 1639653330, Size: 512x512, Model hash: 697c8786_

[Negative prompt](#❎-negative-prompt-template)

---

**Denzel Santa**

```Perfectly-centered portrait-photograph of a real life godly (((orna santa))) (((Denzel Washington))) 1man standing in flower meadow, beautiful eyes, highly detailed beard, ((sharp focus)), photo by Annie Leibovitz, intricate, natural lighting, stars,  high quality, 4k, cover photo, modern disney style```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 91, Sampler: DPM++ 2S a Karras, CFG scale: 12, Seed: 2072333809, Size: 512x512, Model hash: 254a9dce_

---

**Mike Tyson Santa anime**

```Perfectly-centered portrait-photograph of a real life godly ((orna santa)) (((Mike Tyson))) 1boy standing in flower meadow, beautiful eyes,((sharp focus)), photo by Annie Leibovitz, intricate, natural lighting, stars, high quality, 4k, cover photo, (((modern disney style)))```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 74, Sampler: DDIM, CFG scale: 4.5, Seed: 3117230049, Size: 512x512, Model hash: 254a9dce, Denoising strength: 0.7_

**Child Tyson Santa anime)** (use same prompt)

_Steps: 26, Sampler: DDIM, CFG scale: 7, Seed: 2757414259, Size: 512x512, Model hash: 254a9dce, Denoising strength: 0.7_

---

**Carell Santa**

```orna santa steve carell standing in a park, ((sharp focus)), photo by Annie Leibovitz, intricate, natural lighting, high quality, 4k, cover photo```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 76, Sampler: DDIM, CFG scale: 11, Seed: 120176245, Size: 512x512, Model hash: b7ba5b22_


---

**joaquin phoenix ornament**

```(((orna santa))) (joaquin phoenix) hanging on Christmas tree, modern disney style```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 83, Sampler: LMS, CFG scale: 7.5, Seed: 297089387, Size: 512x512, Model hash: b7ba5b22_

**joaquin phoenix anime** (use same prompt)

_Steps: 83, Sampler: DPM++ 2S a, CFG scale: 10.5, Seed: 162322936, Size: 512x512, Model hash: 254a9dce_

---

**Freeman Santa**

```Perfectly-centered portrait-photograph of a real life godly (((orna santa))) (((morgan freeman))) 1man standing in flower meadow, beautiful eyes, highly detailed beard, ((sharp focus)), photo by Annie Leibovitz, intricate, natural lighting, stars,  high quality, 4k, cover photo, modern disney style```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 74, Sampler: DDIM, CFG scale: 4, Seed: 3376117548, Size: 512x512, Model hash: b7ba5b22_


---


**Robin Santa**

```Perfectly-centered portrait-photograph of a real life godly (((orna santa))) (((robin williams))) 1man standing in flower meadow, beautiful eyes, highly detailed beard, ((sharp focus)), photo by Annie Leibovitz, intricate, natural lighting, stars, high quality, 4k, cover photo, modern disney style```

[Negative prompt](#❎-negative-prompt-template)

_Steps: 91, Sampler: DPM++ 2M, CFG scale: 7.5, Seed: 3556207146, Size: 512x512, Model hash: 697c8786_


---


## ❎ Negative Prompt Template

All images were rendered with the negative prompt below:

```((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))). out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck)))```

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

model_id = "3ee/ornamental-santa"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "orna santa holding a plate of cookies"
image = pipe(prompt).images[0]

image.save("./santa_cookies.png")
```

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

-  You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
-  The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
-  You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---
**Shichigoro Diffusion** v0.2

This is an experimental Stable Diffusion model trained on artworks by artist Shichigoro (https://shichigoro.com/).
Only for personal use! Please respect the original artist!

Use the token **_shichigoro_** in your prompts for the effect.

_shichigoro, woman, breasts, detailed iris, intricate details, sharp focus, red eyes, detailed black hair_
Steps: 37, Sampler: Euler a, CFG scale: 7, Seed: 323609095, Size: 512x768
![Woman](https://huggingface.co/SenorKaffee/shichigoro-diff/resolve/main/samples/323609095_37.jpg)

_shichigoro, lara croft_
Steps: 35, Sampler: Euler a, CFG scale: 7, Seed: 1483473625, Size: 512x768
![Lara Croft](https://huggingface.co/SenorKaffee/shichigoro-diff/resolve/main/samples/1483473625_35.jpg)

_shichigoro, cute cat_
Steps: 35, Sampler: Euler a, CFG scale: 7, Seed: 3304424502, Size: 512x704
![Cute Cat](https://huggingface.co/SenorKaffee/shichigoro-diff/resolve/main/samples/3304424502_35.jpg)

_shichigoro, cute dog_
Steps: 35, Sampler: Euler a, CFG scale: 7, Seed: 3304424516, Size: 512x704
![Cute Dog](https://huggingface.co/SenorKaffee/shichigoro-diff/resolve/main/samples/3304424516_35d.jpg)

_shichigoro, cute dog_
Steps: 35, Sampler: Euler a, CFG scale: 7, Seed: 3304424505, Size: 512x704
![Cute Dog](https://huggingface.co/SenorKaffee/shichigoro-diff/resolve/main/samples/3304424505_35.jpg)

_shichigoro, cow_
Steps: 35, Sampler: Euler a, CFG scale: 7, Seed: 3304424524, Size: 512x704
![Cow](https://huggingface.co/SenorKaffee/shichigoro-diff/resolve/main/samples/3304424524_35c.jpg)

_shichigoro, harry potter_
Steps: 35, Sampler: Euler a, CFG scale: 7, Seed: 3304424516, Size: 512x704
![Harry Potter](https://huggingface.co/SenorKaffee/shichigoro-diff/resolve/main/samples/3304424516_35.jpg)

_shichigoro, johnny depp_
Steps: 35, Sampler: Euler a, CFG scale: 7, Seed: 3304424521, Size: 512x704
![Johnny Depp](https://huggingface.co/SenorKaffee/shichigoro-diff/resolve/main/samples/3304424521_35.jpg)

_shichigoro, keanu reeves_
Steps: 35, Sampler: Euler a, CFG scale: 7, Seed: 3304424524, Size: 512x704
![Keanu Reeves](https://huggingface.co/SenorKaffee/shichigoro-diff/resolve/main/samples/3304424524_35.jpg)

_shichigoro, milla jovovich_
Steps: 35, Sampler: Euler a, CFG scale: 7, Seed: 3304424524, Size: 512x704
![Milla Jovovich](https://huggingface.co/SenorKaffee/shichigoro-diff/resolve/main/samples/3304424524_35m.jpg)

_shichigoro, ALICE IN WONDERLAND_
Steps: 35, Sampler: Euler a, CFG scale: 7, Seed: 3876501189, Size: 512x704
![Alice in Wonderland](https://huggingface.co/SenorKaffee/shichigoro-diff/resolve/main/samples/3876501189_35.jpg)

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

This model was trained using the diffusers based dreambooth training by ShivamShrirao using prior-preservation loss and the _train-text-encoder_ flag in 800 steps.

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
---
license: creativeml-openrail-m
library_name: diffusers
pipeline_tag: text-to-image
---
### MoistMix V1
Based on SD1.5

This is one I have been working a long time on, and I think it's finally ready for release. A do (almost) anything model.

Beautiful lighting, paintings, portraits, multiple photography styles, photorealism, anime and animated styles, alien creatures, armor, clothing, massive dreamy landscapes, abstract retro art, horror, space, nsfw, extremely detailed close ups, and whatever your imagination brings (or AI generated prompts lol).

Combining about a dozen other models/mixes and a few trained on some of my own datasets, I hope you all love this as much as I do, it's the only model I've used for weeks now, slowly perfected into what it is today.


This model includes a CKPT and a SafeTensors filetype which you can use the same way as a CKPT, with (sometimes) increased load speed while avoiding pickles. I am including my VAE as well.


[CKPT download link](https://huggingface.co/MoistMix/MoistMixV1/resolve/main/MoistMix.ckpt)

[SafeTensors download link](https://huggingface.co/MoistMix/MoistMixV1/resolve/main/MoistMix.safetensors)

[VAE download link](https://huggingface.co/MoistMix/MoistMixV1/resolve/main/MoistMix.vae.pt)


**A small sample of images generated with this model:**
![Image Samples](https://huggingface.co/MoistMix/MoistMixV1/resolve/main/MoistMix_Sample%20Grid.jpg)

## License
This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 
1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
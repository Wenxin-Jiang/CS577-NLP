---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
---

[*Click here to download the latest Double Exposure embedding for SD 2.x in higher resolution*](https://huggingface.co/joachimsallstrom/Double-Exposure-Embedding)!

**Double Exposure Diffusion**

This is version 2 of the <i>Double Exposure Diffusion</i> model, trained specifically on images of people and a few animals.
The model file (Double_Exposure_v2.ckpt) can be downloaded on the **Files** page. You trigger double exposure style images using token: **_dublex style_** or just **_dublex_**.  

**Example 1:**
![Sample 1](https://huggingface.co/joachimsallstrom/double-exposure-style/resolve/main/v2_sample_images_1.jpg)

#### Example prompts and settings

<i>Galaxy man (image 1):</i><br>
**dublex man galaxy**<br>
_Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3273014177, Size: 512x512_

<i>Emma Stone (image 2):</i><br>
**dublex style Emma Stone, galaxy**<br>
_Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 250257155, Size: 512x512_

<i>Frodo (image 6):</i><br>
**dublex style young Elijah Wood as (Frodo), portrait, dark nature**<br>
_Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3717002975, Size: 512x512_

<br>

**Example 2:**
![Sample 1](https://huggingface.co/joachimsallstrom/double-exposure-style/resolve/main/v2_sample_images_2.jpg)

#### Example prompts and settings

<i>Scarlett Johansson (image 1):</i><br>
**dublex Scarlett Johansson, (haunted house), black background**<br>
_Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3059560186, Size: 512x512_

<i>Frozen Elsa (image 3):</i><br>
**dublex style Elsa, ice castle**<br>
_Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 2867934627, Size: 512x512_

<i>Wolf (image 4):</i><br>
**dublex style wolf closeup, moon**<br>
_Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 312924946, Size: 512x512_

<br>
<p>
This model was trained using Shivam's DreamBooth model on Google Colab @ 2000 steps.
</p>

The previous version 1 of Double Exposure Diffusion is also available in the **Files** section.

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
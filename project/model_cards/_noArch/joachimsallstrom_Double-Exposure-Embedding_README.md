---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
- embedding
---
# Double Exposure Embedding for Stable Diffusion 2.x

![Sample 1](https://huggingface.co/joachimsallstrom/Double-Exposure-Embedding/resolve/main/sample_images_1.jpg)

[*EMBEDDING DOWNLOAD LINK*](https://huggingface.co/joachimsallstrom/Double-Exposure-Embedding/resolve/main/dblx.pt) - This is the <i>Double Exposure Embedding</i> for SD 2.x. 

It was trained with the *v2.1 768 ema pruned* model on 768px images of people, layered with a variety of surroundings. It's been shown to handle objects and animals good as well. 

1. Place the file in the embeddings folder of your Automatic1111 installation. 

2. Trigger the effect in the prompt by writing **dblx**.
<p>
  
### Example prompts and settings

![Sample 1](https://huggingface.co/joachimsallstrom/Double-Exposure-Embedding/resolve/main/sample_images_2.jpg)

<i>Left image:</i><br>
**a profile photo of a woman and a city, photo by dblx**<br>
_Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1965858791, Size: 1088x768, Model hash: 4bdfc29c_

<i>Right image:</i><br>
**woman photo closeup soap bubbles, photo by dblx**<br>
Negative prompt: **deformed, ugly**<br>
_Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3612934306, Size: 1152x768, Model hash: 4bdfc29c_


![Sample 1](https://huggingface.co/joachimsallstrom/Double-Exposure-Embedding/resolve/main/sample_images_3.jpg)

All prompts and settings for the other images can be found [*in this document*](https://huggingface.co/joachimsallstrom/Double-Exposure-Embedding/resolve/main/dblx_prompts_settings.pdf).

This embedding was trained locally with Automatic1111's webui.

The previous Double Exposure models for Stable Diffusion 1.5 can be found [here](https://huggingface.co/joachimsallstrom/Double-Exposure-Diffusion).

## Image credit

Made by masslevel:<br>
_woman rising from ocean_<br>
_cloud glass_<br>
_smiling geisha_<br>
_woman with ocean + flower hair_<br>
_woman with galaxy hair_

Made by [*spaablauw aka Stille Willem*](https://huggingface.co/spaablauw):<br>
_diamond mountain_<br>
_fox_

Made by Klinter:<br>
_american steak flag_

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
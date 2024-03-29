---
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/tuwonga/takeON/resolve/main/takeON_prev.jpg"
tags:
- stable-diffusion
- text-to-image
---
### takeON
This is a fine-tuned Stable Diffusion model (based on v1.5) trained on screenshots from 80s music video **Take on me** (from A-HA band). Use the token **_takeON_** in your prompts to use the style.

_Download the ckpt file from "files and versions" tab into the stable diffusion models folder of your web-ui of choice._

--

**Characters and scenes rendered with this model:**
![Character Samples](https://huggingface.co/tuwonga/takeON/resolve/main/takeON_prev.jpg)

  _prompt and settings used: **[person/scene] in takeON style** | **Steps: 25, Sampler: Euler, CFG scale: 7.5**_
  
--

_**Note:** The model works better on characters than landscape/scenes_

--

This model was trained with Dreambooth training by TheLastBen, using 64 images at 6400 steps with 25% of text encoder.

--

## License
This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 
1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
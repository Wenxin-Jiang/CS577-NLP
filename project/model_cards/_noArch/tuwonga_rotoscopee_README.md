---
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/tuwonga/rotoscopee/resolve/main/rotoscopee_prev1.jpg"
tags:
- stable-diffusion
- text-to-image
---
### Rotoscopee

This is a fine-tuned Stable Diffusion model (based on v1.5) trained on screenshots from the following rotoscope animations :  **_A Scanner Darkly_** movie, **_Undone_** tv series, **_Tehran Taboo_** movie. Use the token **_rotoscopee_** in your prompts to use the style.

_Download the ckpt file from "files and versions" tab into the stable diffusion models folder of your web-ui of choice._

--

**Characters rendered with this model:**
![Character Samples](https://huggingface.co/tuwonga/rotoscopee/resolve/main/rotoscopee_prev1.jpg)
  _prompt and settings used: **[person] in rotoscopee style** | **Steps: 20, Sampler: Euler, CFG scale: 7**_

--

**Landscapes/scenes/animal rendered with this model:**
![Landscape Samples](https://huggingface.co/tuwonga/rotoscopee/resolve/main/rotoscopee_prev2.jpg)
  _prompt and settings used: **city/scene/dog in rotoscopee style** | **Steps: 20, Sampler: Euler, CFG scale: 7**_

--

**Note:** The model works better on characters than landscape/scenes

--

This model was trained with Dreambooth training by TheLastBen, using 50 images at 5000 steps.

--

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
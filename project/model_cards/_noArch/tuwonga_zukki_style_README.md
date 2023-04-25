---
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/tuwonga/zukki_style/resolve/main/zukki_style_prev.jpg"
tags:
- stable-diffusion
- text-to-image
---
### zukki_style
This is a fine-tuned Stable Diffusion model (based on v1.5) trained on screenshots from **Ma vie de courgette** stop motion animation movie.Use the token **_zukki_style_** in your prompts to use the style.

_Download the ckpt file from "files and versions" tab into the stable diffusion models folder of your web-ui of choice._

_Actually this is an experimental model because mainly is possible to render charcters instead of scene/landscapes but I've found more interesting the output in the img2img than txt2img. You can see the results in the second and third pic (original/img2img/img2img). I think would be better to check the "restore faces" option and play around with denoising strength._

--
**Characters rendered with this model:**
![Character Samples](https://huggingface.co/tuwonga/zukki_style/resolve/main/zukki_style_prev.jpg)
  _prompt and settings used: **[person] in zukki_style** | **Steps: 30, Sampler: Euler, CFG scale: 7.5**_
  
--
**Characters rendered with img2img:**
![Character Samples](https://huggingface.co/tuwonga/zukki_style/resolve/main/zukki_style_prev2.jpg)
  _prompt and settings used: **[person] in zukki_style** | **Steps: 30 - you can play around with settings**_

--
**Characters rendered with img2img:**
![Character Samples](https://huggingface.co/tuwonga/zukki_style/resolve/main/zukki_style_prev3.jpg)
  _prompt and settings used: **[person] in zukki_style** | **Steps: 30 - you can play around with settings**_    
  
--
This model was trained with Dreambooth training by TheLastBen, using 32 images at 6400 steps with 25% of text encoder.
--
## License
This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 
1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
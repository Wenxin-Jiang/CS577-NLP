---
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/tuwonga/dbluth/resolve/main/dbluth_prev1.jpg"
tags:
- stable-diffusion
- text-to-image
---
### dbluth
I played a lot in my childhood at laser disc videogames so this model is my personal tribute to the great Disney animator Don Bluth.This is a fine-tuned Stable Diffusion model (based on v1.5), I've trained three different models from videogames laser disc **Dragon's Lair** , **Space Ace** and **Dragon's Lair II Time Warp** then I merged these models into a single one called dbluth.
 Use the token **_dbluth_** in your prompts to use the style.
_Download the ckpt file from "files and versions" tab into the stable diffusion models folder of your web-ui of choice._
The model is pretty similar to Disney classic model because of course Don Bluth was one of the main animator in classic Disney era.
_I've found interesting the output in the img2img generation. You can see the results in the second image (original/img2img)._

**Characters and rendered with this model:**
![Character Samples](https://huggingface.co/tuwonga/dbluth/resolve/main/dbluth_prev1.jpg)
  _prompt and settings used: **[person] in dbluth style** | **Steps: 30, Sampler: Euler, CFG scale: 7.5**_
  
  

**Characters rendered with img2img:**
![Character Samples](https://huggingface.co/tuwonga/dbluth/resolve/main/dbluth_prev2.jpg)
  _prompt and settings used: **[person] in dbluth style** | **Steps: 30 - denoising stregth around 50/70 but you can play around with settings**_
  
--
This model was trained with Dreambooth training by TheLastBen, using 40 images at 8000 steps with 20% of text encoder for each model and then merged in a single one with Automatic1111 webui checkpoint merger.
--
## License
This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 
1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
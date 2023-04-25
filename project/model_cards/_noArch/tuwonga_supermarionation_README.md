---
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/tuwonga/supermarionation/resolve/main/supermarionation_prev1.jpg"
tags:
- stable-diffusion
- text-to-image
---
### supermarionation
This is a fine-tuned Stable Diffusion model (based on v1.5) trained on screenshots from Gerry Anderson **_Supermarionation_** stop motion animation movie, basically from **_Thunderbirds_** tv series. Use the token **_supermarionation_** in your prompts to use the style.

_Download the ckpt file from "files and versions" tab into the stable diffusion models folder of your web-ui of choice._
_I've found interesting (and really funny ^^) the output in the img2img. You can see the results in the second and third pic (original/img2img). You can play around with denoising strength (40-70) and activate or not the restore face option._

### supermarionation v2
In this version I've trained characters and vehicles. 47 images and 9400 steps, 20% text encoder.

-- **Characters and vehicles rendered with this model:**
![Character Samples](https://huggingface.co/tuwonga/supermarionation/resolve/main/supermarionation_v2_prev1.jpg)
  _prompt and settings used: **[person/vehicle] in supermarionation style** | **Steps: 30, Sampler: Euler, CFG scale: 7.5**_
  

**Characters rendered with img2img:**
![Character Samples](https://huggingface.co/tuwonga/supermarionation/resolve/main/supermarionation_v2_prev2.jpg)
  _prompt and settings used: **[person] in supermarionation style** | **Steps: 30 - you can play around with settings**_


**Characters rendered with supermarionation in txt2img:**
![Character Samples](https://huggingface.co/tuwonga/supermarionation/resolve/main/supermarionation_prev1.jpg)
  _prompt and settings used: **[person] in supermarionation style** | **Steps: 40 - you can play around with settings**_ 

**Characters rendered with supermarionation in img2img:**
![Character Samples](https://huggingface.co/tuwonga/supermarionation/resolve/main/supermarionation_prev2.jpg)
  _prompt and settings used: **[person] in supermarionation style** | **Steps: 40 - you can play around with settings**_   
  
--
Supermarionation v1 was trained with Dreambooth training by TheLastBen, using 43 images at 8600 steps with 18% of text encoder.
--
## License
This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 
1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
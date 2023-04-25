---
license: creativeml-openrail-m
language:
- en
library_name: diffusers
pipeline_tag: text-to-image
tags:
- waifu-diffusion
---

# Model Card for Model ID

Anime models mix for stable diffusion



## Model Description

NEW GREAT MODELS MIX 
Call it SkyrMix


This model is 50% weighted mix of:

https://huggingface.co/andite/anything-v4.0/blob/main/anything-v4.0-pruned.safetensors

and

https://huggingface.co/WarriorMama777/OrangeMixs/blob/main/AbyssOrangeMix2/AbyssOrangeMix2_nsfw.safetensors

use same settings

- **Developed by:** Reszka
- **Model type:** Anime/NSFW
- **License:** CreativeML OpenRAIL-M license


# Uses

Sampler: “DPM++ SDE Karras” is good
Steps: forTest: 12～ ,illustration: 20～
Clipskip: 1 or 2
Upscaler : Latenet (nearest-exact)
CFG Scale : 5 or 6 (4～8)
Denoise strength: 0.5 (0.45~0.6)
If you use 0.7～, the picture will change too much.
If below 0.45, Block noise occurs.


## Recommendations

Use bad_prompt_version2, bad-hands5 and bad-artist for better results

<details>
<summary> Click to expand </summary>

</details>
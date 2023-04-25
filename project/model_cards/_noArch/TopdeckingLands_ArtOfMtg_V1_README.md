---
language:
- en
license: cc-by-nc-4.0
thumbnail: "https://huggingface.co/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/land.png"
tags:
- stable-diffusion
- text-to-image
---

# Art of MtG v1

Experimenal model, based on ~5000 arts for cards from Magic: the Gathering game on top of SD1.5 model. Large variety of cards from 2014 to 2022 was used. Logos, guild/clan icons and mana symbols were not part of training set as Fan Content Policy explicitly prohibits their use. Each art was captioned with card name, artist, colors and name of color combination, type line, set name and BLIP description. 

You can try it out on [Huggingface Space](https://huggingface.co/spaces/TopdeckingLands/Diffusion_Space) (probably slow) and [Google Colab](https://colab.research.google.com/drive/109CvcHvmfTv3hlS8DSetiky9kH1WVKFf)

## Usage

_**mtg art**_ is the main prompt to use, and adding _**card frame**_ negative prompt is recommended.

Model has understanding of some planes, terms and characters to different degree. Previews below use negative prompt _lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry_, Euler sampler, 20 steps and CFG 7.

### Planes

Planes that did not have sets named after them are unknown to model. 

![Planes demo](/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/planes.png)

### Characters

Even main cast of planeswalkers that appear often does not work consistently, even if it's often possible to recognize character - the styles are wildly different between specific original arts.

![Planeswalkers demo](/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/walkers.png)

### Species

Model has good understanding of _**phyrexian**_ and Emrakul(tentacle) type of _**eldrazi**_ among others

![Species demo](/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/species.png)

### Artists

A total of 200 artists had at least 5 images included, 50 of them had more than 30 each. It's safe to expect every major modern MtG artist style to be represented and reproducible to some degree. Styles are not supposed to be representative of artist's real style and are biased by types and colors of cards illustrated by them.

![Artists demo](/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/artists1.png)
![Artists demo](/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/artists2.png)
![Artists demo](/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/artists3.png)
![Artists demo](/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/artists4.png)
![Artists demo](/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/artists5.png)

### Color combination names used

* 0-color: colorless
* 1-color: monowhite, monoblue, monoblack, monored, monogreen
* 2-color: guilds of Ravnica
* 3-color: shards of Alara, clans of Tarkir, triomes of Ikoria, families of New Capenna (relevant two)
* 4-color: no special names
* 5-color: WUBRG

Different color combinations have different aesthetic attached. X room for example:

![0, 1 and 5 colors](/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/colors1.png)
![2 colors](/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/colors2.png)
![3 colors](/TopdeckingLands/ArtOfMtg_V1/resolve/main/previews/colors3.png)

## Improvements considered for V2

* Filter out highly off-style Secret Lar card / Variations
* Use scryfall art tags for descriptions in addition to BLIP, dropping use of color combination names
* Add more character-centric data or refine on their art after main training
* Fix BLIP hiccups hiccups hiccups hiccups hiccups hiccups hiccups hiccups

---

Fine-tuning data was provided by Wizards of the Coast under their [Fan Content Policy](https://company.wizards.com/en/legal/fancontentpolicy). Note you can't use this model for commercial purposes, as it's strongly against given policy.
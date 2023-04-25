---

language:
- en
license: other
thumbnail: "https://huggingface.co/ai-characters/Darkest-Diffusion/resolve/main/gandr-collage.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image

---
### Darkest-Diffusion-v1.0

#### Disclaimer

**None of the images that were used to train this or any of my other models were created by me or are owned by me.** 

If you are the owner of some of the images and would like them removed from the model, contact me (AIGeneratedCharacters@mailbox.org) and I will train a new version of the model in question without them included. The old model and dataset version will then be deleted. A public link to the dataset used for this model can be found down below on this page.

#### Example generations (scroll down for the full prompt information of how these were generated)
![Thumbnail](https://huggingface.co/ai-characters/Darkest-Diffusion/resolve/main/gandr-collage.jpg)

A free and open source Stable Diffusion model created by *AI-Characters*, trained on the artstyle of the game "**Darkest Dungeon**". The model was trained at a **512x512** resolution using **Stable Diffusion v1.5** as a base model. 

Write "***in the artstyle of dd***" in your prompt to trigger the artstyle!

#### Social Media

[![KoFi](https://badgen.net/badge/icon/kofi?icon=kofi&label)](https://ko-fi.com/aicharacters)

[![Instagram](https://badgen.net/badge/instagram/ai_characters/purple?icon=github)](https://www.instagram.com/ai_characters/)

[![Twitter](https://badgen.net/badge/twitter/ai_characters/blue?icon=github)](https://twitter.com/ai_characters/)

**I appreciate any donations to my KoFi to help me fund renting GPU's for further model creation and experimentation!** I experiment a lot to achieve the highest possible model quality and flexbility, but this much experimentation requires me to train a lot of different models which in turn costs me a lot in GPU renting costs. So any amount of donations would help me greatly to offset some of the costs! 

## Recommended settings

These are my recommended settings for quick high quality results. These are also the settings on which I tested the model.

- Sampler: Euler_a

- Steps: 20

- CFG: 7

- Resolution: 512x512, then rescaled to 1024x1024 using either high-res fix or Img2Img

## Tips and Tricks

###### I recommend using a UI that supports high-res fix, Img2Img, and negative prompts at the very least. Personally I use the "Automatic1111 WebUI".

- **Rescale to a 1024x1024 resolution** using either Img2Img or high-res fix at a 0.5 denoising strength for much better, higher quality results.

- Use "in the artstyle of dd" as a **negative prompt**, if you want to generate images that are closer to what the standard StableDiffusion model would generate. Be mindful however, that due to the nature of how this model was trained the output generated via this way will still look different from the original vanilla model.

- Use "armor" and "medieval" as **negative prompts** to achieve more modern looking results. No guruantee that it will always work however. At times it may also reduce the output quality.

- If you notice recurring elements in your outputs, such as every output image having sunglasses in it, make said recurring element a **negative prompt**. No guruantee that it will work.

- Emphasize the artstyle like **(artstyle of dd:1.3)** to get the classic Darkest Dungeon style black eyes as can be seen in the image examples down below!

![Black Eyes](https://huggingface.co/ai-characters/Darkest-Diffusion/resolve/main/black%20eyes.jpg)

- Change the wording of the prompt and use negative prompts to get more varied results! Compare the following two examples (prompts see in the prompt section):

![knight](https://huggingface.co/ai-characters/Darkest-Diffusion/resolve/main/grid-0083.png)

![varied knight](https://huggingface.co/ai-characters/Darkest-Diffusion/resolve/main/grid-0082.png)

**But I much recommend doing an initial generation in the vanilla v1.5 Stable Diffusion model and then using Img2Img in my model to transfer the Darkest Dungeon artstyle to that initial generation to get more varied results instead, as one can get more varied outputs in the original v1.5 Stable Diffusion model!**

See below for an example!

## Img2Img example

Here is an example of how to do effective Img2Img with this model!

First I did an initial Txt2Img generation in the vanilla v1.5 Stable Diffusion model with the following prompt:

- Emma Watson wearing a Supergirl outfit and standing in a street in New York City
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3210643789, Size: 512x512, Model hash: a2a802b2, Batch size: 2, Batch pos: 0

![example1](https://huggingface.co/ai-characters/Darkest-Diffusion/resolve/main/00364-3210643789-Emma%20Watson%20wearing%20a%20Supergirl%20outfit%20and%20standing%20in%20a%20street%20in%20New%20York%20City.png)

I then switched models to my Darkest-Diffusion v1.0 model and did a first Img2Img pass at a 512x512 resolution with the following settings:

- digital artwork in the artstyle of dd of Emma Watson wearing a Supergirl outfit and standing in a street in New York City
Negative prompt: photo, photograph, instagram
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 4005497546, Size: 512x512, Model hash: 6ae1720a, Denoising strength: 0.5, Mask blur: 4

![example2](https://huggingface.co/ai-characters/Darkest-Diffusion/resolve/main/00399-4005497546-digital%20artwork%20in%20the%20artstyle%20of%20dd%20of%20Emma%20Watson%20wearing%20a%20Supergirl%20outfit%20and%20standing%20in%20a%20street%20in%20New%20York%20City.png)

I then did a couple more (3-5) passes with the artstyle being more emphasized in the prompt (artstyle of dd:1.3) and had the final pass rescaled to 1024x1024:

- digital artwork in the (artstyle of dd:1.3) of Emma Watson wearing a Supergirl outfit and standing in a street in New York City
Negative prompt: photo, photograph, instagram
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 970774608, Size: 1024x1024, Model hash: 6ae1720a, Denoising strength: 0.4, Mask blur: 4

![example3](https://huggingface.co/ai-characters/Darkest-Diffusion/resolve/main/00416-970774608-digital%20artwork%20in%20the%20(artstyle%20of%20dd_1.3)%20of%20Emma%20Watson%20wearing%20a%20Supergirl%20outfit%20and%20standing%20in%20a%20street%20in%20New%20York%20City.png)

## Prompts and settings used to generate the examples found in the thumbnail of this page, in order

- facial closeup artwork in the artstyle of dd of a princess
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1199794856, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0, Denoising strength: 0.5, First pass size: 512x512
- character art in the artstyle of dd of Supergirl
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 2738426192, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0, Denoising strength: 0.5, First pass size: 512x512
- (full-body full-length full-shot:1.3) character art in the artstyle of dd of (Zendaya:1.4) wearing helmetless armor and a cape and holding one spear
Negative prompt: (helmet), (half-body, half-length, medium shot), man, male, cloak, hoodie
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 229405137, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0, Denoising strength: 0.5, First pass size: 512x512
- artwork in the artstyle of dd of Emma Watson standing in a street in New York City wearing a tshirt and jeans
Negative prompt: sunglasses
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 2287424046, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0, Denoising strength: 0.5, First pass size: 512x512
- artwork in the artstyle of dd of a winged fairy with butterfly wings in a (sunny forest clearing:1.3) wearing fancy fairy dress happy light atmosphere
Negative prompt: armor
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 761962005, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0, Denoising strength: 0.5, First pass size: 512x512
- artwork in the artstyle of dd of a winged fairy with butterfly wings (in a dark forest clearing:1.3) wearing fancy fairy dress dark moody atmosphere
Negative prompt: armor
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 2510528777, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0, Denoising strength: 0.5, First pass size: 512x512
- character art in the artstyle of dd of Ellie from Last of Us with feathered wings
Negative prompt: armor, 3d video game render, man, rifle, gun, holding
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1202360977, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 1, Denoising strength: 0.5, First pass size: 512x512
- artwork in the artstyle of dd of the animal pig
Negative prompt: human, people, person, humanoid, armor, clothing, soldier, knight
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1357521697, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 1, Denoising strength: 0.5, First pass size: 512x512
- landscape art in the artstyle of dd of a mountain valley with a river flowing through
Negative prompt: house, building, houses, buildings, city, town, civilization
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1359049560, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0, Denoising strength: 0.5, First pass size: 512x512
- landscape art in the artstyle of dd of a modern city with skyscrapers
Negative prompt: medieval
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3002591719, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0, Denoising strength: 0.5, First pass size: 512x512
- artwork in the artstyle of dd of a car
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 856392436, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0, Denoising strength: 0.5, First pass size: 512x512
- artwork in the artstyle of dd of a modern car
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1281304113, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 1, Denoising strength: 0.5, First pass size: 512x512

**Prompts for the image examples of the Darkest Dungeon style black eyes from the "Tips and Tricks" section of this page:**

- facial closeup artwork (in the artstyle of dd:1.3) of a princess
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 871645361, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0, Denoising strength: 0.5, First pass size: 512x512

- character art in the (artstyle of dd:1.3) of Supergirl
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1528142431, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 1, Denoising strength: 0.5, First pass size: 512x512

- (full-body full-length full-shot:1.3) character art in the (artstyle of dd:1.3) of Zendaya
Negative prompt: (half-body, half-length, medium shot)
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 3902706159, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 1, Denoising strength: 0.5, First pass size: 512x512

- artwork in the (artstyle of dd:1.3) of a winged fairy with butterfly wings in a (sunny forest clearing:1.3) wearing fancy fairy dress happy light atmosphere
Negative prompt: armor
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1556219471, Size: 1024x1024, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0, Denoising strength: 0.5, First pass size: 512x512

**Prompts for the two knight examples:**

- artwork in the artstyle of dd of a knight
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 1013797835, Size: 512x512, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0

- a man as a knight wearing partial armor in the dd style
Negative prompt: armor
Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 721362658, Size: 512x512, Model hash: 6ae1720a, Batch size: 2, Batch pos: 0

## Current shortcomings of the model

- The model is "infected" by the training, which means that using it to generate images not in the "dd artstyle" will generate output that will be different from what you would get in the original Stable Diffusion model

- The model may struggle at times with more complex prompts

- The model is better at simple character art than it is at anything else (e.g. landscapes), though you can still use it for those other art types

- No unique characters, classes, locations, or items of the game have been trained or captioned and thus cannot be deliberately prompted to appear

- Some prompts may not be very varied in their output; in that case use either Img2Img to transfer the Darkest Dungeon artstyle (see above for an example) to a vanilla v1.5 Stable Diffusion generation, as one can get more varied outputs in the original v1.5 Stable Diffusion model, or reword the prompt and use negative prompts for more varied outputs!

## Outlook into the future

I am currently in the process of creating many different high-quality models for various concepts. This is taking a lot of time as I am manually gathering thousands of high quality images from Fancaps.net, Artstation, DeviantArt, Pinterest, Google's image search, among others. I am then also manually editing and captioning those images for the highest possible quality. I then may also have to create different models to test various different settings and captions which will also take a lot of time (and money). So please be patient for new model releases. **If you want to support me, any amount donated to my Kofi would help greatly to offset the training costs!**

Here is a non-exhaustive list of various concepts for which I am currently working on or am planning to make models for (however no guruantees that all of them will result in a final model in the end):

- Chainsaw Man (2022)
- Castle in the Sky
- Nausicaä of the Valley of the Wind; Nausicaä
- Legend of Korra; Korra; all the other characters
- She-Ra and the Princesses of Power; Adora/She-Ra
- The Dragon Prince; Rayla
- StarWars: The Clone Wars; Ahsoka
- Fallout 4
- How To Train Your Dragon; Astrid
- Incredibles 2
- Raya and The Last Dragon; Raya
- Overwatch; Mercy
- Horizon: Zero Dawn/Forbidden West; Aloy
- Last of Us 2; Ellie
- Kena: Bridge of Spirits; Kena
- Supergirl
- Final Fantasy XII
- Final Fantasy XIII; Lighting
- Pantheon (2022)
- Harley Quinn (2019)
- Weathering with You
- 90s + 80s anime style
- high quality video game renders
- high quality modern western animation
- high quality modern generic anime
- high quality modern realistic anime
- high quality modern 3d animation

**Currently "On-Hold" until I have a more ethical dataset available:**

- muscle growth and strong women
- size growth and giantess and tall women
- hybrids (e.g. a dragon-human hybrid)
- winged women
- transformations (e.g. a woman transforming into a dragon)
- General scifi art/subjects
- General fantasy art/subjects
- high quality photos
- high quality stylised digital art
- high quality realistic detailed digital art
- high quality grey pencil drawings
- high quality colored pencil drawings

**Published models:**

- Darkest-Diffusion v1.0 **(you are here)**
- [4elements-diffusion v1.0](https://huggingface.co/ai-characters/4elements-diffusion) (Outdated)


## How I created this model and the underlying dataset (+ dataset download link!)

I wanted to test various different methods of captioning images as well as training on various different resolutions. For that I needed a model that can be created using only a small dataset so that testing times and expenses are kept low. Thus I randomly came up with this Darkest Dungeon model, which uses only 14 training images (initally only 11).

I took the images from google image search as well as [Riot Pixels](https://en.riotpixels.com/games/darkest-dungeon/). I chose only the most cleanest and highest quality images. I then further edited the images to take out watermarks and texts as well as remove unneccessary noise in the image. I also cropped the images a bit.

I created many different models to complete my testing and to find the most optimal settings and caption style to create a Darkest Dungeon model with the highest possible quality.

**[The captioned and edited dataset that I used to train this model with can be found here!](https://huggingface.co/datasets/ai-characters/Darkest-Diffusion-v1.0-Dataset)**

I trained this model using the ["EverDream" repo](https://github.com/victorchall/EveryDream-trainer) with filename captions. I captioned the images using the [BatchPrompter](https://github.com/Snowad14/BatchPrompter).

For the training I used the v1-finetune_everydream.yaml file with the following settings:

- Learning rate: 1e-6

- Repeats: 250

- Epochs: 1

- Batch size: 1

- Conditional dropout: 0.05

- Resolution: 512

For a more in-depth guide on how to actually setup and use the EverDream repo, please look up other tutorials on the web, especially YouTube or Reddit, or visit the [EverDream Discord](https://discord.gg/uheqxU6sXN)!

## Alternative Download Links

[Alternative download link for the model](https://www.dropbox.com/s/b275sirplii0iwk/Darkest-Diffusion-v1.0.ckpt?dl=0)

[Alternative download link for the captioned dataset](https://www.dropbox.com/s/qkd93vqfxjt9zkd/14%20%27Darkest%20Dungeon%27%20trainiing%20images.7z?dl=0)

## License

This model is open access and available to all, with a modified CreativeML OpenRAIL-M license for **non-commercial use only** further specifying rights and usage. This modified CreativeML OpenRAIL License specifies:

1. **You cannot use this model to generate so-called "NFTs" or "Non-fungible Tokens"**
2. **You can't host or use the model or its derivatives or inference or finetuning based on those on websites/apps/etc., from which you earn, will earn, or plan to earn revenue, unless you offer those services for the model in question for free.**
3. **You are free to host the model or its derivatives on completely non-commercial websites/apps/etc. Please state the full model name (Darkest-Diffusion v1.0) and include a link to the model card (https://huggingface.co/ai-characters/Darkest-Diffusion).**
2. You can't use the model to deliberately produce nor share illegal or harmful outputs or content
3. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
4. You may re-distribute the weights. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of this **modified CreativeML OpenRAIL-M for non-commercial use only** to all your users (please read the license entirely and carefully) [Please read the full license here](https://huggingface.co/ai-characters/Darkest-Diffusion/blob/main/License%20-%20Modified%20CreativeML%20Open%20RAIL-M%20for%20non-commercial%20use%20only)
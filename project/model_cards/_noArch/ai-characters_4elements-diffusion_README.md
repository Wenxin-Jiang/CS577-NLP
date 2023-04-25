---

language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/gandr-collage.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image

---
# 4elements-diffusion

##### A StableDiffusion All-In-One Legend of Korra style + Korra character Dreambooth model created by AI-Characters

#### For what tokens to use in your prompts to employ the desired effects scroll down to the following section of this page: "Tokens to use to prompt the artstyle as well as Korra's different outfits"

![Thumbnail](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/gandr-collage.jpg)

**Feel free to donate to my [KoFi](https://ko-fi.com/aicharacters)** to help me fund renting GPU's for further model creation and experimentation!

Follow me on [Twitter](https://twitter.com/ai_characters) and [Instagram](https://www.instagram.com/ai_characters/) for AI art posts and model updates! 

## Quick Feature Overview

- Create anyone and anything in the LoK artstyle! 

- Create Korra in any artstyle! 

- Mix and match all of Korra's outfits however you want to!

- Give anyone Korra's outfits! 

- Give Korra any outfits!

*This model is much trickier to use than other models, but in return it is very flexible and has high likeness!* **I thus highly recommend checking out the "How to correctly use this model" section of this page!**

--- This model is not yet final! I will keep working on it and trying to improve it! I also welcome anyone to use my uploaded dataset (see at the bottom of this page) to create a better version! ---

## IMPORTANT INFORMATION BEFORE YOU USE THIS MODEL
 
I highly recommend using img2img when using this model, either by converting photos into the Legend of Korra artstyle or by resizing your initial 512x512 txt2img Legend of Korra style generations up to 1024x1024 or higher resolutions. **Your initial 512x512 txt2img generations using the Legend of Korra artstyle WILL ALWAYS look like crap** if you generate shots of characters that are more zoomed out than just a closeup (e.g. half-body or full-shot). **Resizing the initial 512x512 generations to 1024x1024 or bigger** (full-shots will likely need 1536x1536 to look good) using img2img **will drastically improve your experience using this model!**

The model is also infected, e.g. photos output with this model WILL look different from those output in the vanilla SD model! So I recommend generating people in the vanilla SD model using txt2img first and then sending them to img2img and switching the model to this one and then applying the style! This way your result is more true to vanilla SD but just with the style applied!

**For more useful information on how to correctly use this model, see the "How to correctly use this model" section of this page!**

## Introduction

Welcome to my first ever published StableDiffusion model and the first public model **trained on the Legend of Korra artstyle**! But not just the artstyle: **I have trained this model on Korra, including *all* of her outfits, as well!** In total this model was trained using a manually captioned dataset of 1142 images: screencaps from the show, fanart, and cosplay photos.

I spent every day the last 4 weeks working on this project and spent hundreds of euros renting many many many GPU hours on VastAI to experiment with various parameters. I have created more than 50 ckpt's since then and learned a ton since then and got a ton of insight.

## Recommended samplers, steps, CFG values and denoising strength settings (for img2img)

- Euler a at 20 steps for quick results

- LMS at 100-150 steps for higher quality results that also follow your prompt more closely

- DPM++ 2M Karras at 20 steps for an alternative to EulerA

- CFG value from 7 to 4 (4 can look better in terms of image quality because it will have less of the overtraining effect, but it can also look less detailed)

- denoising strength of 0.4-0.6 for general img2img, and up to around 0.8 for more harcore cases where the style needs more denoising to be correctly applied (thoughthat will change the image of course, consider also to just do multiple runs through 0.5-0.6)

## How to correctly use this model (it's not as simple as the other models floating around the web currently!)

This model is not as easy to use as some of the other models you might be used to. For good results prompt engineering and img2img resizing is required. I highly recommend tinkering with the prompt weights, word order in the prompt, samplers, cfg and step values, etc! The results can be well worth it!

**My recommendation is to generate a photo in the vanilla SD model, send it to img2img, then switching the model to this one, and using the img2img function to transfer the style to the Legend of Korra style!** Also consider inpainting (though this model isn't trained on the new base inpainting model yet)! **I also recommend to keep prompts simple and the "zoom" closer to the character for better results! Though sometimes a highly complex prompt can also result in much better generations**, e.g. "Emma Watson, tlok artstyle" will almost always produce much worse results than a more complex prompt!

- **The most important bit first: SD doesn't play well with the artstyle at the standard 512x512. So your initial 512x512 generations in the artstyle will need to be resized to 1024x1024 for half-body shots and 1536x1536 for full-body shots in order to look good.** Closeups will look okay in 512x512 but I still recommend upscaling to 1024x1024.

An example:

Initial 512x512 generation

![Initial 512x512 generation](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/29103-3085544956-full-shot%20Emma%20Watson%20standing%20city%20street%20background%20day%20tlok%20artstyle.png)

Upscaled to 1024x1024 (with an inpainted face)

![Upscaled to 1024x1024 (with an inpainted face)](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00405-773303902-facial%20closeup%20Emma%20Watson%20standing%20city%20street%20background%20day%20tlok%20artstyle.png)

Upscaled to 1526x1536 (with an inpainted face)

![Upscaled to 1526x1536 (with an inpainted face)](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00410-2273971619-facial%20closeup%20big%20eyes%20Emma%20Watson%20standing%20city%20street%20background%20day%20tlok%20artstyle.png)

- **I highly recommend using the following negative prompt for *all* generations** (no matter what style, aka it massively improves the tlok artstyle generations as well!): 

**blur, vignette, instagram**

This will drastically reduce the "overtrained effect" of the generations, e.g. too bright, vignetted and fried images. I have no idea why that works. It just does.

Examples:

Without the negative prompt:

![Without the negative prompt](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/grid-0164.png)

With the negative prompt:

![With the negative prompt)](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/grid-0165.png)

- Only for photos: You can add "photo, tlok artstyle" to the negative prompt for a further reduction in the "overtrained effect"! Doesn't always work, but sometimes does! Having photo in both the positive and negative prompt may sound nonsensical, but it works!

- **Also consider going from a CFG value of 7 down to a CFG value of 4.** This will make the image somewhat less detailed but it will also look much better in certain cases!

Example:

CFG value of 7:

![CFG7](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/grid-0399.png)

CFG value of 4:

![CFG4](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/grid-0398.png)

- **Use "cosplay photo" and not just "photo" in your positive prompt as just "photo" is sometimes not strong enough to force through the photo style, while "cosplay photo" almost always is because the captions were trained on that!**

Example:

Just "photo"

![Just "photo"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/grid-0170.png)

"cosplay photo"

!["cosplay photo"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/grid-0169.png)

- The model was trained using captions such as "cosplay photo", "full-shot", "half-body", "closeup", "facial closeup", among others. **So in case you are trying to force a different style but the tlok artstyle keeps popping up, try changing "full-shot" to "full-body" for example!**

- **Alternatively, add "tlok artstyle" to the negative prompt if you find that the Legend of Korra style is influencing your prompt too strongly!**

Example:

"19th century oil painting"

!["19th century oil painting"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/grid-0173.png)

"19th century oil painting (negative prompt "tlok artstyle")"

!["19th century oil painting (negative prompt "tlok artstyle")"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/grid-0174.png)

- **Sometimes the photo generations of Korra will be too white, add "white skin" to the negative prompt in that case!**

## Example generations using this model!

empire state building tlok artstyle (using img2img)

!["empire state building tlok artstyle"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00416-1482461181-empire%20state%20building%20tlok%20artstyle.png)

woman with long blue hair wearing a traditional Japanese kimono during golden hour lighting tlok artstyle (resized with img2img + face inpainted)

!["woman with long blue hair wearing a traditional Japanese kimono during golden hour lighting tlok artstyle"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00418-1248489237-closeup%20woman%20with%20long%20blue%20hair%20wearing%20a%20traditional%20Japanese%20kimono%20during%20golden%20hour%20lighting%20tlok%20artstyle.png)

young woman with red hair wearing modern casual white tshirt and blue jeans standing in front of the Brandenburg Gate tlok artstyle (resized with img2img + face inpainted)

!["young woman with red hair wearing modern casual white tshirt and blue jeans standing in front of the Brandenburg Gate tlok artstyle"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00422-3495601497-closeup%20young%20woman%20with%20red%20hair%20wearing%20modern%20casual%20white%20tshirt%20and%20blue%20jeans%20standing%20in%20front%20of%20the%20Brandenburg%20Gate%20tl.png)

written letter tlok artstyle (resized using img2img)

!["written letter tlok artstyle"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00424-2560151794-written%20letter%20tlok%20artstyle.png)

Korra wearing business suit stada hairstyle tlok artstyle (resized with img2img + face inpainted)

!["facial closeup Korra wearing business suit stada hairstyle tlok artstyle"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00427-2247884288-facial%20closeup%20Korra%20wearing%20business%20suit%20stada%20hairstyle%20tlok%20artstyle.png)

full-shot Korra wearing astronaut outfit stada hairstyle tlok artstyle (resized using img2img)

!["full-shot Korra wearing astronaut outfit stada hairstyle tlok artstyle"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00429-2606052026-full-shot%20Korra%20wearing%20astronaut%20outfit%20stada%20hairstyle%20tlok%20artstyle.png)

Korra wearing defa outfit stada hairstyle as a cute pixar character (resized using img2img)

!["Korra wearing defa outfit stada hairstyle as a cute pixar character"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00430-2716015699-Korra%20wearing%20defa%20outfit%20stada%20hairstyle%20as%20a%20cute%20pixar%20character.png)

half-body Korra wearing Kimono taio hairstyle figurine (resized using img2img)

!["half-body Korra wearing Kimono taio hairstyle figurine"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00432-1669236977-half-body%20Korra%20wearing%20Kimono%20taio%20hairstyle%20figurine.png)

dog tlok artstyle

!["dog tlok artstyle"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/29467-1204970377-dog%20tlok%20artstyle.png)

mountain river valley tlok artstyle

!["mountain river valley tlok artstyle"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/29496-782504688-mountain%20river%20valley%20tlok%20artstyle.png)

Korra wearing bikini shoa hairstyle realistic detailed digital art by Greg Rutkowski

!["Korra wearing bikini shoa hairstyle realistic detailed digital art by Greg Rutkowski"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/29506-3823816358-Korra%20wearing%20bikini%20shoa%20hairstyle%20realistic%20detailed%20digital%20art%20by%20Greg%20Rutkowski.png)

Korra wearing rain jacket and jeans stada hairstyle cosplay photograph

!["Korra wearing rain jacket and jeans stada hairstyle cosplay photograph"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/29548-1019120701-Korra%20wearing%20rain%20jacket%20and%20jeans%20stada%20hairstyle%20cosplay%20photograph.png)

car on a road city street background tlok artstyle (resized using img2img)

!["car on a road city street background tlok artstyle"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00433-2844107839-car%20on%20a%20road%20city%20street%20background%20tlok%20artstyle.png)

Emma Watson (wearing defa outfit:1.3) cosplay photograph (resized using img2img)

!["Emma Watson (wearing defa outfit_1.3) cosplay photograph"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00435-172622402-Emma%20Watson%20(wearing%20defa%20outfit_1.3)%20cosplay%20photograph.png)

Zendaya standing in a forest wearing runa outfit tlok artstyle (resized using img2img + face inpainted)

!["Zendaya standing in a forest wearing runa outfit tlok artstyle"](https://huggingface.co/ai-characters/4elements-diffusion/resolve/main/00438-2275197862-facial%20closeup%20Zendaya%20standing%20in%20a%20forest%20wearing%20runa%20outfit%20tlok%20artstyle.png)

## Tokens to use to prompt the artstyle as well as Korra's different outfits

**You can give Korra's outfits and hairstyles also to other people thanks to the token method! You can also mix and match outfits and hairstyles however you want to**, though results may at times be worse than if you just pair the correct hairstyle to the correct outfit (aka as it was in the show)!

Legend of Korra artstyle:

- tlok artstyle

Korra's hairstyles:

- stada hairstyle (Default ponytail hair)

- oped hairstyle (Opened hair)

- loes hairstyle (Loose hair)

- shoa hairstyle (Season4 short hair)

- taio hairstyle (Traditional formal hair)

- foha hairstyle (Season4 formal hair)

- okch hairstyle (young child Korra hairstyle)

Korra's outfits:

"wearing X outfit"

**(the second words are the hairstyles, e.g. with "runa shoa" "runa" is the outfit and "shoa" the hairstyle; prompting the corresponding hairstyle alongside the outfit will give you better likeness, but you can also mix and match different hairstyles and outfits together as you see fit at the cost of likeness, though some outfits and hairstyles work better than others in this regard)**

- runa shoa (earth kingdom runaway)

- saco stada (default parka)

- aino stada (airnomad (makes her look like a child for some reason))

- fife stada (fireferrets probending uniform)

- eqli stada (equalist disguise)

- boez oped (season2 parka)

- defa stada (default outfit)

- alte stada (season2 outfit)

- asai shoa (Asami's jacket (doesn't work so well))

- taso stada (Tarrlok's taskforce)

- dava oped (dark avatar/season 3 finale)

- seri foha (series finale gown)

- fose shoa (season4 outfit)

- proe stada (probending training attire)

- tuwa shoa (turfwars finale gown from the comics (doesn't work so well))

- cidi stada (civilian disguise)

- epgo taio (traditional dress)

- bafo loes (bath/sleeping robe)

- ektu shoa (earth kingdom tunic/hoodie)

- pama loes (pajamas)

- exci stada (firebending exercise (doesn't work so well))

- as chie, wearing yowi (child korra, winter outfit from the comics)

- as chie, wearing suou (child kora, summer outfit)

## Current shortcomings of the model

- the model is infected due to no regularization. This means better likeness but also means that you are better off using the original vanilla SD model for txt2img photo generations and then send them to img2img and switch the model over to this one for style transfer!

- the model may struggle at times with more complex prompts

- location tagging is very rudimentary for now (exterior, day, arctic)

- Landscapes could look better

- No tagging of unique locations, e.g. Republic City

- Korra is the only trained character for now

- a few of the outfits don't work that well because of low amount of training images or low resolution images. Generally some outfits, people, things, styles and prompts will work better than others

- likeness was better for certain prompts in my older models

## Outlook into the future

- Ideally I will be able to expand upon this model in the future by adding all the other characters from the show and maybe even ATLA characters! However, right now I am uncertain if that is possible, as the model is already heavily trained.

- Generally I want to improve this models likeness and flexibility

- Training this model on the new base inpainting model

- I seek to produce more models in the future such as models for Ahsoka, Aloy, Owl House, Ghibli, Sadie Sink, She-Ra, various online artists... but that will take time (and money)

## How I created this model and the underlying dataset (+ dataset download link!)

At first I wanted to create only a small Korra model with only her default outfit. In the first days I was experimenting with the standard class and token Dreambooth method using JoePennas repo. For that I manually downloaded 900 screenshots from the show of Korra in her default outfit from fancaps.net. I then manually cropped and resized those images. As I ran into walls I stopped trying to create this model and restarted trying to create a general style model using native finetuning instead. This time however I used the 40€ paid version of "Bulk Image Downloader" to automatically download around 30000 screencaps of the show from fancaps.net. I then used AntiDupl.NET to delete around half of the images which were found out by the program to be a duplicate. I then used ChaiNNer and IrfanView to bulk crop and resize the rest of the dataset to 512x512. I also downloaded around 200 high-quality fanarts and cosplay photos depicting Korra in her various outfits and some non-show outfits and used Irfanview to automatically resize them to 512x512 without cropping by adding black borders to the image (those do not show up in the final model output, luckily).

I spent a lot of money on GPU renting for the native finetuning but results were worse than my Dreambooth experiments so I went back to Dreambooth and used a small fraction of the finetuning dataset to create a style model. I learned a lot this time around and improved my model results but still results were not to my liking.

That is when I found out about the caption method in JoePennas repo. So I went ahead and spent an entire weekend, 12 hours each day, manually captioning around 1000 images. I used around 300 images from the former finetuning dataset for the style, 600 from the former 900 manually cropped and resized screencaps of Korra in her default outfit, then around 200 fanarts and cosplay photos and some additional screencaps and images of Korra in all her other outfits, to create my final dataset.

I used "Bulk File Rename" for Windows 10 to bulk rename files aka add captions.

**[The captioned dataset can be found here!](https://huggingface.co/datasets/ai-characters/4elements-diffusion-captioned-dataset)**

**[The 14000 show screencaps can be found for download here!](https://www.dropbox.com/s/406u0tv9xuttgku/14284%20images%2C%20512x512%2C%20automatically%20cropped%2C%20downscaled%20from%201080x1080.7z?dl=1)**

I encourage everyone to try and do it better than me and create your own Legend of Korra model!

Ultimately I spent the past two weeks experimenting with various different captions and training settings to reach my final model.

My final model uses these training settings:

- Repo: JoePenna's with captions (no class or regularization and only a fake token that will not be used during training)

- Learning rate: 3e-6 (for 80 repeats) and 2e-6 (for 35 repeats)

- Repeats/Steps: See above (1 repeat = one run through the entire dataset, so 1142 steps)

I had to use such high learning rates because due to the nature of the size of the dataset and captions it required it to attain the likeness I wanted for both the style and all of Korra's outfits.

There is much more to be said here regarding my workflow, experimentation, and the like, but I don't want to make this longer than necessary and this *is* already very long.

## Alternative Download Links

[Alternative download link for the model](https://www.dropbox.com/s/ayyk6c039gux7zs/4elements-diffusion.ckpt?dl=1)

[Alternative download link for the captioned dataset](https://www.dropbox.com/s/iobslrmyvdoi8oy/1142%20images%2C%20manually%20captioned%2C%20manual%20and%20automatic%20cropping%2C%20downscaled%20from%201024x1024.7z?dl=1)

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage. The CreativeML OpenRAIL License specifies:

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully) [Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

---
language:
  - en
license: creativeml-openrail-m
tags:
  - stable-diffusion
  - stable-diffusion-diffusers
  - text-to-image
  - diffusers
inference: true
---
## Example: 
”Negative prompt: (worst quality, low quality:1.4)” is really useful in anywhere

I think all models are great with correct Hires.fix
## Ekmix-Pastel
pastel but lines(with Hires.fix) (Merging the loras into the model.)
~~~
python networks\merge_lora.py --sd_model .\models\model.safetensors --save_to .\lora\2.safetensors --models  .\lora\MagicLORA.pt  .\lora\Jordan_3.safetensors  .\lora\sttabi_v1.4-04.safetensors  .\lora\xlimo768.pt  .\lora\dpep2.pt  --ratios 0.3 1 0.5 0.6 0.35
~~~
![](https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/main/examples/xy_grid-0061-191289848-.png)
~~~
masterpiece,best quality,best quality,Amazing,beautiful detailed eyes,1girl,finely detail,Depth offield,extremely detailed CG unity 8k wallpaper,masterpiece,upper body,(vtuber minato aqua),pink hair,blue streaked hair, palace,holy,white long split mop dress ,mature female,standing,medium_breasts,silver-tiara,smile,black high heels,very long hair, body towards aside,jewelry,hair blue flower,grey eyes,close-up,
Negative prompt: (worst quality, low quality:1.3)
Steps: 30, Sampler: Euler a, CFG scale: 6, Seed: 191289851, Size: 512x768, Model hash: 0526445f65, Denoising strength: 0.5, Eta: 0.5, Clip skip: 2, ENSD: 31337, Hires resize: 856x1280, Hires steps: 30, Hires upscaler: Latent
~~~
pastel but lines(without hires fix) (better!)
![](https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/main/examples/xy_grid-0078-2035526620.png)
~~~
{masterpiece},{best quality},{1girl,{{loli},black hair,blue eyes,very long hair,hair flower,hanfu,happy}},Amazing,beautiful detailed eyes,finely detail,Depth of field,extremely detailed CG,original,outdoors,beautiful detailed hand,beautiful detailed fingers,{{soaked},{wet through}},{body under water},standing,{beautiful detailed water,beautiful detailed sky,fluttered detailed splashs}
Negative prompt: (worst quality, low quality:1.3)
Steps: 30, Sampler: DPM++ 2M Karras, CFG scale: 6, Seed: 2035526620, Size: 768x512, Model hash: ca485b96f8, Eta: 0.5, Clip skip: 2, ENSD: 31337
~~~
## Ekmix-gen4
balance between anime and reality(Merging by block weighted merge.)
![0](https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/main/examples/xy_grid-0273-620659051-masterpiece%2Cbest%20quality%2Cbest%20quality%2CAmazing%2Cbeautiful%20detailed%20eyes%2C1girl%2Cfinely%20detail%2CDepth%20offield%2Cextremely%20detailed%20CG%20un.png)
~~~
masterpiece,best quality,best quality,Amazing,beautiful detailed eyes,1girl,finely detail,Depth offield,extremely detailed CG unity 8k wallpaper,masterpiece,upper body,(vtuber minato aqua),pink hair,blue streaked hair, palace,holy,white long split mop dress ,mature female,standing,medium_breasts,silver-tiara,smile,black high heels,very long hair, body towards aside,jewelry,hair blue flower,grey eyes,close-up,
~~~
![1](https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/main/examples/xy_grid-0274-439385113-%7Bmasterpiece%7D%2C%7Bbest%20quality%7D%2C%7B1girl%2C%7B%7Bloli%7D%2Cblack%20hair%2Cblue%20eyes%2Cvery%20long%20hair%2Chair%20flower%2Chanfu%2Chappy%7D%7D%2CAmazing%2Cbeautiful%20deta.png)
~~~
{masterpiece},{best quality},{1girl,{{loli},black hair,blue eyes,very long hair,hair flower,hanfu,happy}},Amazing,beautiful detailed eyes,finely detail,Depth of field,extremely detailed CG,original,outdoors,beautiful detailed hand,beautiful detailed fingers,{{soaked},{wet through}},{body under water},standing,{beautiful detailed water,beautiful detailed sky,fluttered detailed splashs},by Paul Hedley,
~~~
# Great hypernetworks
 style1 and 2 are my favourite.
 3,4 may need retrain.
 ![0](https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/main/examples/xy_grid-0003-3253762592-%7Bmasterpiece%7D%2C%7Bbest%20quality%7D%2C%7B1girl%2C%7B%7Bloli%7D%2Cblack%20hair%2Cblue%20eyes%2Cvery%20long%20hair%2Chair%20flower%2Chanfu%2Chappy%7D%7D%2CAmazing%2Cbeautiful%20deta.png)




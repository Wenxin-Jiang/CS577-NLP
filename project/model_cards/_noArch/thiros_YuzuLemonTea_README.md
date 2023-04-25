---
license: cc0-1.0
tags:
- stable-diffusion
- text-to-image
---
# YuzuLemonTea Mix models ☕

List of my experimental merge models

- [Recommended Settings](#recommended-setteings)
- [YuzuLemonMilk](#yuzulemonmilk)
- [YuzuLemonChaiLatte](#yuzulemonchailatte)
- [YuzuGinger](#yuzuginger)

# important notice(Jan 15/23)

According to bbc-mc's note, there is a possibility of bug that some token(prompt) can be ignored, when merge with "add difference" option.
Milk and ChaiLatte models are now replaced with bug-fix ver.

https://note.com/bbcmc/n/n12c05bf109cc

# Recommended Setteings
VAE: "kl-f8-anime2" and "vae-ft-mse-840000-ema-pruned" are suitable

Steps: 20-30, Sampler: DPM++ SDE Karras or DPM++ 2M Karras, CFG scale: 8, Clip skip: 2, ENSD: 31377, Hires upscale: 2, Hires upscaler: Latent (bicubic antialiased),Denoising strength: 0.54~0.7

Negataive Prompt: (worst quality:2), (low quality:2),inaccurate limb,lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name
- (worst quality), (low quality) are adjustable between 1.4~2.0
- If you don't want 3DCG-ish paint, you can add (3d:0.8)~1.0 in Negative Prompt

# Sample prompt
4girls,(a 3d reader of:0.8) (teenage loli children:1.2), (wearing intricate casual camisole, cute hair ornament,crop jacket,hot pants, tighhigh:1.1),
shiny brown skin,
looking at viewer, (alluring smug:1.2),
dynamic angle,
(onomichi street:1.2),fisheye
<img src="https://i.imgur.com/2JiZwFU.jpg"  width="" height="1000">

# YuzuLemonMilk
Block merged model of Anything v3 and some real models.
Rather photo realistic.
Works fine with positive (realistic) and (photo realistic).
<img src="https://i.imgur.com/qYK8DKn.jpg"  width="" height="1000">


# YuzuLemonChaiLatte

Combination of a weight merge of ACertainModel and Anything-V3.0, and a block merge of several  realistic models.
Rather anime-ish style with realistic background.
- v3.5
<img src="https://i.imgur.com/WLKr3pj.jpg"  width="" height="1000">
- v9.5
<img src="https://i.imgur.com/Ufh3JK2.jpg"  width="" height="1000">

# YuzuGinger

Add more anime models to YuzuLemonChaiLatte. Can be very anime looks.
- v1
<img src="https://i.imgur.com/4vc4HSL.jpg"  width="" height="1000">
- v4
<img src="https://i.imgur.com/M6q6hYp.jpg"  width="" height="1000">
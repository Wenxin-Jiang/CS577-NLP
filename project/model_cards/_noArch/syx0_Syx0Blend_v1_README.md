---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: creativeml-openrail-m
inference: true

---

Intro
===

Been using this mix for a week. I'm a noobie.
</br></br></br>

### Recommends:
---


<b>WxH</b>: Multiples of 128 (i.e 512x512)

<b>VAE</b>: vae-ft-mse-840000-ema-pruned.ckpt

<b>Hypernetwork</b>: anything-v3.0.vae.pt (optional)

<b>HiRes Fix</b>:  Recommended 
</br></br></br>

### Suggestions:
---

<b>anime results</b>:

>sketch, watercolor, illustration

<b>realistic results</b>:

>Realistic, role-playing, face, portrait, painting of a beautiful rpg champion

<b>negative prompts</b>:

(that yields consistent results)

>(disfigured), (bad art), (deformed), (poorly drawn), (extra limbs), (close up), strange colors, blurry, boring, signature, letters, watermark, out of frame , worst quality , text , blurred , monstrous , hideous , ugly , duplicate , cropped , mutilated , horrifying

</br>

### Workflow
---

| Step | Interpolation Method | Primary Model | Secondary model | Tertiary Model | Merge Name |
|------|----------------------|---------------|-----------------|----------------|------------|
| 1    | Weighted Sum @ 0.4  | RPG   | AnythingV3.0 | n/a           | AnyRPG-mix |
| 2    | Add Difference @ 1    | AnyRPG-mix   | Baka-Diffusion V1 | berrymix-v3 | BakaBerry-d1 |
| 3    | Weighted Sum @ 0.25  | BakaBerry-d1 | r34_e4        | n/a           | Syx0 Blend V3 |



Socials:</br>
https://github.com/axsddlr

https://www.reddit.com/user/ayyser
</br></br></br>




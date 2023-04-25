---
license: creativeml-openrail-m
language:
- en
tags:
- stable-diffusion
- text-to-image
---

# Any(thing) Mix(es)
Mixed weeb models :)

# Models
## anything-berry-30.ckpt
[Re-uploaded from](https://huggingface.co/misobarisic/anything-berrymix)
Step | Interpolation Method | Primary Model | Secondary model | Tertiary Model | Merge Name
 --- | ---                  | ---           | ---             | ---            | ---
1    | Weighted Sum @ 0.30  | Anything V3   | Berry Mix       | n/a            | **anything-berry-30**

## anything-f222-15.ckpt
[Recipe Source](https://www.reddit.com/r/WaifuDiffusion/comments/zdbs3r/comment/iz0nr48/?utm_source=reddit&utm_medium=web2x&context=3)
Step | Interpolation Method | Primary Model | Secondary model | Tertiary Model | Merge Name
 --- | ---                  | ---           | ---             | ---            | ---
1    | Weighted Sum @ 0.15  | Anything V3   | Zeipher F222 | n/a | **anything-f222-15**
 
## anything-f222-15-elysiumv2-10.ckpt
[Recipe Source](https://www.reddit.com/r/WaifuDiffusion/comments/zg1d8x/comment/izei93c/?utm_source=reddit&utm_medium=web2x&context=3)
Step | Interpolation Method | Primary Model | Secondary model | Tertiary Model | Merge Name
 --- | ---                  | ---           | ---             | ---            | ---
1    | Weighted Sum @ 0.10  | anything-f222-15   | Elysium Anime v2 | n/a | **anything-f222-15-elysiumv2-10**

## berrymix-v3.ckpt
[Recipe Source](https://rentry.org/hdgrecipes#berrymix-v3-535d98a3)
Step | Interpolation Method | Primary Model | Secondary model | Tertiary Model | Merge Name
 --- | ---                  | ---           | ---             | ---            | ---
1 	 | Weighted Sum @ 0.05 	| AnythingV3.0 	| Stable Diffusion 1.5 	| n/a 	| Anything Fix
2 	 | Add Difference @ 1 	| Anything fix 	| Zeipher F222 	| Stable Diffusion 1.5 	| berrymix3 lite
3 	 | Weighted Sum @ 0.25 	| berrymix3 lite 	|r34_e4 	| n/a 	| **berrymix V3**

## blossom-extract.safetensors
[Recipe Source](https://www.reddit.com/r/StableDiffusion/comments/zk8y50/comment/izyhn8w/?utm_source=reddit&utm_medium=web2x&context=3)
Step | Interpolation Method | Primary Model | Secondary model | Tertiary Model | Merge Name
 --- | ---                  | ---           | ---             | ---            | ---
 1   | Add Difference @ 1   | Anything V3   | Zeipher F222    | Stable Diffusion 1.4 | **blossom-extract**

## hentai-elysium-50.safetensors
[Recipe Source](https://www.reddit.com/r/WaifuDiffusion/comments/zn6wdb/comment/j0fabe6/?utm_source=reddit&utm_medium=web2x&context=3)
Step | Interpolation Method | Primary Model | Secondary model | Tertiary Model | Merge Name
 --- | ---                  | ---           | ---             | ---            | ---
1    | Weighted Sum @ 0.5   | Hentai Diffusion 17   | Elysium Anime v2    | n/a | **hentai-elysium-50**

## nutmeg-mix.ckpt
[Recipe Source](https://rentry.org/hdgrecipes#nutmegmix-aa3e502b)
Step | Interpolation Method | Primary Model | Secondary model | Tertiary Model | Merge Name
 --- | ---                  | ---           | ---             | ---            | ---
1 	 | Weighted Sum @ 0.05 	| NovelAI 	| Stable Diffusion 1.5 	| n/a 	| nutmegmix-part1
2 	 | Weighted Sum @ 0.05 	| nutmegmix-part1 	| Zeipher F222 	| n/a 	| nutmegmix-part2
3 	 | Weighted Sum @ 0.05 	| nutmegmix-part2 	| r34_e4 	| n/a 	| nutmegmix-part3
4 	 | Weighted Sum @ 0.05 	| nutmegmix-part3 	| SmirkingFace 	| n/a 	| nutmegmix-part4
5 	 | Weighted Sum @ 0.3 	| AnythingV3.0 	| nutmegmix-part4 	| n/a 	| **nutmeg-mix**

## raspberry-mix.ckpt
[Recipe Source](https://rentry.org/hdgrecipes#raspberry-mix-4d202242)
Step | Interpolation Method | Primary Model | Secondary model | Tertiary Model | Merge Name
 --- | ---                  | ---           | ---             | ---            | ---
1 	 | Weighted Sum @ 0.25 	| AnythingV3.0 	| Stable Diffusion 1.5 	| n/a 	| AnyV3-SD1.5
2 	 | Add Difference @ 1 	| AnyV3-SD1.5 	| Zeipher F222 	| Stable Diffusion 1.4 	| raspberry-lite
3 	 | Weighted Sum @ 0.15 	| raspberry-lite 	| r34_e4 	| n/a 	| **raspberry mix**

## strawberry-mix.ckpt
[Recipe Source](https://rentry.org/hdgrecipes#strawberry-mix-e043dfc5)
Step | Interpolation Method | Primary Model | Secondary model | Tertiary Model | Merge Name
 --- | ---                  | ---           | ---             | ---            | ---
1 	 | Weighted Sum @ 0.25 	| AnythingV3.0 	| Stable Diffusion 1.4 	| n/a 	| AnyV3-SD1.4
2 	 | Add Difference @ 1 	| AnyV3-SD1.4 	| Zeipher F111 	| Stable Diffusion 1.4 	| strawberry-lite
3 	 | Weighted Sum @ 0.15 	| strawberry-lite 	| r34_e4 	| n/a 	| **strawberry mix**
---
license: creativeml-openrail-m
tags:
- text-to-image
- stable-diffusion
---
### This is a mixed model made by IWillRemember, obtained from Discord. All credits goes to them who provided the models, thank you.
Quote from IWillRemember:
"...it's an amazingly accurate mix and it does almost everything really well if the right tags are used, the art style is really soft, photorealism, classicism, ghotic stuff and cyberpunk themed stuff are really... really good with it, personally i love it
... This is the full recipe:

| Model: A     | Model: B               | Interpolation Method | Merge Name |
| ------------ | ---------------------- | -------------------- | ---------- |
| Anything V3  | EasterE9               | Weighted Sum @ 0.5   | temp01     |
| temp01       | animefull-final-pruned | Weighted Sum @ 0.25  | temp02     |
| temp02       | F222                   | Weighted Sum @ 0.25  | temp03     |
| temp03       | WD 1.3                 | Weighted Sum @ 0.05  | temp04     |
| temp04       | SamdoesArt             | Weighted Sum @ 0.05  | RememberMix|

Example image:
![](https://huggingface.co/NiteStormz/Remembermix/resolve/main/example.png "")
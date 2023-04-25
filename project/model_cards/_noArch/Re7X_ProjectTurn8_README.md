---
license: other
tags:
- stable-diffusion
- text-to-image
---

# Currently being edited. Model files are already available.

# 現在編集中です。モデルファイルは既に公開してあります。

---

# ProjectTurn8

<img src="https://i.imgur.com/WiS93wx.png"  width="1000" height="">
●What is this?

We are submitting a variety of merge models that are well done.

●How to use

Put the downloaded model file into stable-diffusion-webui\models\Stable-diffusion

It is recommended to use bad_prompt_version2 of TextualInversion, but the painting style may change significantly.

●Comparison of models in the public domain.

<img src="https://i.imgur.com/j1lmHAQ.jpg"  width="1000" height="">

```jsx
straw hat, (white sundress:1.2), 1 girl,loli, standing, blond hair, yellow eyes, medium breasts, outdoor, beach, cowboy shot, from outside, looking at viewer, perfect anatomy, sunlight
Negative prompt: (worst quality:1.4), (low quality:1.4),(monochrome:1.1),(bad_prompt:0.5),(swimsuit:1.2)
Steps: 36, Sampler: DPM++ SDE Karras, CFG scale: 6.5, Seed: 123, Size: 512x768, Model hash: 40ab3495, Eta: 0.67, Clip skip: 2, ENSD: 31337
```


----

## ProjectTurn8-Jupiter

●What is this?

This model is a merge of Stella and basil_mix using the extension sdweb-merge-block-weighted-gui.
Compared to Earth, the skin and clothing textures are more realistic and improved.

However, if you do not use Hires. fix, the look will be lost.

●Recommended setting

CFG Scale : 9±3

Clip skip : 2

Hires. fix : Upscale by 2

●Samples

<img src="https://i.imgur.com/zIn6hkC.png"  width="400" height="">


----

## ProjectTurn8-Stella
<img src="https://i.imgur.com/qUTbReP.png"  width="1000" height="">
●What is this?

This is a merged model based on anything+everything ver2.
It is mainly suited for writing 2D cute girls.

Basically, other models are created based on this model.

●Recommended setting

CFG Scale : 8±3

Clip skip : 2

----
## ProjectTurn8-Earth
<img src="https://i.imgur.com/efIyvTu.png"  width="1000" height="">
●What is this?

This model was created using the extension sdweb-merge-block-weighted-gui.
It is possible to create more realistic illustrations compared to Stella.

●Recommended setting

CFG Scale : 6±1

Sampling method : DPM++ SDE Karras

----
## ProjectTurn8-Luna
<img src="https://i.imgur.com/pnVSdat.png"  width="1000" height="">
●What is this?

This model is a cross between Earth and Stella.

●Recommended setting

CFG Scale : 6±1

Sampling method : DPM++ SDE Karras

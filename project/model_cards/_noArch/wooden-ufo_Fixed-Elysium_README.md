---
license: openrail
language: 
  - ja
tags:
  - text-to-image
---
# このモデルについて
　問題が[報告](https://twitter.com/alice_diffusion/status/1608283908935929856)されている [hesw23168/SD-Elysium-Model](https://huggingface.co/hesw23168/SD-Elysium-Model) の Elysium_Anime_V3 を Elysium_V1 を使って修正したものです。Elysium_Anime_V3f.ckpt が修正したものです。ですがこの問題とされている Elysium_Anime_V3.safetensors の方が使い勝手がいいこともあるため、そのオリジナルのファイルも置いておきます。  
# 修正前後の比較
```
Prompt: Sleepy Hatune Miku,  
Negative prompt: , , , , , ((Evil)), ((Nightmare)), ((Creepy)), ((Unpleasant)), ((Awkward)), ((Nauseating)), ((Useless)),  
Steps: 50, Sampler: Euler, CFG scale: 7, Seed: 2072204094, Size: 512x512, Clip skip: 2
```
|Elysium_Anime_V3|Elysium_Anime_V3f|
|:---:|:---:|
|![01341-2072204094-Sleepy Hatune Miku,.png](https://s3.amazonaws.com/moonup/production/uploads/1672311261072-63a828d72e05ca32e34a346f.png)|![01342-2072204094-Sleepy Hatune Miku,.png](https://s3.amazonaws.com/moonup/production/uploads/1672311261063-63a828d72e05ca32e34a346f.png)|
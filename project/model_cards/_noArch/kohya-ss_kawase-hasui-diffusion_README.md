---
license: creativeml-openrail-m
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
---

Kawase Hasui Diffusion is trained on pantings by [KAWASE Hasui（川瀬巴水）](https://en.wikipedia.org/wiki/Hasui_Kawase).
The model has been trained on Stable Diffusion v2-1 with DreamBooth method with a learning rate of 1.0e-6 for 2,600 steps with the batch size of 8 (8 train or reg images) on 169 training images and 664 regularization images.

This model is based on SD2.1 768/v, so if you use this model in the poplular Web UI, please rename 'v2-inference-v.yaml' to 'kawase-hasui-epoch-000003.yaml' (or ~_fp16.yaml) and place it to the same folder to .safetensors.

The training prompt is "picture by lvl". 

## Examples

![Japan tourism poster](./sample1.png)
```
picture by lvl, japan tourism poster
seed  : 968191097, sampler: k_euler_a, steps : 160, CFG scale : 5.5
```

![Cyberpunk Akihabara](./sample2.png)
```
picture by lvl, cyberpunk akihabara
seed  : 1418478714, sampler: k_euler_a, steps : 160, CFG scale : 5.5
```

![Ruined castle](./sample3.png)
```
picture by lvl, ruined castle, fantasy, dawn
seed  : 897433524, sampler: k_euler_a, steps : 160, CFG scale : 5.5
```

![Party of adventurers](./sample4.png)
```
picture by lvl, fantasy, party of adventurers, ready to fight, in front of ruined temple
seed  : 1814292911, sampler: k_euler_a, steps : 160, CFG scale : 5.5
```

## License

CreativeML Open RAIL-M 

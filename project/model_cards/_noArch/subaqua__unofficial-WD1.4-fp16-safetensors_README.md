---
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
license: creativeml-openrail-m
---

# See https://huggingface.co/hakurei/waifu-diffusion-v1-4

## This is WD1.4 with .safetensors and fp16, which is unofficial fork

- [Waifu Diffusion 1.4 Anime Epoch 2 Safetensors](https://huggingface.co/subaqua/_unofficial-WD1.4-fp16-safetensors/resolve/main/wd-1-4-anime_e2-fp16.safetensors): A faster-loading and lighter version of WD1.4 Anime E2
- [Waifu Diffusion 1.4 Anime Safetensors Inference Config](https://huggingface.co/subaqua/_unofficial-WD1.4-fp16-safetensors/resolve/main/wd-1-4-anime_e2-fp16.yaml): A file included to allow for inference with Automatic's WebUI and with the original Stable Diffusion codebase.

This configuration file is modified for "Waifu Diffusion 1.4 Anime Inference Config" with the following changes:
```
model:
  params:
    unet_config:
      params:
        use_checkpoint: False
```

## Grate respect to the WD1.4 development team!

## Inherited License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)
---
language: 
  - en
thumbnail: "https://s3.amazonaws.com/moonup/production/uploads/1663756797814-62bd5f951e22ec84279820e8.png"
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
datasets:
- lambdalabs/pokemon-blip-captions
---

__Stable Diffusion fine tuned on Pokémon by [Lambda Labs](https://lambdalabs.com/).__

Put in a text prompt and generate your own Pokémon character, no "prompt engineering" required!

If you want to find out how to train your own Stable Diffusion variants, see this [example](https://github.com/LambdaLabsML/examples/tree/main/stable-diffusion-finetuning) from Lambda Labs.


![image.png](https://s3.amazonaws.com/moonup/production/uploads/1663756797814-62bd5f951e22ec84279820e8.png)

> Girl with a pearl earring, Cute Obama creature, Donald Trump, Boris Johnson, Totoro, Hello Kitty

## Usage

Make sure you have setup the Stable Diffusion repo and downloaded `ema-only-epoch=000142.ckpt`

```bash
 python scripts/txt2img.py \
    --prompt 'robotic cat with wings' \
    --outdir 'outputs/generated_pokemon' \
    --H 512 --W 512 \
    --n_samples 4 \
    --config 'configs/stable-diffusion/pokemon.yaml' \
    --ckpt ema-only-epoch=000142.ckpt
```

You can also use the normal stable diffusion inference config.

## Model description

Trained on [BLIP captioned Pokémon images](https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions) using 2xA6000 GPUs on [Lambda GPU Cloud](https://lambdalabs.com/service/gpu-cloud) for around 15,000 step (about 6 hours, at a cost of about $10).

## Links

- [Lambda Diffusers](https://github.com/LambdaLabsML/lambda-diffusers)
- [Captioned Pokémon dataset](https://huggingface.co/datasets/lambdalabs/pokemon-blip-captions)
- [Model weights in Diffusers format](https://huggingface.co/lambdalabs/sd-pokemon-diffusers)
- [Original model weights](https://huggingface.co/justinpinkney/pokemon-stable-diffusion)
- [Training code](https://github.com/justinpinkney/stable-diffusion)

Trained by [Justin Pinkney](justinpinkney.com) ([@Buntworthy](https://twitter.com/Buntworthy)) at [Lambda Labs](https://lambdalabs.com/).
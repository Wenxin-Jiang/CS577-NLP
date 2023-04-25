---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
inference: false
---
# Stable Diffusion

Stable Diffusion is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input.
This model card gives an overview of all available model checkpoints. For more in-detail model cards, please have a look at the model repositories listed under [Model Access](#model-access).

## Stable Diffusion Version 1

For the first version 4 model checkpoints are released.
*Higher* versions have been trained for longer and are thus usually better in terms of image generation quality then *lower* versions. More specifically: 

- **stable-diffusion-v1-1**: The checkpoint is randomly initialized and has been trained on 237,000 steps at resolution `256x256` on [laion2B-en](https://huggingface.co/datasets/laion/laion2B-en).
  194,000 steps at resolution `512x512` on [laion-high-resolution](https://huggingface.co/datasets/laion/laion-high-resolution) (170M examples from LAION-5B with resolution `>= 1024x1024`).
- **stable-diffusion-v1-2**: The checkpoint resumed training from `stable-diffusion-v1-1`.
  515,000 steps at resolution `512x512` on "laion-improved-aesthetics" (a subset of laion2B-en,
filtered to images with an original size `>= 512x512`, estimated aesthetics score `> 5.0`, and an estimated watermark probability `< 0.5`. The watermark estimate is from the LAION-5B metadata, the aesthetics score is estimated using an [improved aesthetics estimator](https://github.com/christophschuhmann/improved-aesthetic-predictor)).
- **stable-diffusion-v1-3**: The checkpoint resumed training from `stable-diffusion-v1-2`. 195,000 steps at resolution `512x512` on "laion-improved-aesthetics" and 10 % dropping of the text-conditioning to improve [classifier-free guidance sampling](https://arxiv.org/abs/2207.12598)
- **stable-diffusion-v1-4**: The checkpoint resumed training from `stable-diffusion-v1-2`. 195,000 steps at resolution `512x512` on "laion-improved-aesthetics" and 10 % dropping of the text-conditioning to improve [classifier-free guidance sampling](https://arxiv.org/abs/2207.12598).
- [**`stable-diffusion-v1-4`**](https://huggingface.co/CompVis/stable-diffusion-v1-4) Resumed from `stable-diffusion-v1-2`.225,000 steps at resolution `512x512` on "laion-aesthetics v2 5+" and 10 % dropping of the text-conditioning to improve [classifier-free guidance sampling](https://arxiv.org/abs/2207.12598).

### Model Access

Each checkpoint can be used both with Hugging Face's [ 🧨 Diffusers library](https://github.com/huggingface/diffusers) or the original [Stable Diffusion GitHub repository](https://github.com/CompVis/stable-diffusion). Note that you have to *"click-request"* them on each respective model repository.

| **[🤗's 🧨 Diffusers library](https://github.com/huggingface/diffusers)**     | **[Stable Diffusion GitHub repository](https://github.com/CompVis/stable-diffusion)** |
| ----------- | ----------- |
| [`stable-diffusion-v1-1`](https://huggingface.co/CompVis/stable-diffusion-v1-1)      | [`stable-diffusion-v-1-1-original`](https://huggingface.co/CompVis/stable-diffusion-v-1-1-original)       |
| [`stable-diffusion-v1-2`](https://huggingface.co/CompVis/stable-diffusion-v1-2)   | [`stable-diffusion-v-1-2-original`](https://huggingface.co/CompVis/stable-diffusion-v-1-2-original)        |
| [`stable-diffusion-v1-3`](https://huggingface.co/CompVis/stable-diffusion-v1-3)   | [`stable-diffusion-v-1-3-original`](https://huggingface.co/CompVis/stable-diffusion-v-1-3-original)        |
| [`stable-diffusion-v1-4`](https://huggingface.co/CompVis/stable-diffusion-v1-4)   | [`stable-diffusion-v-1-4-original`](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original)        |

### Demo

To quickly try out the model, you can try out the [Stable Diffusion Space](https://huggingface.co/spaces/stabilityai/stable-diffusion).

### License

[The CreativeML OpenRAIL M license](https://huggingface.co/spaces/CompVis/stable-diffusion-license) is an [Open RAIL M license](https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses), adapted from the work that [BigScience](https://bigscience.huggingface.co/) and [the RAIL Initiative](https://www.licenses.ai/) are jointly carrying in the area of responsible AI licensing. See also [the article about the BLOOM Open RAIL license](https://bigscience.huggingface.co/blog/the-bigscience-rail-license) on which our license is based.

## Citation

```bibtex
    @InProceedings{Rombach_2022_CVPR,
        author    = {Rombach, Robin and Blattmann, Andreas and Lorenz, Dominik and Esser, Patrick and Ommer, Bj\"orn},
        title     = {High-Resolution Image Synthesis With Latent Diffusion Models},
        booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
        month     = {June},
        year      = {2022},
        pages     = {10684-10695}
    }
```

*This model card was written by: Robin Rombach and Patrick Esser and is based on the [DALL-E Mini model card](https://huggingface.co/dalle-mini/dalle-mini).*

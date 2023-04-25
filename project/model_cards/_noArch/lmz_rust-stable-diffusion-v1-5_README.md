---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- rust
inference: true
extra_gated_prompt: |-
  This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
  The CreativeML OpenRAIL License specifies:

  1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content
  2. CompVis claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
  3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
  Please read the full license carefully here: https://huggingface.co/spaces/CompVis/stable-diffusion-license

extra_gated_heading: Please read the LICENSE to access this model
---

This repository hosts weights for a Rust based version of Stable Diffusion.
These weights have been directly adapted from the
[runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
weights, they can be used with the
[diffusers-rs](https://github.com/LaurentMazare/diffusers-rs) crate.

To do so, checkout the diffusers-rs repo, copy the weights in the `data/`
directory and run the following command:

```bash
cargo run --example stable-diffusion --features clap -- --prompt "A rusty robot holding a fire torch."
```

This is for the image-to-text pipeline, example using the image-to-image and
inpainting pipelines can be found in the
[crate readme](https://github.com/LaurentMazare/diffusers-rs/blob/main/README.md).


## License
The license is unchanged, see the
[original version](https://huggingface.co/spaces/CompVis/stable-diffusion-license).
In line with paragraph 4, the original copyright is preserved:
Copyright (c) 2022 Robin Rombach and Patrick Esser and contributors

The model details section below is copied from the runwayml version, refer to
the [original repo](https://huggingface.co/runwayml/stable-diffusion-v1-5) for
use restrictions, limitations, bias discussion etc.

## Model Details
- **Developed by:** Robin Rombach, Patrick Esser
- **Model type:** Diffusion-based text-to-image generation model
- **Language(s):** English
- **License:** [The CreativeML OpenRAIL M license](https://huggingface.co/spaces/CompVis/stable-diffusion-license) is an [Open RAIL M license](https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses), adapted from the work that [BigScience](https://bigscience.huggingface.co/) and [the RAIL Initiative](https://www.licenses.ai/) are jointly carrying in the area of responsible AI licensing. See also [the article about the BLOOM Open RAIL license](https://bigscience.huggingface.co/blog/the-bigscience-rail-license) on which our license is based.
- **Model Description:** This is a model that can be used to generate and modify images based on text prompts. It is a [Latent Diffusion Model](https://arxiv.org/abs/2112.10752) that uses a fixed, pretrained text encoder ([CLIP ViT-L/14](https://arxiv.org/abs/2103.00020)) as suggested in the [Imagen paper](https://arxiv.org/abs/2205.11487).
- **Resources for more information:** [GitHub Repository](https://github.com/CompVis/stable-diffusion), [Paper](https://arxiv.org/abs/2112.10752).
- **Cite as:**

      @InProceedings{Rombach_2022_CVPR,
          author    = {Rombach, Robin and Blattmann, Andreas and Lorenz, Dominik and Esser, Patrick and Ommer, Bj\"orn},
          title     = {High-Resolution Image Synthesis With Latent Diffusion Models},
          booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
          month     = {June},
          year      = {2022},
          pages     = {10684-10695}
      }

## Weight Extraction

The weights have been converted by downloading them from the runwayml/stable-diffusion-v1.5 repo,
and then running the following commands in the
[diffusers-rs repo](https://github.com/LaurentMazare/diffusers-rs).

After downloading the files, use Python to convert them to `npz` files.

```python
import numpy as np
import torch
model = torch.load("./vae.bin")
np.savez("./vae.npz", **{k: v.numpy() for k, v in model.items()})
model = torch.load("./unet.bin")
np.savez("./unet.npz", **{k: v.numpy() for k, v in model.items()})
```

Convert these `.npz` files to `.ot` files via `tensor-tools`.

```bash
cargo run --release --example tensor-tools cp ./data/vae.npz ./data/vae.ot
cargo run --release --example tensor-tools cp ./data/unet.npz ./data/unet.ot
```

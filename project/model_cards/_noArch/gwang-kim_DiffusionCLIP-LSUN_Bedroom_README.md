---
library_name: pytorch
tags:
- diffusion
- image-to-image
---

# DiffusionCLIP: Text-Guided Diffusion Models for Robust Image Manipulation - Bedrooms

Creators: Gwanghyun Kim, Taesung Kwon, Jong Chul Ye
Paper: https://arxiv.org/abs/2110.02711

<img src="https://github.com/submission10095/DiffusionCLIP_temp/raw/master/imgs/main1.png" alt="Excerpt from DiffusionCLIP paper showcasing comparison of DiffusionCLIP versus other methods for image reconstruction, manipulation, and style transfer." style="height: 300px;"/>

DiffusionCLIP is a diffusion model which is well suited for image manipulation thanks to its nearly perfect inversion capability, which is an important advantage over GAN-based models. This checkpoint was trained on the ["Bedrooms" category of the LSUN Dataset](https://www.yf.io/p/lsun).

This checkpoint is most appropriate for manipulation, reconstruction, and style transfer on images of indoor locations, such as bedrooms. The weights should be loaded into the [DiffusionCLIP model](https://github.com/gwang-kim/DiffusionCLIP).

### Credits

- Code repository available at: https://github.com/gwang-kim/DiffusionCLIP

### Citation

```
@article{kim2021diffusionclip,
  title={Diffusionclip: Text-guided image manipulation using diffusion models},
  author={Kim, Gwanghyun and Ye, Jong Chul},
  journal={arXiv preprint arXiv:2110.02711},
  year={2021}
}
```

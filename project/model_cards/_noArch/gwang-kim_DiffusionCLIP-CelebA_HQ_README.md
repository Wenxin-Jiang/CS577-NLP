---
library_name: pytorch
tags:
- diffusion
- image-to-image
---

# DiffusionCLIP: Text-Guided Diffusion Models for Robust Image Manipulation - Faces

Creators: Gwanghyun Kim, Taesung Kwon, Jong Chul Ye
Paper: https://arxiv.org/abs/2110.02711

<img src="https://github.com/submission10095/DiffusionCLIP_temp/raw/master/imgs/main1.png" alt="Excerpt from DiffusionCLIP paper showcasing comparison of DiffusionCLIP versus other methods for image reconstruction, manipulation, and style transfer." style="height: 300px;"/>

DiffusionCLIP is a diffusion model which is well suited for image manipulation thanks to its nearly perfect inversion capability, which is an important advantage over GAN-based models. This checkpoint was trained on the [CelebA-HQ Dataset](https://arxiv.org/abs/1710.10196), available on the Hugging Face Hub: https://huggingface.co/datasets/huggan/CelebA-HQ.

This checkpoint is most appropriate for manipulation, reconstruction, and style transfer on images of human faces using the DiffusionCLIP model. To use ID loss for preserving Human face identity, you are required to download the [pretrained IR-SE50 model](https://drive.google.com/file/u/1/d/1KW7bjndL3QG3sxBbZxreGHigcCCpsDgn/view) from [TreB1eN](https://github.com/TreB1eN/InsightFace_Pytorch). Additional information is available on [the GitHub repository](https://github.com/gwang-kim/DiffusionCLIP).

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

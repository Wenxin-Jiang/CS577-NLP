---
license: mit
library_name: pytorch
tags:
- gan
- image-to-image
---

# AnimeBackgroundGAN-Miyazaki (CartoonGAN by Chen et. al.)

<img src="https://m.media-amazon.com/images/M/MV5BMTM4MTg2MjAzN15BMl5BanBnXkFtZTcwMTk1NzEyNw@@._V1_.jpg" alt="Howl's Moving Castle directed by Hayao Miyazaki" style="height: 300px;"/>

- [Hayao Miyazaki（宮崎駿）](https://en.wikipedia.org/wiki/Hayao_Miyazaki) pre-trained model from [CartoonGAN](http://openaccess.thecvf.com/content_cvpr_2018/CameraReady/2205.pdf) `[Chen et al., CVPR18]`.
- This model can transform real-life photos into Japanese-animation-like backgrounds, following the style of movies such as [Howl's Moving Castle](https://en.wikipedia.org/wiki/Howl%27s_Moving_Castle_(film)) with a relatively soft and painterly style.
- The implementation is in PyTorch (see [source code here](https://huggingface.co/spaces/akiyamasho/AnimeBackgroundGAN/blob/main/network/Transformer.py)).
- Check out the demo here:

[![Demo in Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/akiyamasho/AnimeBackgroundGAN)

# Other pre-trained model versions

The other versions were also trained from movies of the different Japanese animation directors.

##### Mamoru Hosoda（細田守）
- director of  [Wolf Children](https://en.wikipedia.org/wiki/Wolf_Children), with a distinct mild and cool background style
- [Director Profile](https://en.wikipedia.org/wiki/Mamoru_Hosoda)
- **Model Repository**: https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Hosoda

##### Satoshi Kon（今敏）
- director of [Paprika](https://en.wikipedia.org/wiki/Paprika_(2006_film)) with a distinct high contrast, reddish hue style
- [Director Profile](https://en.wikipedia.org/wiki/Satoshi_Kon)
- **Model Repository**: https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Kon

##### Makoto Shinkai （新海誠）
- director of [Kimi no Na wa](https://en.wikipedia.org/wiki/Kimi_no_Na_wa) with a photorealistic painting style
- [Director Profile](https://en.wikipedia.org/wiki/Makoto_Shinkai) 
- **Model Repository**: https://huggingface.co/akiyamasho/AnimeBackgroundGAN-Shinkai

### Credits

- Paper at [CartoonGAN: Generative Adversarial Networks for Photo Cartoonization](http://openaccess.thecvf.com/content_cvpr_2018/CameraReady/2205.pdf) `[Chen et al., CVPR18]`
- Original PyTorch implementation was created by [Yijun Li](https://github.com/Yijunmaverick/)
- Spaces/Models re-packaging and implementation by [Shō Akiyama](https://github.com/Yijunmaverick/).

##### Special Thanks
- [Nima Boscarino](https://github.com/NimaBoscarino)
- [Omar Sanseviero](https://github.com/osanseviero)
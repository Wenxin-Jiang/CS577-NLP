---
license: apache-2.0
library_name: keras
tags:
- image-to-image

---


## Zero-DCE for low-light image enhancement


**Original Author**: [Soumik Rakshit](https://github.com/soumik12345) <br>
**Date created**: 2021/09/18 <br>
**HF Contribution**: [Harveen Singh Chadha](https://github.com/harveenchadha)<br>
**Dataset**: [LOL Dataset](https://huggingface.co/Harveenchadha/low-light-image-enhancement/blob/main/lol_dataset.zip)

## [Spaces Demo](https://huggingface.co/spaces/Harveenchadha/low-light-image-enhancement)

## Description: Implementing Zero-Reference Deep Curve Estimation for low-light image enhancement.


Zero-Reference Deep Curve Estimation or Zero-DCE formulates low-light image enhancement as the task of estimating an image-specific tonal curve with a deep neural network. In this example, we train a lightweight deep network, DCE-Net, to estimate pixel-wise and high-order tonal curves for dynamic range adjustment of a given image.

Zero-DCE takes a low-light image as input and produces high-order tonal curves as its output. These curves are then used for pixel-wise adjustment on the dynamic range of the input to obtain an enhanced image. The curve estimation process is done in such a way that it maintains the range of the enhanced image and preserves the contrast of neighboring pixels. This curve estimation is inspired by curves adjustment used in photo editing software such as Adobe Photoshop where users can adjust points throughout an image’s tonal range.

Zero-DCE is appealing because of its relaxed assumptions with regard to reference images: it does not require any input/output image pairs during training. This is achieved through a set of carefully formulated non-reference loss functions, which implicitly measure the enhancement quality and guide the training of the network.


Sample Images:

<img src="https://keras.io/img/examples/vision/zero_dce/zero_dce_25_0.png" >
<img src="https://keras.io/img/examples/vision/zero_dce/zero_dce_25_1.png" >
<img src="https://keras.io/img/examples/vision/zero_dce/zero_dce_25_2.png" >
<img src="https://keras.io/img/examples/vision/zero_dce/zero_dce_25_3.png" >
<img src="https://keras.io/img/examples/vision/zero_dce/zero_dce_25_4.png" >
<img src="https://keras.io/img/examples/vision/zero_dce/zero_dce_25_5.png" >
<img src="https://keras.io/img/examples/vision/zero_dce/zero_dce_25_6.png" >
<img src="https://keras.io/img/examples/vision/zero_dce/zero_dce_25_7.png" >

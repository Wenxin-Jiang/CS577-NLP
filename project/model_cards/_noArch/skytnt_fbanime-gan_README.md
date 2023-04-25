---
tags:
- unconditional-image-generation
license: apache-2.0
---

# Model info

Project [fbanimegan](https://github.com/SkyTNT/fbanimegan)

### fbanime.pkl

StyleGan2 model trained with official [StyleGan3](https://github.com/NVlabs/stylegan3).
But I modified the code (networks_stylegan2.py and dataset.py) to support non-square resolutions.

FID: 1.4

### fbanime_fp32.pkl

fp32 version of fbanime.pkl

Note: Fp16 version (fbanime.pkl) only works on gpu. And fp32 version works on gpu and cpu.

### g_mapping.onnx

onnx format mapping network of fbanime_fp32.pkl

### g_synthesis.onnx

onnx format synthesis network of fbanime_fp32.pkl

### encoder.onnx

e4e model trained with [encoder4editing-stylegan3](https://github.com/yj7082126/encoder4editing-stylegan3).
I add support for official StyleGan2 model and change backbone to ResNet-34 in [restyle-encoder](https://github.com/yuval-alaluf/restyle-encoder).

### waifu_dect.onnx

YOLOv5 model trained with official [YOLOv5](https://github.com/ultralytics/yolov5)

# Usage

see [demo](https://huggingface.co/spaces/skytnt/full-body-anime-gan/blob/main/app.py)

# Dataset

[fbanimehq](https://huggingface.co/datasets/skytnt/fbanimehq) v2.0


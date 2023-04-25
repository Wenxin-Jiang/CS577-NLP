---
license: apache-2.0
library_name: keras
pipeline_tag: text-to-image
tags:
- text encoder
- stable diffusion
- v1.4
---

This repository hosts the TFLite version of `text encoder` part of [KerasCV Stable Diffusion](https://github.com/keras-team/keras-cv/tree/master/keras_cv/models/stable_diffusion). 

Stable Diffusion consists of `text encoder`, `diffusion model`, `decoder`, and some glue codes to handl inputs and outputs of each part. The TFLite version of `text encoder` in this repository is built not only with the `text encoder` itself but also TensorFlow operations that generates `context` and `unconditional context`. These output should be passed down to the `diffusion model` which is hosted in [this repository](https://huggingface.co/keras-sd/diffusion-model-tflite/tree/main).

TFLite conversion was based on the `SavedModel` from [this repository](https://huggingface.co/keras-sd/tfs-text-encoder/tree/main), and TensorFlow version `>= 2.12-nightly` was used.
  - NOTE: [Dynamic range quantization](https://www.tensorflow.org/lite/performance/post_training_quant#optimizing_an_existing_model) was used.
  - NOTE: TensorFlow version `< 2.12-nightly` will fail for the conversion process.
  - NOTE: For those who wonder how `SavedModel` is constructed, find it in [keras-sd-serving repository](https://github.com/deep-diver/keras-sd-serving).
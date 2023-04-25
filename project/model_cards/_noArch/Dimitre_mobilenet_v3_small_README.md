---
license: apache-2.0
library_name: tfhub
tags:
- vision
- image-classification
- mobilenet
- tensorflow
datasets:
- imagenet-1k
metrics:
- accuracy
---

## Model name: mobilenet_v3_small_100_224
## Description adapted from [TFHub](https://tfhub.dev/google/imagenet/mobilenet_v3_small_100_224/classification/5)

# Overview

MobileNet V3 is a family of neural network architectures for efficient on-device image classification and related tasks, originally published by

- Andrew Howard, Mark Sandler, Grace Chu, Liang-Chieh Chen, Bo Chen, Mingxing Tan, Weijun Wang, Yukun Zhu, Ruoming Pang, Vijay Vasudevan, Quoc V. Le, Hartwig Adam: ["Searching for MobileNetV3"](https://arxiv.org/abs/1905.02244), 2019.

Similar to other Mobilenets, MobileNet V3 uses a multiplier for the depth (number of features) in the convolutional layers to tune the accuracy vs. latency tradeoff. In addition, MobileNet V3 comes in two different sizes, small and large, to adapt the network to low or high resource use cases. Although V3 networks can be built with custom input resolutions, just like other Mobilenets, all pre-trained checkpoints were published with the same 224x224 input resolution.

For a quick comparison between these variants, please refer to the following table:

|Size|Depth multiplier|Top1 accuracy (%)|Pixel 1 (ms)|Pixel 2 (ms)|Pixel 3 (ms)|
|----|----------------|-----------------|------------|------------|------------|
|Large|1.0|75.2|51.2|61|44|
|Large|0.75|73.3|39.8|48|32|
|Small|1.0|67.5|15.8|19.4|14.4|
|Small|0.75|65.4|12.8|15.9|11.6|

This model uses the TF-Slim implementation of [`mobilenet_v3`](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet_v3.py) as a small network with a depth multiplier of 1.0.

The model contains a trained instance of the network, packaged to do the [image classification](https://www.tensorflow.org/hub/common_signatures/images#classification) that the network was trained on. If you merely want to transform images into feature vectors, use [`google/imagenet/mobilenet_v3_small_100_224/feature_vector/5`](https://tfhub.dev/google/imagenet/mobilenet_v3_small_100_224/feature_vector/5) instead, and save the space occupied by the classification layer.


# Training

The checkpoint exported into this model was `v3-small_224_1.0_float/ema/model-388500` downloaded from [MobileNet V3 pre-trained](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/README.md) models. Its weights were originally obtained by training on the ILSVRC-2012-CLS dataset for image classification ("Imagenet").

# Usage

This model can be used with the `hub.KerasLayer` as follows. It cannot be used with the `hub.Module` API for TensorFlow 1.

### Using TF Hub and HF Hub
```
model_path = snapshot_download(repo_id="Dimitre/mobilenet_v3_small")
model =  KerasLayer(handle=model_path)

img = np.random.rand(1, 224, 224, 3) # (batch_size, height, width, num_channels)
model(img) # output shape (1, 1001)
```

### Using [TF Hub fork](https://github.com/dimitreOliveira/hub)
```
model = pull_from_hub(repo_id="Dimitre/mobilenet_v3_small")

img = np.random.rand(1, 224, 224, 3) # (batch_size, height, width, num_channels)
model(img) # output shape (1, 1001)
```

The output is a batch of logits vectors. The indices into the logits are the `num_classes` = 1001 classes of the classification from the original training (see above). The mapping from indices to class labels can be found in the file at [download.tensorflow.org/data/ImageNetLabels.txt](https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt) (with class 0 for "background", followed by 1000 actual ImageNet classes).

The input images are expected to have color values in the range [0,1], following the [common image input](https://www.tensorflow.org/hub/common_signatures/images#input) conventions. For this model, the size of the input images is fixed to `height` x `width` = 224 x 224 pixels.

# Fine-tuning

In principle, consumers of this model can [fine-tune](https://www.tensorflow.org/hub/tf2_saved_model#fine-tuning) it by passing `trainable=True` to `hub.KerasLayer`.

However, fine-tuning through a large classification might be prone to overfit.

The momentum (a.k.a. decay coefficient) of batch norm's exponential moving averages defaults to 0.99 for this model, in order to accelerate training on small datasets (or with huge batch sizes).

### Using TF Hub and HF Hub
```
model_path = snapshot_download(repo_id="Dimitre/mobilenet_v3_small")
model =  KerasLayer(handle=model_path, trainable=True)

img = np.random.rand(1, 224, 224, 3) # (batch_size, height, width, num_channels)
model(img) # output shape (1, 1001)
```

### Using [TF Hub fork](https://github.com/dimitreOliveira/hub)
```
model = pull_from_hub(repo_id="Dimitre/mobilenet_v3_small", trainable=True)

img = np.random.rand(1, 224, 224, 3) # (batch_size, height, width, num_channels)
model(img) # output shape (1, 1001)
```
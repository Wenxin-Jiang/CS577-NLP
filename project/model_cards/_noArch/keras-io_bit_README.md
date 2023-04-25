---
tags:
- image-to-image
library_name: keras
---
## Model description
This repo contains the model for the notebook [Image Classification using BigTransfer (BiT)](https://keras.io/examples/vision/bit/).

Full credits go to [Sayan Nath](https://twitter.com/sayannath2350)

Reproduced by [Rushi Chaudhari](https://github.com/rushic24)

BigTransfer (also known as BiT) is a state-of-the-art transfer learning method for image classification.

## Dataset
The [Flower Dataset](https://github.com/tensorflow/datasets/blob/master/docs/catalog/tf_flowers.md) is A large set of images of flowers

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

```
RESIZE_TO = 384
CROP_TO = 224
BATCH_SIZE = 64
STEPS_PER_EPOCH = 10
AUTO = tf.data.AUTOTUNE  # optimise the pipeline performance
NUM_CLASSES = 5  # number of classes
SCHEDULE_LENGTH = (
    500  # we will train on lower resolution images and will still attain good results
)
SCHEDULE_BOUNDARIES = [
    200,
    300,
    400,
]
```

The hyperparamteres like `SCHEDULE_LENGTH` and `SCHEDULE_BOUNDARIES` are determined based on empirical results. The method has been explained in the [original paper](https://arxiv.org/abs/1912.11370) and in their [Google AI Blog Post](https://ai.googleblog.com/2020/05/open-sourcing-bit-exploring-large-scale.html).

The `SCHEDULE_LENGTH` is aslo determined whether to use [MixUp Augmentation](https://arxiv.org/abs/1710.09412) or not. You can also find an easy MixUp Implementation in [Keras Coding Examples](https://keras.io/examples/vision/mixup/).

![table](https://i.imgur.com/oSaIBYZ.jpeg)

### Training results

![Metrics Image](./metrics.png)
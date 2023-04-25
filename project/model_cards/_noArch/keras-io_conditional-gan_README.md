---
library_name: keras
tags:
- image-to-image
---
# Conditional Generative Adversarial Network
This repo contains the model and the notebook to [this Keras example on Conditional GAN](https://keras.io/examples/generative/conditional_gan/).

Full credits to: [Sayak Paul](https://twitter.com/RisingSayak)

# Background Information

Training a GAN conditioned on class labels to generate handwritten digits.

Generative Adversarial Networks (GANs) let us generate novel image data, video data, or audio data from a random input. Typically, the random input is sampled from a normal distribution, before going through a series of transformations that turn it into something plausible (image, video, audio, etc.).

However, a simple DCGAN doesn't let us control the appearance (e.g. class) of the samples we're generating. For instance, with a GAN that generates MNIST handwritten digits, a simple DCGAN wouldn't let us choose the class of digits we're generating. To be able to control what we generate, we need to condition the GAN output on a semantic input, such as the class of an image.

In this example, we'll build a Conditional GAN that can generate MNIST handwritten digits conditioned on a given class. Such a model can have various useful applications:

let's say you are dealing with an imbalanced image dataset, and you'd like to gather more examples for the skewed class to balance the dataset. Data collection can be a costly process on its own. You could instead train a Conditional GAN and use it to generate novel images for the class that needs balancing.
Since the generator learns to associate the generated samples with the class labels, its representations can also be used for other downstream tasks.
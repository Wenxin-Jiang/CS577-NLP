---
library_name: keras
tags:
- gan
- dcgan
- huggan
- tensorflow
- unconditional-image-generation
---

## Model description

Simple DCGAN implementation in TensorFlow to generate CryptoPunks.

## Generated samples
<img src="https://github.com/dimitreOliveira/cryptogans/raw/main/assets/gen_samples.png" width="350" height="350">

Project repository: [CryptoGANs](https://github.com/dimitreOliveira/cryptogans).

## Usage

You can play with the HuggingFace [space demo](https://huggingface.co/spaces/huggan/crypto-gan).

Or try it yourself

```python
import tensorflow as tf
import matplotlib.pyplot as plt
from huggingface_hub import from_pretrained_keras

seed = 42
n_images = 36
codings_size = 100
generator = from_pretrained_keras("huggan/crypto-gan")

def generate(generator, seed):
    noise = tf.random.normal(shape=[n_images, codings_size], seed=seed)
    generated_images = generator(noise, training=False)

    fig = plt.figure(figsize=(10, 10))
    for i in range(generated_images.shape[0]):
        plt.subplot(6, 6, i+1)
        plt.imshow(generated_images[i, :, :, :])
        plt.axis('off')
    plt.savefig("samples.png")
    
generate(generator, seed)
```

## Training data

For training, I used the 10000 CryptoPunks images.

## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>
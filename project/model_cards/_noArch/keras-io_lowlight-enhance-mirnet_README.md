---
tags:
- image-to-image
library_name: keras
---
## Model description
This repo contains the model and the notebook [Low-light image enhancement using MIRNet](https://keras.io/examples/vision/mirnet/).

Full credits go to [Soumik Rakshit](https://github.com/soumik12345)

Reproduced by [Vu Minh Chien](https://www.linkedin.com/in/vumichien/) with a slight change on hyperparameters.

With the goal of recovering high-quality image content from its degraded version, image restoration enjoys numerous applications, such as photography, security, medical imaging, and remote sensing. The MIRNet model for low-light image enhancement is a fully-convolutional architecture that learns an enriched set of features that combines contextual information from multiple scales, while simultaneously preserving the high-resolution spatial details
## Dataset
The [LoL Dataset](https://drive.google.com/uc?id=1DdGIJ4PZPlF2ikl8mNM9V-PdVxVLbQi6) has been created for low-light image enhancement. It provides 485 images for training and 15 for testing. Each image pair in the dataset consists of a low-light input image and its corresponding well-exposed reference image.
## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-04
- train_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: ReduceLROnPlateau
- num_epochs: 50

### Training results

- The results are shown in TensorBoard (Training metrics).


### View Model Demo 

![Model Demo](./demo.png)
  

<details>

<summary> View Model Plot </summary>

  ![Model Image](./model.png)
  
</details>
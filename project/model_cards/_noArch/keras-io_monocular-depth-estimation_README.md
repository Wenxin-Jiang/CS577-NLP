---
tags:
- image-segmentation
library_name: keras
---
## Model description
The original idea from Keras examples [Monocular depth estimation](https://keras.io/examples/vision/depth_estimation/) of author [Victor Basu](https://www.linkedin.com/in/victor-basu-520958147/)

Full credits go to [Vu Minh Chien](https://www.linkedin.com/in/vumichien/)

Depth estimation is a crucial step towards inferring scene geometry from 2D images. The goal in monocular depth estimation is to predict the depth value of each pixel or infer depth information, given only a single RGB image as input.

## Dataset
[NYU Depth Dataset V2](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html) is comprised of video sequences from a variety of indoor scenes as recorded by both the RGB and Depth cameras from the Microsoft Kinect. 

## Training procedure

### Training hyperparameters
**Model architecture**:
- UNet with a pretrained DenseNet 201 backbone.

The following hyperparameters were used during training:
- learning_rate: 1e-04
- train_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: ReduceLROnPlateau
- num_epochs: 10

### Training results

| Epoch  | Training loss | Validation Loss | Learning rate | 
|:------:|:-------------:|:---------------:|:-------------:|
|   1    |    0.1333     |     0.1315      |     1e-04     |
|   2    |    0.0948     |     0.1232      |     1e-04     |
|   3    |    0.0834     |     0.1220      |     1e-04     | 
|   4    |    0.0775     |     0.1213      |     1e-04     | 
|   5    |    0.0736     |     0.1196      |     1e-04     |
|   6    |    0.0707     |     0.1205      |     1e-04     | 
|   7    |    0.0687     |     0.1190      |     1e-04     | 
|   8    |    0.0667     |     0.1177      |     1e-04     |
|   9    |    0.0654     |     0.1177      |     1e-04     |
|   10   |    0.0635     |     0.1182      |     9e-05     |



### View Model Demo 

![Model Demo](./demo.png)
  

<details>

<summary> View Model Plot </summary>

  ![Model Image](./model.png)
  
</details>

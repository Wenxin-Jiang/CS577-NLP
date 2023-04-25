---
library_name: keras
tags:
- ShiftVit
- image-classification
---

## Model description

ShiftViT is a variation of the Vision Transformer (ViT) where the attention operation has been replaced with a shifting operation.

ShiftViT model was proposed as part of the paper [When Shift Operation Meets Vision Transformer: An Extremely Simple Alternative to Attention Mechanism](https://arxiv.org/abs/2201.10801).
Vision Transformers have lately become very popular for computer vision problems and a lot researchers attribute their success to the attention layers. The authors of the ShiftViT paper have tried to show via the ShiftViT model that even without the attention operation, ViTs can reach SoTA results.  

## Model Architecture

The architecture for ShiftViT is inspired by the paper  [Swin Transformer: Hierarchical Vision Transformer using Shifted Windows](https://arxiv.org/abs/2103.14030)

Here the authors propose a modular architecture with 4 stages. Each stage works on its own spatial size, creating a hierarchical architecture.

| ![ShiftViT Architecture](https://i.imgur.com/CHU40HX.png) |
| :--: |
| Figure 1: The entire architecutre of ShiftViT.
[Source](https://arxiv.org/abs/2201.10801) |

Each stage in the ShiftViT architecture comprises of a Shift Block as shown in Fig 2.

| ![ShiftViT block](https://i.imgur.com/IDe35vo.gif) |
| :--: |
| Figure 2: From the Model to a Shift Block. |

**The Shift Block as shown in Fig. 2, comprises of the following:**

- Shift Operation
- Linear Normalization
- MLP Layer: stack of densely-connected layers


**How shift operation works:**
1. Split the channels 
2. Select each of the first four spilts and shift and pad them in the respective directions.
3. After shifting and padding, we concatenate the channel back.

 | ![Manim rendered animation for shift operation](https://i.imgur.com/PReeULP.gif) |
| :--: |
| Figure 3: The TensorFlow style shifting |

## Intended uses 

This ShiftViT model is trained to be used for image classification task. 

However, the ShiftViT architecture can be used for a variety of visual recognition tasks. 
The authors of the [ShiftViT paper](https://arxiv.org/abs/2201.10801) tested the model on the following tasks:
- Image Classification on ImageNet-1k dataset
- Object Detection on COCO dataset
- Semantic Segmentation on ADE20k dataset

## Training and evaluation data

The dataset used for training the model is CIFAR-10.
The CIFAR-10 dataset is a popular dataset used for image classification. It contains images belonging to the following 10 classes:

| Classes | 
| :-- | 
| airplane | 
| automobile | 
| bird | 
| cat | 
| deer | 
| dog | 
| frog | 
| horse | 
| ship | 
| truck |  

No. of samples used for training and evaluation are:
- Training samples: 40000
- Validation samples: 10000
- Testing samples: 10000

## Training procedure

1. Data Preparation:

 - Data Augmentation: The augmentation steps used for data preparation include: rescaling, resizing, cropping and horizontal flipping.
 
 2. Building the ShiftViT Model:
 
 - The steps for constructing the ShiftViT model have been covered extensively in this [Keras example](https://keras.io/examples/vision/shiftvit/)
 
 3. Model Training:
 
 The model is then trained using the following config:
 
 | Training Config | Value |
| :-- | :-- |
| Optimizer | Adam |
| Loss Function | sparse_categorical_crossentropy|
| Metric | Accuracy |
| Epochs | 5 |

4. Model Testing:

The model is tested on the test data post training achieving an accuracy of ~90%.


### Training hyperparameters

The following hyperparameters were used during training:

| Hyperparameters | Value |
| :-- | :-- |
| name | AdamW |
| learning_rate.class_name | WarmUpCosine |
| learning_rate.config.lr_start | 1e-05 |
| learning_rate.config.lr_max | 0.001 |
| learning_rate.config.total_steps | 312 |
| learning_rate.config.warmup_steps | 46 |
| decay | 0.0 |
| beta_1 | 0.8999999761581421 |
| beta_2 | 0.9990000128746033 |
| epsilon | 1e-07 |
| amsgrad | False |
| weight_decay | 9.999999747378752e-05 |
| exclude_from_weight_decay | None |
| training_precision | float32 |


 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./Model.png)

</details>

## Credits:

- HF Contribution: [Shivalika Singh](https://www.linkedin.com/in/shivalika-singh)
- Full credits to original [Keras example](https://keras.io/examples/vision/shiftvit/) by [Aritra Roy Gosthipaty](https://twitter.com/ariG23498) and [Ritwik Raha](https://twitter.com/ritwik_raha)
- Check out the demo space [here](https://huggingface.co/spaces/keras-io/shiftvit)

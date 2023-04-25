---
tags:
- image-classification
- keras
license: apache-2.0
---
# Train a Vision Transformer on small datasets

Author: [Jónathan Heras](https://twitter.com/_Jonathan_Heras)

[Keras Blog](https://keras.io/examples/vision/vit_small_ds/) | [Colab Notebook](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/vision/ipynb/vit_small_ds.ipynb)

In the academic paper [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929), the authors mention that Vision Transformers (ViT) are data-hungry. Therefore, pretraining a ViT on a large-sized dataset like JFT300M and fine-tuning it on medium-sized datasets (like ImageNet) is the only way to beat state-of-the-art Convolutional Neural Network models.

The self-attention layer of ViT lacks locality inductive bias (the notion that image pixels are locally correlated and that their correlation maps are translation-invariant). This is the reason why ViTs need more data. On the other hand, CNNs look at images through spatial sliding windows, which helps them get better results with smaller datasets.

In the academic paper [Vision Transformer for Small-Size Datasets](https://arxiv.org/abs/2112.13492v1), the authors set out to tackle the problem of locality inductive bias in ViTs.

The main ideas are:

- Shifted Patch Tokenization
- Locality Self Attention

# Use the pre-trained model

The model is pre-trained on the CIFAR100 dataset with the following hyperparameters:
```python
# DATA
NUM_CLASSES = 100
INPUT_SHAPE = (32, 32, 3)
BUFFER_SIZE = 512
BATCH_SIZE = 256

# AUGMENTATION
IMAGE_SIZE = 72
PATCH_SIZE = 6
NUM_PATCHES = (IMAGE_SIZE // PATCH_SIZE) ** 2

# OPTIMIZER
LEARNING_RATE = 0.001
WEIGHT_DECAY = 0.0001

# TRAINING
EPOCHS = 50

# ARCHITECTURE
LAYER_NORM_EPS = 1e-6
TRANSFORMER_LAYERS = 8
PROJECTION_DIM = 64
NUM_HEADS = 4
TRANSFORMER_UNITS = [
    PROJECTION_DIM * 2,
    PROJECTION_DIM,
]
MLP_HEAD_UNITS = [
    2048,
    1024
]
```
I have used the `AdamW` optimizer with cosine decay learning schedule. You can find the entire implementation in the keras blog post.

To use the pretrained model:
```python
loaded_model = from_pretrained_keras("keras-io/vit_small_ds_v2")
```

---
license: mit
tags:
- vision
- image-classification
- tensorflow
pipeline_tag: image-classification
library_name: keras
datasets:
- svnfs/depth-of-field
widget:
- src: https://huggingface.co/datasets/svnfs/depth-of-field/blob/main/data/0/-1a83VD65ss.jpg
  example_title: Shallow DoF
- src: https://huggingface.co/datasets/svnfs/depth-of-field/blob/main/data/1/007R8JewpwU.jpg
  example_title: Deep DoF  
---
# Bokeh (ボケ Japanese word for blur) 

Bokeh model is based on a densenet like architecture trained on Unsplash images at 300x200 resolution. It classifies whether an photo is capture with bokeh producing a shallow depth of field

## Model description

Bokeh model is based on a DenseNet architecture. The model is trained with a mini-batch size of 32 samples with Adam optimizer and a learning rate $0.0001$.
It has 3.632 trainable parameters, 8 convolution filters are used for the network's input, with $7\times7$ kernel size.

## Training data

The bokeh model is pretrained on [depth-of-field](https://huggingface.co/datasets/svnfs/depth-of-field) dataset, a dataset consisted of 1200 images and 2 classes manually annotated.
### BibTeX entry and citation info

```
@article{sniafas2021,
  title={DoF: An image dataset for depth of field classification},
  author={Niafas, Stavros},
  doi= {10.13140/RG.2.2.17217.89443},
  url= {https://www.researchgate.net/publication/355917312_Photography_Style_Analysis_using_Machine_Learning}
  year={2021}
}
```

---
license: apache-2.0
tags:
- vision
- image-classification
datasets:
- nih-pc-chex-mimic_ch-google-openi-rsna
---
    
    
# densenet121-res224-mimic_nb

A DenseNet is a type of convolutional neural network that utilises dense connections between layers, through Dense Blocks, where we connect all layers (with matching feature-map sizes) directly with each other. To preserve the feed-forward nature, each layer obtains additional inputs from all preceding layers and passes on its own feature-maps to all subsequent layers.
        

### How to use

Here is how to use this model to classify an image of xray:

Note: Each pretrained model has 18 outputs. The `all` model has every output trained. However, for the other weights some targets are not trained and will predict randomly becuase they do not exist in the training dataset. The only valid outputs are listed in the field `{dataset}.pathologies` on the dataset that corresponds to the weights. 


Benchmarks of the modes are here: [BENCHMARKS.md](https://github.com/mlmed/torchxrayvision/blob/master/BENCHMARKS.md)
```python
import urllib.request

import skimage
import torch
import torch.nn.functional as F
import torchvision
import torchvision.transforms

import torchxrayvision as xrv

model_name = "densenet121-res224-mimic_nb"

img_url = "https://huggingface.co/spaces/torchxrayvision/torchxrayvision-classifier/resolve/main/16747_3_1.jpg"
img_path = "xray.jpg"
urllib.request.urlretrieve(img_url, img_path)

model = xrv.models.get_model(model_name, from_hf_hub=True)

img = skimage.io.imread(img_path)
img = xrv.datasets.normalize(img, 255)

# Check that images are 2D arrays
if len(img.shape) > 2:
    img = img[:, :, 0]
if len(img.shape) < 2:
    print("error, dimension lower than 2 for image")

# Add color channel
img = img[None, :, :]

transform = torchvision.transforms.Compose([xrv.datasets.XRayCenterCrop()])

img = transform(img)

with torch.no_grad():
    img = torch.from_numpy(img).unsqueeze(0)
    preds = model(img).cpu()
    output = {
        k: float(v)
        for k, v in zip(xrv.datasets.default_pathologies, preds[0].detach().numpy())
    }
print(output)

```
For more code examples, we refer to the [example scripts](https://github.com/kamalkraj/torchxrayvision/blob/master/scripts).


### Citation

Primary TorchXRayVision paper: [https://arxiv.org/abs/2111.00595](https://arxiv.org/abs/2111.00595)

```
Joseph Paul Cohen, Joseph D. Viviano, Paul Bertin, Paul Morrison, Parsa Torabian, Matteo Guarrera, Matthew P Lungren, Akshay Chaudhari, Rupert Brooks, Mohammad Hashir, Hadrien Bertrand
TorchXRayVision: A library of chest X-ray datasets and models. 
https://github.com/mlmed/torchxrayvision, 2020


@article{Cohen2020xrv,
author = {Cohen, Joseph Paul and Viviano, Joseph D. and Bertin, Paul and Morrison, Paul and Torabian, Parsa and Guarrera, Matteo and Lungren, Matthew P and Chaudhari, Akshay and Brooks, Rupert and Hashir, Mohammad and Bertrand, Hadrien},
journal = {https://github.com/mlmed/torchxrayvision},
title = {{TorchXRayVision: A library of chest X-ray datasets and models}},
url = {https://github.com/mlmed/torchxrayvision},
year = {2020}
arxivId = {2111.00595},
}


```
and this paper which initiated development of the library: [https://arxiv.org/abs/2002.02497](https://arxiv.org/abs/2002.02497)
```
Joseph Paul Cohen and Mohammad Hashir and Rupert Brooks and Hadrien Bertrand
On the limits of cross-domain generalization in automated X-ray prediction. 
Medical Imaging with Deep Learning 2020 (Online: https://arxiv.org/abs/2002.02497)

@inproceedings{cohen2020limits,
  title={On the limits of cross-domain generalization in automated X-ray prediction},
  author={Cohen, Joseph Paul and Hashir, Mohammad and Brooks, Rupert and Bertrand, Hadrien},
  booktitle={Medical Imaging with Deep Learning},
  year={2020},
  url={https://arxiv.org/abs/2002.02497}
}
```
    
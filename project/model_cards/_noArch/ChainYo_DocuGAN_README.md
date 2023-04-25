---
license: mit
library_name: pytorch
tags:
- gan
- sngan
- huggan
- unconditional-image-generation
datasets: 
- ChainYo/rvl-cdip-invoice
---

## Model description

SN-GAN implementation with PyTorch-Lightning to generate Documents.

## Generated samples

<img src="https://raw.githubusercontent.com/ChainYo/docugan/master/documents_samples.png" width="400" height="1200">

Project repository: [DocuGAN](https://github.com/ChainYo/docugan).

## Usage

You can see the tool to generate document on HuggingFace by trying the [space demo](https://huggingface.co/spaces/ChainYo/DocuGAN).

## Training data

For training, I used the invoices subpart of `RVL-CDIP` dataset. Find the full dataset [here](https://huggingface.co/datasets/ChainYo/rvl-cdip)

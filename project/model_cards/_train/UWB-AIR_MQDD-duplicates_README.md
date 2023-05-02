---
license: cc-by-nc-sa-4.0
---

# MQDD - Multimodal Question Duplicity Detection

This repository publishes trained models and other supporting materials for the paper 
[MQDD – Pre-training of Multimodal Question Duplicity Detection for Software Engineering Domain](https://arxiv.org/abs/2203.14093). For more information, see the paper.
The Stack Overflow Datasets (SOD) and Stack Overflow Duplicity Dataset (SODD) presented in the paper can be obtained from our [Stack Overflow Dataset repository](https://github.com/kiv-air/StackOverflowDataset).

To acquire the pre-trained model only, see the [UWB-AIR/MQDD-pretrained](https://huggingface.co/UWB-AIR/MQDD-pretrained).

## Fine-tuned MQDD

We release a fine-tuned version of our MQDD model for duplicate detection task. The model's architecture follows the architecture of a two-tower model as depicted in the figure below:

<img src="https://raw.githubusercontent.com/kiv-air/MQDD/master/img/architecture.png" width="700">

A self-standing encoder without a duplicate detection head can be loaded using the following source code snippet. Such a model can be used for building search systems based, for example, on [Faiss](https://github.com/facebookresearch/faiss) library.

```Python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("UWB-AIR/MQDD-duplicates")
model = AutoModel.from_pretrained("UWB-AIR/MQDD-duplicates")
```

A checkpoint of a full two-tower model can than be obtained from our [GoogleDrive folder](https://drive.google.com/drive/folders/1CYiqF2GJ2fSQzx_oM4-X_IhpObi4af5Q?usp=sharing). To load the model, one needs to use the model's implementation from `models/MQDD_model.py` in our [GitHub repository](https://github.com/kiv-air/MQDD). To construct the model and load it's checkpoint, use the following source code:

```Python
from MQDD_model import ClsHeadModelMQDD

model = ClsHeadModelMQDD("UWB-AIR/MQDD-duplicates")
ckpt = torch.load("model.pt",  map_location="cpu")
model.load_state_dict(ckpt["model_state"])
```

## Licence
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. http://creativecommons.org/licenses/by-nc-sa/4.0/

## How should I cite the MQDD? 
For now, please cite [the Arxiv paper](https://arxiv.org/abs/2203.14093):
```
@misc{https://doi.org/10.48550/arxiv.2203.14093,
  doi = {10.48550/ARXIV.2203.14093},
  url = {https://arxiv.org/abs/2203.14093},
  author = {Pašek, Jan and Sido, Jakub and Konopík, Miloslav and Pražák, Ondřej},
  title = {MQDD -- Pre-training of Multimodal Question Duplicity Detection for Software Engineering Domain},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution Non Commercial Share Alike 4.0 International}
}
```

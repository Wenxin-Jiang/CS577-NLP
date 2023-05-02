---
license: cc-by-nc-sa-4.0
---

# MQDD - Multimodal Question Duplicity Detection

This repository publishes pre-trained model for the paper 
[MQDD – Pre-training of Multimodal Question Duplicity Detection for Software Engineering Domain](https://arxiv.org/abs/2203.14093). For more information, see the paper.
The Stack Overflow Datasets (SOD) and Stack Overflow Duplicity Dataset (SODD) presented in the paper can be obtained from our [Stack Overflow Dataset repository](https://github.com/kiv-air/StackOverflowDataset).

To acquire the fine-tuned model, see [UWB-AIR/MQDD-duplicate](https://huggingface.co/UWB-AIR/MQDD-duplicates).

The MQDD model, which is based on a Longformer architecture and is pre-trained on 218.5M training examples. The model was trained using MLM training objective accompanied with our novel Same Post (SP) and Question Answer (QA) learning objectives targeting specifically the duplicate detection task. 

The model can be loaded using the following source code snippet:

```Python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("UWB-AIR/MQDD-pretrained")
model = AutoModel.from_pretrained("UWB-AIR/MQDD-pretrained")
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

---
language: en
---
# CPT

This repository contains the code and pre-trained models for our EMNLP'22 paper [Continual Training of Language Models for Few-Shot Learning](https://arxiv.org/abs/2210.05549) by <a href="https://vincent950129.github.io/"> Zixuan Ke</a>, <a href="https://linhaowei1.github.io/">Haowei Lin</a>, <a href="https://shaoyijia.github.io/">Yijia Shao</a>, <a href="https://howardhsu.github.io/">Hu Xu</a>, <a href="https://leishu02.github.io/">Lei Shu</a>, and <a href="https://www.cs.uic.edu/~liub/">Bing Liu</a>.

## Requirements

First, install PyTorch by following the instructions from [the official website](https://pytorch.org). To faithfully reproduce our results, please use the correct `1.7.0` version corresponding to your platforms/CUDA versions. PyTorch version higher than `1.7.0` should also work. For example, if you use Linux and **CUDA11** ([how to check CUDA version](https://varhowto.com/check-cuda-version/)), install PyTorch by the following command,

```bash
pip install torch==1.7.0+cu110 -f https://download.pytorch.org/whl/torch_stable.html
```

If you instead use **CUDA** `<11` or **CPU**, install PyTorch by the following command,

```bash
pip install torch==1.7.0
```

Then run the following script to install the remaining dependencies,

```bash
pip install -r requirements.txt
```

**Attention**: Our model is based on `transformers==4.11.3` and `adapter-transformers==2.2.0`. Using them from other versions may cause some unexpected bugs.

## Use CPT with Huggingface

You can easily import our continually post-trained model with HuggingFace's `transformers`:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Import our model. The package will take care of downloading the models automatically
tokenizer = AutoTokenizer.from_pretrained("roberta-base")
model = AutoModelForSequenceClassification.from_pretrained("UIC-Liu-Lab/CPT", trust_remote_code=True)

# Tokenize input texts
texts = [
    "There's a kid on a skateboard.",
    "A kid is skateboarding.",
    "A kid is inside the house."
]
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")

# Task id and smax
t = torch.LongTensor([0]).to(model.device)	# using task 0's CL-plugin, choose from {0, 1, 2, 3}
smax = 400

# Get the model output!
res = model(**inputs, return_dict=True, t=t, s=smax)
```

If you encounter any problem when directly loading the models by HuggingFace's API, you can also download the models manually from the [repo](https://huggingface.co/UIC-Liu-Lab/CPT/tree/main) and use `model = AutoModel.from_pretrained({PATH TO THE DOWNLOAD MODEL})`.

Note: The post-trained weights you load contain un-trained classification heads. The post-training sequence is `Restaurant -> AI -> ACL -> AGNews`, you can use the downloaded weights to fine-tune the corresponding end-task. The results (MF1/Acc) will be consistent with follows.

|                 | Restaurant    | AI            | ACL           | AGNews        | Avg.          |
| --------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| UIC-Liu-Lab/CPT | 53.90 / 75.13 | 30.42 / 30.89 | 37.56 / 38.53 | 63.77 / 65.79 | 46.41 / 52.59 |


## Citation

Please cite our paper if you use CPT in your work:

```bibtex
@inproceedings{ke2022continual,
   title={Continual Training of Language Models for Few-Shot Learning},
   author={Ke, Zixuan and Lin, Haowei and Shao, Yijia and Xu, Hu and Shu, Lei, and Liu, Bing},
   booktitle={Empirical Methods in Natural Language Processing (EMNLP)},
   year={2022}
}
```


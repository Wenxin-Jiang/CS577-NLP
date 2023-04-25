---
tags:
- background-removal
- computer-vision
- image-segmentation
license: apache-2.0
library: pytorch
inference: false
---

# IS-Net_DIS

* Model Authors: Xuebin Qin, Hang Dai, Xiaobin Hu, Deng-Ping Fan*, Ling Shao, Luc Van Gool
* Paper: Highly Accurate Dichotomous Image Segmentation (ECCV 2022 - https://arxiv.org/pdf/2203.03041.pdf
* Code Repo: https://github.com/xuebinqin/DIS
* Project Homepage: https://xuebinqin.github.io/dis/index.html

From the paper abstract:

> [...]  we introduce a simple intermediate supervision baseline (IS- Net) using both feature-level and mask-level guidance for DIS model training. Without tricks, IS-Net outperforms var- ious cutting-edge baselines on the proposed DIS5K, mak- ing it a general self-learned supervision network that can help facilitate future research in DIS.

![](https://raw.githubusercontent.com/xuebinqin/DIS/main/figures/is-net.png)

[HCE score](https://github.com/xuebinqin/DIS#4-human-correction-efforts-hce): 1016 

# Citation

```
@InProceedings{qin2022,
      author={Xuebin Qin and Hang Dai and Xiaobin Hu and Deng-Ping Fan and Ling Shao and Luc Van Gool},
      title={Highly Accurate Dichotomous Image Segmentation},
      booktitle={ECCV},
      year={2022}
}
```

---
language: 
  - zh
license: apache-2.0
---

# Mengzi-oscar-base (Chinese Multi-modal pre-training model)
Mengzi-oscar is trained based on the Multi-modal pre-training model [Oscar](https://github.com/microsoft/Oscar), and is initialized using [Mengzi-Bert-Base](https://github.com/Langboat/Mengzi). 3.7M pairs of images and texts were used, including 0.7M Chinese image-caption pairs, 3M Chinese image-question pairs, a total of 0.22M different images.

[Mengzi: Towards Lightweight yet Ingenious Pre-trained Models for Chinese](https://arxiv.org/abs/2110.06696)


## Usage
#### Installation
Check [INSTALL.md](https://github.com/microsoft/Oscar/blob/master/INSTALL.md) for installation instructions.
#### Pretrain & fine-tune
See the [Mengzi-Oscar.md](https://github.com/Langboat/Mengzi/blob/main/Mengzi-Oscar.md) for details.

## Citation
If you find the technical report or resource is useful, please cite the following technical report in your paper.
```
@misc{zhang2021mengzi,
      title={Mengzi: Towards Lightweight yet Ingenious Pre-trained Models for Chinese}, 
      author={Zhuosheng Zhang and Hanqing Zhang and Keming Chen and Yuhang Guo and Jingyun Hua and Yulong Wang and Ming Zhou},
      year={2021},
      eprint={2110.06696},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
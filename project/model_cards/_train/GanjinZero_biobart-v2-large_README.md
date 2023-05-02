---
language: 
  - en
license: apache-2.0

tags:
- bart
- biobart
- biomedical

inference: true

widget:
- text: "Influenza is a <mask> disease."
- type: "text-generation"

---

Paper: [BioBART: Pretraining and Evaluation of A Biomedical Generative Language Model](https://arxiv.org/pdf/2204.03905.pdf)

V2 adopts a new biomedical vocab.

```
@misc{BioBART,
  title={BioBART: Pretraining and Evaluation of A Biomedical Generative Language Model},
  author={Hongyi Yuan and Zheng Yuan and Ruyi Gan and Jiaxing Zhang and Yutao Xie and Sheng Yu},
  year={2022},
  eprint={2204.03905},
  archivePrefix={arXiv}
}
```
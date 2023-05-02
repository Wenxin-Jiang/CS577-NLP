---
language: ur
license: afl-3.0
---

This model is used to detect **abusive speech** in **Urdu**. It is finetuned on MuRIL model using Urdu abusive speech dataset.
The model is trained with learning rates of 2e-5. Training code can be found at this [url](https://github.com/hate-alert/IndicAbusive)

LABEL_0 :-> Normal

LABEL_1 :-> Abusive


### For more details about our paper

Mithun Das, Somnath Banerjee and Animesh Mukherjee. "[Data Bootstrapping Approaches to Improve Low Resource Abusive Language Detection for Indic Languages](https://arxiv.org/abs/2204.12543)". Accepted at ACM HT 2022.

***Please cite our paper in any published work that uses any of these resources.***
~~~
@article{das2022data,
  title={Data Bootstrapping Approaches to Improve Low Resource Abusive Language Detection for Indic Languages},
  author={Das, Mithun and Banerjee, Somnath and Mukherjee, Animesh},
  journal={arXiv preprint arXiv:2204.12543},
  year={2022}
}
~~~
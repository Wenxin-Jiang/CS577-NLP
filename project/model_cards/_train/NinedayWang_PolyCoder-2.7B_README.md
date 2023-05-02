This is a PolyCoder model with **2.7B** parameters, 
presented in the paper ["A Systematic Evaluation of Large Language Models of Code"](https://arxiv.org/pdf/2202.13169.pdf) (MAPS'2022 and ICLR'2022 Workshop Deep Learning 4 Code).

The model was trained on **249 GB** of code across **12** programming languages.

**Note** - this model requires `transformers` version of at least **4.23.0**:
```
pip install transformers==4.23.0
```
For more information, see: [https://github.com/VHellendoorn/Code-LMs](https://github.com/VHellendoorn/Code-LMs)

If you use this model, please cite:
```
@inproceedings{
  xu2022polycoder,
  title={A Systematic Evaluation of Large Language Models of Code},
  author={Frank F. Xu and Uri Alon and Graham Neubig and Vincent Josua Hellendoorn},
  booktitle={Deep Learning for Code Workshop},
  year={2022},
  url={https://openreview.net/forum?id=SLcEnoObJZq}
}
```
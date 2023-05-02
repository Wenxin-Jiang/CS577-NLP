---
widget:
- text: "low lung volumes, [MASK] pulmonary vascularity."
tags:
- fill-mask
- pytorch
- transformers
- bert
- biobert 
- radbert 
- language-model
- uncased
- radiology
- biomedical
datasets:
- wikipedia
- bookscorpus
- pubmed
- radreports
language:
  - en
license: mit
---

RadBERT was continuously pre-trained on radiology reports from a BioBERT initialization. 

## Citation

```bibtex
@article{chambon_cook_langlotz_2022, 
  title={Improved fine-tuning of in-domain transformer model for inferring COVID-19 presence in multi-institutional radiology reports}, 
  DOI={10.1007/s10278-022-00714-8}, journal={Journal of Digital Imaging}, 
  author={Chambon, Pierre and Cook, Tessa S. and Langlotz, Curtis P.}, 
  year={2022}
} 
```
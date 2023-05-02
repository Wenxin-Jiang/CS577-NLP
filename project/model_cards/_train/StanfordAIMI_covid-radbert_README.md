---
widget:
- text: "procedure: single ap view of the chest comparison: none findings: no surgical hardware nor tubes. lungs, pleura: low lung volumes, bilateral airspace opacities. no pneumothorax or pleural effusion. cardiovascular and mediastinum: the cardiomediastinal silhouette seems stable. impression: 1. patchy bilateral airspace opacities, stable, but concerning for multifocal pneumonia. 2. absence of other suspicions, the rest of the lungs seems fine."
- text: "procedure: single ap view of the chest comparison: none findings: No surgical hardware nor tubes. lungs, pleura: low lung volumes, bilateral airspace opacities. no pneumothorax or pleural effusion. cardiovascular and mediastinum: the cardiomediastinal silhouette seems stable. impression: 1. patchy bilateral airspace opacities, stable. 2. some areas are suggestive that pneumonia can not be excluded. 3. recommended to follow-up shortly and check if there are additional symptoms"
tags:
- text-classification
- pytorch
- transformers
- uncased
- radiology 
- biomedical
- covid-19
- covid19
language:
  - en
license: mit
---
COVID-RadBERT was trained to detect the presence or absence of COVID-19 within radiology reports, along an "uncertain" diagnostic when further medical tests are required. 

## Citation

```bibtex
@article{chambon_cook_langlotz_2022, 
  title={Improved fine-tuning of in-domain transformer model for inferring COVID-19 presence in multi-institutional radiology reports}, 
  DOI={10.1007/s10278-022-00714-8}, journal={Journal of Digital Imaging}, 
  author={Chambon, Pierre and Cook, Tessa S. and Langlotz, Curtis P.}, 
  year={2022}
} 
```
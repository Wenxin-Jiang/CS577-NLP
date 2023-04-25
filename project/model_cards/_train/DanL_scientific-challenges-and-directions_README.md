---
tags:
- generated_from_trainer
- text-classification

language:
- en

datasets:
- DanL/scientific-challenges-and-directions-dataset

widget:
- text: "severe atypical cases of pneumonia emerged and quickly spread worldwide."
  example_title: "challenge"
- text: "we speculate that studying IL-6 will be beneficial."
  example_title: "direction"
- text: "in future studies, both PRRs should be tested as the cause for multiple deaths."
  example_title: "both"
- text: "IbMADS1-transformed potatoes exhibited tuber morphogenesis in the fibrous roots."
  example_title: "neither"


metrics:
- precision
- recall
- f1
model-index:
- name: scientific-challenges-and-directions
  results: []
---

# scientific-challenges-and-directions

We present a novel resource to help scientists and medical professionals discover challenges and potential directions across scientific literature, focusing on a broad corpus pertaining to the COVID-19 pandemic and related historical research. At a high level, the _challenges_ and _directions_ are defined as follows:

* **Challenge**: A sentence mentioning a problem, difficulty, flaw, limitation, failure, lack of clarity, or knowledge gap.
* **Research direction**: A sentence mentioning suggestions or needs for further research, hypotheses, speculations, indications or hints that an issue is worthy of exploration.  

* This model here is described in our paper: [A Search Engine for Discovery of Scientific Challenges and Directions](https://arxiv.org/abs/2108.13751) (though we've upgraded the infrastructure since the paper was released - there are slight differences in the results).
* Our dataset can be found [here](https://huggingface.co/datasets/DanL/scientific-challenges-and-directions-dataset).
* Please cite our paper if you use our datasets or models in your project. See the [BibTeX](#citation). 
* Feel free to [email us](#contact-us). 
* Also, check out [our search engine](https://challenges.apps.allenai.org/), as an example application.

## Model description
This model is a fine-tuned version of [PubMedBERT](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the [scientific-challenges-and-directions-dataset](https://huggingface.co/datasets/DanL/scientific-challenges-and-directions-dataset), designed for multi-label text classification.

## Training and evaluation data
The scientific-challenges-and-directions model is trained based on a dataset that is a collection of 2894 sentences and their surrounding contexts, from 1786 full-text papers in the CORD-19 corpus, labeled for classification of challenges and directions by expert annotators with biomedical and bioNLP backgrounds. For full details on the train/test/split of the data see section 3.1 in our [paper](https://arxiv.org/abs/2108.13751)

## Example notebook
We include an example notebook that uses the model for inference in our [repo](https://github.com/Dan-La/scientific-challenges-and-directions). See `Inference_Notebook.ipynb`.
A training notebook is also included.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning rate: 2e-05
- train batch size: 8
- eval batch size: 4
- seed: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr scheduler type: linear
- lr scheduler warmup steps: 500
- num epochs: 30

### Training results
The achieves the following results on the test set:
- Precision Challenge: 0.768719  
- Recall Challenge: 0.780405  
- F1 Challenge: 0.774518
- Precision Direction: 0.758112  
- Recall Direction: 0.774096  
- F1 Direction: 0.766021
- Precision (micro avg. on both labels): 0.764894  
- Recall (micro avg. on both labels): 0.778139  
- F1 (micro avg. on both labels): 0.771459

### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3

## Citation

If using our dataset and models, please cite:

```
@misc{lahav2021search,
      title={A Search Engine for Discovery of Scientific Challenges and Directions}, 
      author={Dan Lahav and Jon Saad Falcon and Bailey Kuehl and Sophie Johnson and Sravanthi Parasa and Noam Shomron and Duen Horng Chau and Diyi Yang and Eric Horvitz and Daniel S. Weld and Tom Hope},
      year={2021},
      eprint={2108.13751},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## Contact us

Please don't hesitate to reach out.

**Email:** `lahav@mail.tau.ac.il`,`tomh@allenai.org`.

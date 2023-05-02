---
datasets:
- SZTAKI-HLT/HunSum-1
language:
- hu
metrics:
- rouge
pipeline_tag: text2text-generation
inference:
  parameters:
    num_beams: 5
    length_penalty: 2
    max_length: 128
    no_repeat_ngram_size: 3
    early_stopping: True
tags:
- hubert
- bert
- summarization
---

# Model Card for Bert2Bert-HunSum-1

The Bert2Bert-HunSum-1 is a Hungarian abstractive summarization model, which was trained on the [SZTAKI-HLT/HunSum-1 dataset](https://huggingface.co/datasets/SZTAKI-HLT/HunSum-1).
The model is based on [SZTAKI-HLT/hubert-base-cc](https://huggingface.co/SZTAKI-HLT/hubert-base-cc).

## Intended uses & limitations

- **Model type:** Text Summarization
- **Language(s) (NLP):** Hungarian
- **Resource(s) for more information:**
  - [GitHub Repo](https://github.com/dorinapetra/summarization)
 
## Parameters

- **Batch Size:** 13
- **Learning Rate:** 5e-5
- **Weight Decay:** 0.01
- **Warmup Steps:** 16000
- **Epochs:** 15
- **no_repeat_ngram_size:** 3
- **num_beams:** 5
- **early_stopping:** True

## Results

| Metric        | Value                                       |
| :------------ | :------------------------------------------ |
| ROUGE-1       | 28.52                                       |
| ROUGE-2       | 10.35                                       |
| ROUGE-L       | 20.07                                       |

## Citation

If you use our model, please cite the following paper:
```
@inproceedings {HunSum-1,
    title = {{HunSum-1: an Abstractive Summarization Dataset for Hungarian}},
	booktitle = {XIX. Magyar Számítógépes Nyelvészeti Konferencia (MSZNY 2023)},
	year = {2023},
	publisher = {Szegedi Tudományegyetem, Informatikai Intézet},
	address = {Szeged, Magyarország},
	author = {Barta, Botond and Lakatos, Dorina and Nagy, Attila and Nyist, Mil{\'{a}}n Konor and {\'{A}}cs, Judit},
	pages = {231--243}
}
```
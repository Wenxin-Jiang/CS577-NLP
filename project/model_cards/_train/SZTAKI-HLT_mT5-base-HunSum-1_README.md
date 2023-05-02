---
language:
- hu
pipeline_tag: summarization
inference:
  parameters:
    num_beams: 5
    length_penalty: 2
    max_length: 128
    encoder_no_repeat_ngram_size: 4
    no_repeat_ngram_size: 3
datasets:
- SZTAKI-HLT/HunSum-1
metrics:
- rouge
license: apache-2.0
---

# Model Card for mT5-base-HunSum-1

The mT5-base-HunSum-1 is a Hungarian abstractive summarization model, which was trained on the [SZTAKI-HLT/HunSum-1 dataset](https://huggingface.co/datasets/SZTAKI-HLT/HunSum-1).
The model is based on [google/mt5-base](https://huggingface.co/google/mt5-base).

## Intended uses & limitations

- **Model type:** Text Summarization
- **Language(s) (NLP):** Hungarian
- **Resource(s) for more information:**
  - [GitHub Repo](https://github.com/dorinapetra/summarization)
 
## Parameters

- **Batch Size:** 12
- **Learning Rate:** 5e-5
- **Weight Decay:** 0.01
- **Warmup Steps:** 3000
- **Epochs:** 10
- **no_repeat_ngram_size:** 3
- **num_beams:** 5
- **early_stopping:** False
- **encoder_no_repeat_ngram_size:** 4

## Results

| Metric        | Value                                       |
| :------------ | :------------------------------------------ |
| ROUGE-1       | 37.70                                       |
| ROUGE-2       | 11.22                                       |
| ROUGE-L       | 24.37                                       |

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
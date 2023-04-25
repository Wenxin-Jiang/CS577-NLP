---
language: en
license: unlicense  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: pytorch  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
tags:
- onxx  # Example: audio
- ner  # Example: automatic-speech-recognition
- nlp  # Example: speech
- pytorch  # Example to specify a library: allennlp
- token-classification  # Example to specify a library: allennlp
datasets:
- conll2003  # Example: common_voice. Use dataset id from https://hf.co/datasets
metrics:
- evaluate-metric/accuracy  # Example: wer. Use metric id from https://hf.co/metrics
widget:
- text: "Jens Peter Hansen kommer fra Danmark"
# Optional. Add this if you want to encode your eval results in a structured way.
model-index:
- name: quantized_distilbert_conll2003_static
  results:
  - task:
      type: token-classification             # Required. Example: automatic-speech-recognition
      name: NER             # Optional. Example: Speech Recognition
    dataset:
      type: conll2003          # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: CONLL 2003          # Required. A pretty name for the dataset. Example: Common Voice (French)
    metrics:
      - type: evaluate-metric/accuracy         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 0.9839570110198201       # Required. Example: 20.90
      - type: evaluate-metric/recall         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 0.9180410636149444       # Required. Example: 20.90
      - type: evaluate-metric/f1         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 0.9053190606588665       # Required. Example: 20.90
      - type: evaluate-metric/precision         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 0.8929448354886234       # Required. Example: 20.90
---

| Feature | Description |
| --- | --- |
| **Name** | `quantized_distilbert_conll2003_static` |
| **Version** | `0.0.0` |

### Label Scheme

<details>

<summary>View label scheme (4 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `LOC`, `MISC`, `ORG`, `PER` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `accuracy` | 98.39 |
| `f1` | 90.53 |
| `precision` | 89.29 |
| `recall` | 91.80 |
---
license: apache-2.0
language:
- en
tags:
- text-generation
- text2text-generation
pipeline_tag: text2text-generation
widget:
- text: "Describe the following data: Iron Man | instance of | Superhero [SEP] Stan Lee | creator | Iron Man"
  example_title: "Example1"
- text: "Describe the following data: First Clearing | LOCATION | On NYS 52 1 Mi. Youngsville [SEP] On NYS 52 1 Mi. Youngsville | CITY_OR_TOWN | Callicoon, New York"
  example_title: "Example2"
---

# MTL-data-to-text
The MTL-data-to-text model was proposed in [**MVP: Multi-task Supervised Pre-training for Natural Language Generation**](https://arxiv.org/abs/2206.12131) by Tianyi Tang, Junyi Li, Wayne Xin Zhao and Ji-Rong Wen.

The detailed information and instructions can be found [https://github.com/RUCAIBox/MVP](https://github.com/RUCAIBox/MVP).

## Model Description
MTL-data-to-text is supervised pre-trained using a mixture of labeled data-to-text datasets. It is a variant (Single) of our main [MVP](https://huggingface.co/RUCAIBox/mvp) model. It follows a standard Transformer encoder-decoder architecture.

MTL-data-to-text is specially designed for data-to-text generation tasks, such as KG-to-text generation (WebNLG, DART), table-to-text generation (WikiBio, ToTTo) and MR-to-text generation (E2E).

## Example
```python
>>> from transformers import MvpTokenizer, MvpForConditionalGeneration

>>> tokenizer = MvpTokenizer.from_pretrained("RUCAIBox/mvp")
>>> model = MvpForConditionalGeneration.from_pretrained("RUCAIBox/mtl-data-to-text")

>>> inputs = tokenizer(
...     "Describe the following data: Iron Man | instance of | Superhero [SEP] Stan Lee | creator | Iron Man",
...     return_tensors="pt",
... )
>>> generated_ids = model.generate(**inputs)
>>> tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
['Iron Man is a fictional superhero appearing in American comic books published by Marvel Comics.']
```

## Related Models
**MVP**: [https://huggingface.co/RUCAIBox/mvp](https://huggingface.co/RUCAIBox/mvp).

**Prompt-based models**:

- MVP-multi-task: [https://huggingface.co/RUCAIBox/mvp-multi-task](https://huggingface.co/RUCAIBox/mvp-multi-task).
- MVP-summarization: [https://huggingface.co/RUCAIBox/mvp-summarization](https://huggingface.co/RUCAIBox/mvp-summarization).
- MVP-open-dialog: [https://huggingface.co/RUCAIBox/mvp-open-dialog](https://huggingface.co/RUCAIBox/mvp-open-dialog).
- MVP-data-to-text: [https://huggingface.co/RUCAIBox/mvp-data-to-text](https://huggingface.co/RUCAIBox/mvp-data-to-text).
- MVP-story: [https://huggingface.co/RUCAIBox/mvp-story](https://huggingface.co/RUCAIBox/mvp-story).
- MVP-question-answering: [https://huggingface.co/RUCAIBox/mvp-question-answering](https://huggingface.co/RUCAIBox/mvp-question-answering).
- MVP-question-generation: [https://huggingface.co/RUCAIBox/mvp-question-generation](https://huggingface.co/RUCAIBox/mvp-question-generation).
- MVP-task-dialog: [https://huggingface.co/RUCAIBox/mvp-task-dialog](https://huggingface.co/RUCAIBox/mvp-task-dialog).

**Multi-task models**:
- MTL-summarization: [https://huggingface.co/RUCAIBox/mtl-summarization](https://huggingface.co/RUCAIBox/mtl-summarization).
- MTL-open-dialog: [https://huggingface.co/RUCAIBox/mtl-open-dialog](https://huggingface.co/RUCAIBox/mtl-open-dialog).
- MTL-data-to-text: [https://huggingface.co/RUCAIBox/mtl-data-to-text](https://huggingface.co/RUCAIBox/mtl-data-to-text).
- MTL-story: [https://huggingface.co/RUCAIBox/mtl-story](https://huggingface.co/RUCAIBox/mtl-story).
- MTL-question-answering: [https://huggingface.co/RUCAIBox/mtl-question-answering](https://huggingface.co/RUCAIBox/mtl-question-answering).
- MTL-question-generation: [https://huggingface.co/RUCAIBox/mtl-question-generation](https://huggingface.co/RUCAIBox/mtl-question-generation).
- MTL-task-dialog: [https://huggingface.co/RUCAIBox/mtl-task-dialog](https://huggingface.co/RUCAIBox/mtl-task-dialog).

## Citation
```bibtex
@article{tang2022mvp,
  title={MVP: Multi-task Supervised Pre-training for Natural Language Generation},
  author={Tang, Tianyi and Li, Junyi and Zhao, Wayne Xin and Wen, Ji-Rong},
  journal={arXiv preprint arXiv:2206.12131},
  year={2022},
  url={https://arxiv.org/abs/2206.12131},
}
```

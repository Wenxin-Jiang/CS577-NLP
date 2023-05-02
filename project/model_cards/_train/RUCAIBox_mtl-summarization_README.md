---
license: apache-2.0
language:
- en
tags:
- text-generation
- text2text-generation
- summarization
pipeline_tag: text2text-generation
widget:
- text: "Summarize: You may want to stick it to your boss and leave your job, but don't do it if these are your reasons."
  example_title: "Example1"
- text: "Summarize: Jorge Alfaro drove in two runs, Aaron Nola pitched seven innings of two-hit ball and the Philadelphia Phillies beat the Los Angeles Dodgers 2-1 Thursday, spoiling Clayton Kershaw's first start in almost a month. Hitting out of the No. 8 spot in the ..."
  example_title: "Example2"
---

# MTL-summarization
The MTL-summarization model was proposed in [**MVP: Multi-task Supervised Pre-training for Natural Language Generation**](https://arxiv.org/abs/2206.12131) by Tianyi Tang, Junyi Li, Wayne Xin Zhao and Ji-Rong Wen.

The detailed information and instructions can be found [https://github.com/RUCAIBox/MVP](https://github.com/RUCAIBox/MVP).

## Model Description
MTL-summarization is supervised pre-trained using a mixture of labeled summarization datasets. It is a variant (Single) of our main [MVP](https://huggingface.co/RUCAIBox/mvp) model. It follows a standard Transformer encoder-decoder architecture.

MTL-summarization is specially designed for summarization tasks, such as new summarization (CNN/DailyMail, XSum) and dialog summarization (SAMSum).

## Example
```python
>>> from transformers import MvpTokenizer, MvpForConditionalGeneration

>>> tokenizer = MvpTokenizer.from_pretrained("RUCAIBox/mvp")
>>> model = MvpForConditionalGeneration.from_pretrained("RUCAIBox/mtl-summarization")

>>> inputs = tokenizer(
...     "Summarize: You may want to stick it to your boss and leave your job, but don't do it if these are your reasons.",
...     return_tensors="pt",
... )
>>> generated_ids = model.generate(**inputs)
>>> tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
["Don't do it if these are your reasons"]
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

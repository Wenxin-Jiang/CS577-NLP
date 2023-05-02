---
license: apache-2.0
language:
- en
tags:
- text-generation
- text2text-generation
pipeline_tag: text2text-generation
widget:
- text: "Given the story title: I think all public schools should have a uniform dress code."
  example_title: "Example1"
- text: "Given the story title: My girlfriend and I decided to move to a new state. We packed everything in our cars and drove there."
  example_title: "Example2"
---

# MVP-story
The MVP-story model was proposed in [**MVP: Multi-task Supervised Pre-training for Natural Language Generation**](https://arxiv.org/abs/2206.12131) by Tianyi Tang, Junyi Li, Wayne Xin Zhao and Ji-Rong Wen.

The detailed information and instructions can be found [https://github.com/RUCAIBox/MVP](https://github.com/RUCAIBox/MVP).

## Model Description
MVP-story is a prompt-based model that MVP is further equipped with prompts pre-trained using labeled story generation datasets. It is a variant (MVP+S) of our main [MVP](https://huggingface.co/RUCAIBox/mvp) model. It follows a Transformer encoder-decoder architecture with layer-wise prompts.

MVP-story is specially designed for story generation tasks, such as ROCStories and WritingPrompts.

## Example
```python
>>> from transformers import MvpTokenizer, MvpForConditionalGeneration

>>> tokenizer = MvpTokenizer.from_pretrained("RUCAIBox/mvp")
>>> model = MvpForConditionalGeneration.from_pretrained("RUCAIBox/mvp-story")

>>> inputs = tokenizer(
...     "Given the story title: I think all public schools should have a uniform dress code.",
...     return_tensors="pt",
... )
>>> generated_ids = model.generate(**inputs, max_length=1024)
>>> tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
['I think it would be a good idea to have uniform dress codes for all public schools. It would make it easier for students to dress appropriately.']
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

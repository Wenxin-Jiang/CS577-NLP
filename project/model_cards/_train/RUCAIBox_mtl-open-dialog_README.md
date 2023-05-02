---
license: apache-2.0
language:
- en
tags:
- text-generation
- text2text-generation
- conversational
pipeline_tag: text2text-generation
widget:
- text: "Given the dialog: do you like dance? [SEP] Yes I do. Did you know Bruce Lee was a cha cha dancer?"
  example_title: "Example1"
- text: "Given the dialog: i used to scare for darkness [X_SEP] it feels like hitting to blank wall when i see the darkness [SEP] Oh ya? I don't really see how [SEP] dont you feel so.. its a wonder [SEP] I do actually hit blank walls a lot of times but i get by"
  example_title: "Example2"
---

# MTL-open-dialog
The MTL-open-dialog model was proposed in [**MVP: Multi-task Supervised Pre-training for Natural Language Generation**](https://arxiv.org/abs/2206.12131) by Tianyi Tang, Junyi Li, Wayne Xin Zhao and Ji-Rong Wen.

The detailed information and instructions can be found [https://github.com/RUCAIBox/MVP](https://github.com/RUCAIBox/MVP).

## Model Description
MTL-open-dialog is supervised pre-trained using a mixture of labeled open dialogue system datasets. It is a variant (Single) of our main [MVP](https://huggingface.co/RUCAIBox/mvp) model. It follows a standard Transformer encoder-decoder architecture.

MTL-open-dialog is specially designed for open dialogue system (conversation) tasks, such as chitchat (PersonaChat, DailyDialog), knowledge grounded conversation (Topical-Chat, Wizard of Wikipedia) and visual dialog (DSTC7-AVSD).

## Example
```python
>>> from transformers import MvpTokenizer, MvpForConditionalGeneration

>>> tokenizer = MvpTokenizer.from_pretrained("RUCAIBox/mvp")
>>> model = MvpForConditionalGeneration.from_pretrained("RUCAIBox/mtl-open-dialog")

>>> inputs = tokenizer(
...     "Given the dialog: do you like dance? [SEP] Yes I do. Did you know Bruce Lee was a cha cha dancer?",
...     return_tensors="pt",
... )
>>> generated_ids = model.generate(**inputs)
>>> tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
['Yes he won the Hong Kong Cha Cha championship in 1958']
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

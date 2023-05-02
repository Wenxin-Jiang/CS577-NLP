---
language: 
  - zh
license: apache-2.0
widget:
- text: "“房间很一般，小，且让人感觉脏，隔音效果差，能听到走廊的人讲话，走廊光线昏暗，旁边没有什么可吃” 这条评论的态度是什么？"
---

# Mengzi-T5-MT model
This is a Multi-Task model trained on the multitask mixture of 27 datasets and 301 prompts, based on [Mengzi-T5-base](https://huggingface.co/Langboat/mengzi-t5-base).

[Mengzi: Towards Lightweight yet Ingenious Pre-trained Models for Chinese](https://arxiv.org/abs/2110.06696)

## Usage
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration
tokenizer = T5Tokenizer.from_pretrained("Langboat/mengzi-t5-base-mt")
model = T5ForConditionalGeneration.from_pretrained("Langboat/mengzi-t5-base-mt")
```

## Citation
If you find the technical report or resource is useful, please cite the following technical report in your paper.
```
@misc{zhang2021mengzi,
      title={Mengzi: Towards Lightweight yet Ingenious Pre-trained Models for Chinese}, 
      author={Zhuosheng Zhang and Hanqing Zhang and Keming Chen and Yuhang Guo and Jingyun Hua and Yulong Wang and Ming Zhou},
      year={2021},
      eprint={2110.06696},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
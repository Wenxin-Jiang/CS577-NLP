---
license: bsd-3-clause
tags:
- codet5
datasets:
- code_search_net
inference: true
---

# CodeT5-base for Code Summarization

[CodeT5-base](https://huggingface.co/Salesforce/codet5-base) model fine-tuned on CodeSearchNet data in a multi-lingual training setting (
Ruby/JavaScript/Go/Python/Java/PHP) for code summarization. It was introduced in this EMNLP 2021
paper [CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation](https://arxiv.org/abs/2109.00859)
by Yue Wang, Weishi Wang, Shafiq Joty, Steven C.H. Hoi. Please check out more
at [this repository](https://github.com/salesforce/CodeT5).

## How to use

Here is how to use this model:

```python
from transformers import RobertaTokenizer, T5ForConditionalGeneration

if __name__ == '__main__':
    tokenizer = RobertaTokenizer.from_pretrained('Salesforce/codet5-base-multi-sum')
    model = T5ForConditionalGeneration.from_pretrained('Salesforce/codet5-base-multi-sum')

    text = """def svg_to_image(string, size=None):
    if isinstance(string, unicode):
        string = string.encode('utf-8')
        renderer = QtSvg.QSvgRenderer(QtCore.QByteArray(string))
    if not renderer.isValid():
        raise ValueError('Invalid SVG data.')
    if size is None:
        size = renderer.defaultSize()
        image = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
        painter = QtGui.QPainter(image)
        renderer.render(painter)
    return image"""

    input_ids = tokenizer(text, return_tensors="pt").input_ids

    generated_ids = model.generate(input_ids, max_length=20)
    print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
    # this prints: "Convert a SVG string to a QImage."
```

## Fine-tuning data

We employ the filtered version of CodeSearchNet data [[Husain et al., 2019](https://arxiv.org/abs/1909.09436)]
from [CodeXGLUE](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Text/code-to-text) benchmark for fine-tuning on
code summarization. The data is tokenized with our pre-trained code-specific BPE (Byte-Pair Encoding) tokenizer. One can
prepare text (or code) for the model using RobertaTokenizer with the vocab files from [codet5-base](https://huggingface.co/Salesforce/codet5-base).

### Data statistic

| Programming Language | Training |  Dev   |  Test  |
| :------------------- | :------: | :----: | :----: |
| Python               | 251,820  | 13,914 | 14,918 |
| PHP                  | 241,241  | 12,982 | 14,014 |
| Go                   | 167,288  | 7,325  | 8,122  |
| Java                 | 164,923  | 5,183  | 10,955 |
| JavaScript           |  58,025  | 3,885  | 3,291  |
| Ruby                 |  24,927  | 1,400  | 1,261  |

## Training procedure

We fine-tune codet5-base on these six programming languages (Ruby/JavaScript/Go/Python/Java/PHP) in the multi-task learning setting. We employ the
balanced sampling to avoid biasing towards high-resource tasks. Please refer to the [paper](https://arxiv.org/abs/2109.00859) for more details.

## Evaluation results

Unlike the paper allowing to select different best checkpoints for different programming languages (PLs), here we employ one checkpoint for
all PLs. Besides, we remove the task control prefix to specify the PL in training and inference. The results on the test set are shown as below:

| Model       |   Ruby    | Javascript |    Go     |  Python   |   Java    |    PHP    |  Overall  |
| ----------- | :-------: | :--------: | :-------: | :-------: | :-------: | :-------: | :-------: |
| Seq2Seq     |   9.64    |   10.21    |   13.98   |   15.93   |   15.09   |   21.08   |   14.32   |
| Transformer |   11.18   |   11.59    |   16.38   |   15.81   |   16.26   |   22.12   |   15.56   |
| [RoBERTa](https://arxiv.org/pdf/1907.11692.pdf)     |   11.17   |   11.90    |   17.72   |   18.14   |   16.47   |   24.02   |   16.57   |
| [CodeBERT](https://arxiv.org/pdf/2002.08155.pdf)    | 12.16 | 14.90  | 18.07 | 19.06 | 17.65 | 25.16 | 17.83 |
| [PLBART](https://aclanthology.org/2021.naacl-main.211.pdf)    | 14.11 |15.56  |  18.91 |   19.30 |  18.45 |  23.58 |  18.32 | 
| [CodeT5-small](https://arxiv.org/abs/2109.00859)    |14.87    | 15.32   |  19.25    | 20.04   |  19.92   |  25.46   |  19.14 | 
| [CodeT5-base](https://arxiv.org/abs/2109.00859)    |  **15.24**   |  16.16   |  19.56   |  20.01   |  **20.31**   |  26.03   |  19.55 | 
| [CodeT5-base-multi-sum](https://arxiv.org/abs/2109.00859)    | **15.24**  | **16.18**  | **19.95**   |   **20.42**    | 20.26  | **26.10**  |  **19.69** | 

## Citation

```bibtex
@inproceedings{
    wang2021codet5,
    title={CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation}, 
    author={Yue Wang, Weishi Wang, Shafiq Joty, Steven C.H. Hoi},
    booktitle={Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, EMNLP 2021},
    year={2021},
}
```
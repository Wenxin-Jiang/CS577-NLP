---
language: 
  - zh

inference: 
  parameters:
    top_p: 0.9
    max_new_tokens: 128
    num_return_sequences: 3
    do_sample: true
    repetition_penalty: 1.1

license: apache-2.0
tags:
- generate
- gpt2

widget:
- 北京是中国的
- 西湖的景色

---

# Wenzhong2.0-GPT2-110M-BertTokenizer-chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

善于处理NLG任务，中文版的GPT2-Small。基于BertTokenizer，实现字级别token，更便于受控文本生成。

Focused on handling NLG tasks, Chinese GPT2-Small.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General  | 自然语言生成 NLG | 闻仲 Wenzhong | GPT2 |      110M      |     中文 Chinese     |

## 模型信息 Model Information

类似于Wenzhong2.0-GPT2-3.5B-chinese，我们实现了一个small版本的12层的Wenzhong2.0-GPT2-110M-BertTokenizer-chinese，并在悟道（300G版本）上面进行预训练。本次开源别于之前开源的闻仲-GPT2系列，主要在于将BPE的分词换成了BertTokenzier的字级别分词。

Similar to Wenzhong2.0-GPT2-3.5B-chinese, we implement a small size Wenzhong2.0-GPT2-110M-BertTokenizer-chinese with 12 layers, which is pre-trained on Wudao Corpus (300G version).This open source version is different from the previous open source Wenzhong-GPT2 series, mainly because the word segmentation of BPE is replaced by the word level word segmentation of BertTokenzier.

## 使用 Usage

### 加载模型 Loading Models

```python 
from transformers import BertTokenizer,GPT2LMHeadModel
hf_model_path = 'IDEA-CCNL/Wenzhong-GPT2-110M'
tokenizer = BertTokenizer.from_pretrained(hf_model_path)
model = GPT2LMHeadModel.from_pretrained(hf_model_path)
```

### 使用示例 Usage Examples

这里需要提一点，GPT在训练的时候是没有添加special_tokens的，BertTokenizer会默认补充special_tokens，所以在tokenzier的时候需要将add_special_tokens设置为false，这样生产效果会更好。

```python
def generate_word_level(input_text,n_return=5,max_length=128,top_p=0.9):
    inputs = tokenizer(input_text,return_tensors='pt',add_special_tokens=False).to(model.device)
    gen = model.generate(
                            inputs=inputs['input_ids'],
                            max_length=max_length,
                            do_sample=True,
                            top_p=top_p,
                            eos_token_id=21133,
                            pad_token_id=0,
                            num_return_sequences=n_return)

    sentences = tokenizer.batch_decode(gen)
    for idx,sentence in enumerate(sentences):
        print(f'sentence {idx}: {sentence}')
        print('*'*20)
    return gen

outputs = generate_word_level('西湖的景色',n_return=5,max_length=128)
```

## 引用 Citation

如果您在您的工作中使用了我们的模型，可以引用我们的[论文](https://arxiv.org/abs/2209.02970)：

If you are using the resource for your work, please cite the our [paper](https://arxiv.org/abs/2209.02970):

```text
@article{fengshenbang,
  author    = {Jiaxing Zhang and Ruyi Gan and Junjie Wang and Yuxiang Zhang and Lin Zhang and Ping Yang and Xinyu Gao and Ziwei Wu and Xiaoqun Dong and Junqing He and Jianheng Zhuo and Qi Yang and Yongfeng Huang and Xiayu Li and Yanghan Wu and Junyu Lu and Xinyu Zhu and Weifeng Chen and Ting Han and Kunhao Pan and Rui Wang and Hao Wang and Xiaojun Wu and Zhongshen Zeng and Chongpei Chen},
  title     = {Fengshenbang 1.0: Being the Foundation of Chinese Cognitive Intelligence},
  journal   = {CoRR},
  volume    = {abs/2209.02970},
  year      = {2022}
}
```

也可以引用我们的[网站](https://github.com/IDEA-CCNL/Fengshenbang-LM/):

You can also cite our [website](https://github.com/IDEA-CCNL/Fengshenbang-LM/):

```text
@misc{Fengshenbang-LM,
  title={Fengshenbang-LM},
  author={IDEA-CCNL},
  year={2021},
  howpublished={\url{https://github.com/IDEA-CCNL/Fengshenbang-LM}},
}
```

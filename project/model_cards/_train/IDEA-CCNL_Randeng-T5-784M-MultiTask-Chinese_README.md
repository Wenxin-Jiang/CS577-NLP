---
license: apache-2.0
language: zh
tags:
- Text2Text Generation
- T5
- chinese
- sentencepiece
inference: true
widget:
- text: "新闻分类任务：【微软披露拓扑量子计算机计划！】这篇文章的类别是什么？故事/文化/娱乐/体育/财经/房产/汽车/教育/科技"
- type: "text-generation"
---

# Randeng-T5-784M-MultiTask-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

在Randeng-T5-784M的基础上，收集了100个左右的中文数据集，进行Text2Text统一范式的有监督任务预训练。

On the basis of Randeng-T5-784M, about 100 Chinese datasets were collected and pre-trained for the supervised task of Text2Text unified paradigm.

本模型在中文zero-shot榜单ZeroClue上取得了第三名（不包括人类）的成绩，在所有基于T5（encoder-decoder架构）的模型中排名第一。

This model achieved the 3rd place (excluding humans) on the Chinese zero-shot benchmark ZeroClue, ranking first among all models based on T5 (encoder-decoder architecture).

![截图于Screenshot taken on 2022.12.01](zeroclue.png)

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General | 自然语言转换 NLT | 燃灯 Randeng | MultiTask |      784M      |    多任务-中文 MultiTask-Chinese    |


## 模型信息 Model Information

参考论文：[Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](http://jmlr.org/papers/v21/20-074.html)

基于[Randeng-T5-784M](https://huggingface.co/IDEA-CCNL/Randeng-T5-784M)，我们在收集的100+个中文领域的多任务数据集（从中采样了30w+个样本）上微调了它，得到了此多任务版本。这些多任务包括：情感分析，新闻分类，文本分类，意图识别，自然语言推理，多项选择，指代消解，抽取式阅读理解，实体识别，关键词抽取，生成式摘要。

Based on [Randeng-T5-784M](https://huggingface.co/IDEA-CCNL/Randeng-T5-784M), we fine-tuned it on a collection of 100+ multitasking datasets in Chinese domains (from which 30w+ samples were sampled) to obtain this multitasking version. These multitasks include: sentiment analysis, news classification, text classification, intention recognition, natural language inference, multiple choice, denotational disambiguation, extractive reading comprehension, entity recognition, keyword extraction, and generative summarization.


## 使用 Usage

```python
import torch
from transformers import T5Tokenizer, T5Config, T5ForConditionalGeneration

# load tokenizer and model 
pretrained_model = "IDEA-CCNL/Randeng-T5-784M-MultiTask-Chinese"

special_tokens = ["<extra_id_{}>".format(i) for i in range(100)]
tokenizer = T5Tokenizer.from_pretrained(
    pretrained_model,
    do_lower_case=True,
    max_length=512,
    truncation=True,
    additional_special_tokens=special_tokens,
)
config = T5Config.from_pretrained(pretrained_model)
model = T5ForConditionalGeneration.from_pretrained(pretrained_model, config=config)
model.resize_token_embeddings(len(tokenizer))
model.eval()

# tokenize
text = "新闻分类任务：【微软披露拓扑量子计算机计划！】这篇文章的类别是什么？故事/文化/娱乐/体育/财经/房产/汽车/教育/科技"
encode_dict = tokenizer(text, max_length=512, padding='max_length',truncation=True)

inputs = {
  "input_ids": torch.tensor([encode_dict['input_ids']]).long(),
  "attention_mask": torch.tensor([encode_dict['attention_mask']]).long(),
  }

# generate answer
logits = model.generate(
  input_ids = inputs['input_ids'],
  max_length=100, 
  do_sample= True
  # early_stopping=True,
  )

logits=logits[:,1:]
predict_label = [tokenizer.decode(i,skip_special_tokens=True) for i in logits]
print(predict_label)

# model output: 科技
```

除了分类任务，其他任务的数据构造例子如下：

In addition to classification tasks, data construction examples of other tasks are as follows:

```python
example_dict={
    "文本分类":{"text_a":"钢琴块3别踩白块儿3钢琴块3是一款简洁的钢琴模拟软件,在Android平台上,类似的软件还是比较多的。","choices":["相机","影视娱乐","棋牌中心","新闻","财经","策略","休闲益智","教育"]},
    '新闻分类':{"text_a":"微软披露拓扑量子计算机计划！","choices":["故事","文化","娱乐","体育","财经","房产","汽车","教育","科技"]},
    '情感分析':{"text_a":"刚买iphone13 pro 还不到一个月，天天死机最差的一次购物体验","choices":["好评","差评"]},
    '意图识别':{"text_a":"打电话给吴小军。","choices":["放音乐","播放下一首","打电话","退出导航","开始导航","其他","暂停音乐","导航","开导航"]},

    '语义匹配':{"text_a":"今天心情不好","text_b":"我很不开心","choices":["相似","不相似"]},
    '自然语言推理':{"text_a":"小明正在上高中","text_b":"小明是一个初中生","choices":["无关","矛盾","蕴含"]},

    '多项选择':{"text_a":"这大家千万不能着急，我们现在只是暂时输了7分。距离比赛结束还有20多分钟呢，我们是完全有机会转败为赢的，大家加油!","question":"说话人希望大家：","choices":["别得意","冷静一些","加快速度","提前预习"]},
    '指代消解':{"text_a":"李鸣觉得董客这人，踏实得叫人难受。可因为孟野和森森太疯，他只好去找董客聊天，但在董客眼里，李鸣也是不正常，他竟然放着现成的大学不愿上。","question":"【他】指的是【李鸣】吗？","choices":["是","不是"]},

    '实体识别':{"text_a":"北京大学是我国的一座历史名校，坐落在海淀区，蔡元培曾经担任校长","question":"机构"},
    '抽取式阅读理解':{"text_a":"《H》正式定档3月7日下午两点整在京东商城独家平台开启第一批5000份预售,定价230元人民币,回馈最忠实的火星歌迷,意在用精品回馈三年来跟随华晨宇音乐不离不弃的粉丝们的支持与厚爱","question":"华晨宇专辑h预售价格是多少？"},
    '关键词抽取':{"text_a":"今儿在大众点评，找到了口碑不错的老茶故事私房菜。"},
    '关键词识别':{"text_a":"今儿在大众点评，找到了口碑不错的老茶故事私房菜。","question":"请问这篇文章的关键词是大众点评、老茶私房菜吗？,"choices":["是","不是"]}

    "生成式摘要":{"text_a":"针对传统的流量分类管理系统存在不稳定、结果反馈不及时、分类结果显示不直观等问题,设计一个基于web的在线的流量分类管理系统.该系统采用流中前5个包(排除3次握手包)所含信息作为特征值计算资源,集成一种或多种分类算法用于在线网络流量分类,应用数据可视化技术处理分类结果.实验表明:在采用适应在线分类的特征集和c4.5决策树算法做分类时,系统能快速做出分类,且精度达到94％以上;数据可视化有助于人机交互,改善分类指导."}
}

# 构造prompt的过程中，verbalizer这个占位key的内容，是通过 "/".join(choices) 拼接起来
dataset2instruction = {
    "情感分析": {
        "prompt": "{}任务：【{}】这篇文章的情感态度是什么？{}",
        "keys_order": ["subtask_type","text_a", "verbalizer"],
        "data_type": "classification",
    },
    "文本分类": {
        "prompt": "{}任务：【{}】这篇文章的类别是什么？{}",
        "keys_order": ["subtask_type","text_a", "verbalizer"],
        "data_type": "classification",
    },
    "新闻分类": {
        "prompt": "{}任务：【{}】这篇文章的类别是什么？{}",
        "keys_order": ["subtask_type","text_a", "verbalizer"],
        "data_type": "classification",
    },
    "意图识别": {
        "prompt": "{}任务：【{}】这句话的意图是什么？{}",
        "keys_order": ["subtask_type","text_a", "verbalizer"],
        "data_type": "classification",
    },
# --------------------
    "自然语言推理": {
        "prompt": "{}任务：【{}】和【{}】，以上两句话的逻辑关系是什么？{}",
        "keys_order": ["subtask_type","text_a", "text_b", "verbalizer"],
        "data_type": "classification",
    },
    "语义匹配": {
        "prompt": "{}任务：【{}】和【{}】，以上两句话的内容是否相似？{}",
        "keys_order": ["subtask_type","text_a", "text_b", "verbalizer"],
        "data_type": "classification",
    },
# -----------------------
    "指代消解": {
        "prompt": "{}任务：文章【{}】中{}{}",
        "keys_order": ["subtask_type","text_a", "question", "verbalizer"],
        "data_type": "classification",
    },
    "多项选择": {
        "prompt": "{}任务：阅读文章【{}】问题【{}】？{}",
        "keys_order": ["subtask_type","text_a", "question", "verbalizer"],
        "data_type": "classification",
    },
# ------------------------
    "抽取式阅读理解": {
        "prompt": "{}任务：阅读文章【{}】问题【{}】的答案是什么？",
        "keys_order": ["subtask_type","text_a", "question"],
        "data_type": "mrc",
    },
    "实体识别": {
        "prompt": "{}任务：找出【{}】这篇文章中所有【{}】类型的实体？",
        "keys_order": ["subtask_type","text_a", "question"],
        "data_type": "ner",
    },
# ------------------------
    "关键词抽取": {
        "prompt": "{}任务：【{}】这篇文章的关键词是什么？",
        "keys_order": ["subtask_type","text_a"],
        "data_type": "keys",
    },
    "关键词识别":{
        "prompt": "{}任务：阅读文章【{}】问题【{}】{}",
        "keys_order": ["subtask_type","text_a","question","verbalizer"],
        "data_type": "classification",
    },
    "生成式摘要": {
        "prompt": "{}任务：【{}】这篇文章的摘要是什么？",
        "keys_order": ["subtask_type","text_a"],
        "data_type": "summ",
    }, 
}

def get_instruction(sample):

    template = dataset2instruction[sample["subtask_type"]]
    # print(template)
    # print(sample)
    sample["instruction"] = template["prompt"].format(*[
                sample[k] for k in template["keys_order"]
            ])

    print(sample["instruction"])
    
    return sample["instruction"]
```

## 预训练或微调 prtrain or finetune
如果您对于怎么预训练Randeng-T5模型或者想在自己的下游任务中微调Randeng模型，欢迎使用[Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM/)项目，这里提供了完整的示例：
- [预训练](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/pretrain_t5)
- [微调](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/mt5_summary)

If you want to pre train the Randeng T5 model or fine tune the Randeng model in your downstream tasks, welcome to use [Fengshenbang LM]（ https://github.com/IDEA-CCNL/Fengshenbang-LM/ ）A complete example of the project is provided here:

- [Pre training](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/pretrain_t5)
- [Fine tune](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/mt5_summary)

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
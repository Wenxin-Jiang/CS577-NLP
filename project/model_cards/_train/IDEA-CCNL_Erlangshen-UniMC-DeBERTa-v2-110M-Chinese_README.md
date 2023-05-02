---
license: apache-2.0
# inference: true

# inference:
#   parameters:
tags:
- classification
- zero-shot
---

# Erlangshen-UniMC-DeBERTa-v2-110M-Chinese

- Main Page:[Fengshenbang](https://fengshenbang-lm.com/)
- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/unimc/)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)
- API: [Fengshen-OpenAPI](https://fengshenbang-lm.com/open-api)

## 简介 Brief Introduction

UniMC 核心思想是将自然语言理解任务转化为 multiple choice 任务，并且使用多个 NLU 任务来进行预训练。我们在英文数据集实验结果表明仅含有 2.35 亿参数的 [ALBERT模型](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-Albert-235M-English)的zero-shot性能可以超越众多千亿的模型。并在中文测评基准 FewCLUE 和 ZeroCLUE 两个榜单中，13亿的[二郎神](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-MegatronBERT-1.3B-Chinese)获得了第一的成绩。

The core idea of UniMC is to convert natural language understanding tasks into multiple choice tasks and use multiple NLU tasks for pre-training. Our experimental results on the English dataset show that the zero-shot performance of a [ALBERT](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-Albert-235M-English) model with only 235 million parameters can surpass that of many hundreds of billions of models. And in the Chinese evaluation benchmarks FewCLUE and ZeroCLUE two lists, 1.3 billion [Erlangshen](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-MegatronBERT-1.3B-Chinese) won the first result.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General | 自然语言理解 NLU | 二郎神 Erlangshen | DeBERTa-v2 |     110M    |     Chinese     |

## 模型信息 Model Information

我们为零样本学习者提出了一种与输入无关的新范式，从某种意义上说，它与任何格式兼容并适用于一系列语言任务，例如文本分类、常识推理、共指解析、情感分析。我们的方法将零样本学习转化为多项选择任务，避免常用的大型生成模型（如 FLAN）中的问题。它不仅增加了模型的泛化能力，而且显着减少了对参数的需求。我们证明了这种方法可以在通用语言基准上取得最先进的性能，并在自然语言推理和文本分类等任务上产生令人满意的结果。更多详细信息可以参考我们的[论文](https://arxiv.org/abs/2210.08590)或者[GitHub](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/unimc/)

We propose an new paradigm for zero-shot learners that is input-agnostic, in the sense that  it is compatible with any format and applicable to a list of language tasks, such as text classification, commonsense  reasoning, coreference resolution, sentiment analysis.
Our approach converts zero-shot learning into multiple choice tasks, 
avoiding problems in commonly used large generative models such as FLAN. It not only adds generalization ability to the models, but also reduces the needs of parameters significantly. We demonstrate that this approach leads to state-of-the-art performance on common language benchmarks, and produces satisfactory results on tasks such as natural language inference and text classification. For more details, please refer to our [paper](https://arxiv.org/abs/2210.08590) or [github](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/unimc/)

### 下游效果 Performance

我们使用全量数据测评我们的模型性能，并与 RoBERTa 进行对比

We use full data to evaluate our model performance and compare it with RoBERTa

| Model      | afqmc    | tnews   | iflytek     | ocnli  |
|------------|------------|----------|-----------|----------|
| RoBERTa-110M | 74.06       | 57.5     | 60.36        | 74.3     |
| RoBERTa-330M | 74.88       | 58.79     | 61.52      | 77.77       |
| [Erlangshen-UniMC-DeBERTa-v2-110M-Chinese](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-DeBERTa-v2-110M-Chinese/)     | 74.49       | 57.28     | 61.42        | 76.98     |
| [Erlangshen-UniMC-DeBERTa-v2-330M-Chinese](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-DeBERTa-v2-330M-Chinese/)    | **76.16**       | 58.61       | -      | **81.86** | 



## 使用 Usage
```shell
git clone https://github.com/IDEA-CCNL/Fengshenbang-LM.git
cd Fengshenbang-LM
pip install --editable .
```


```python3
import argparse
from fengshen.pipelines.multiplechoice import UniMCPipelines


total_parser = argparse.ArgumentParser("TASK NAME")
total_parser = UniMCPipelines.piplines_args(total_parser)
args = total_parser.parse_args()
pretrained_model_path = 'IDEA-CCNL/Erlangshen-UniMC-DeBERTa-v2-110M-Chinese'
args.learning_rate=2e-5
args.max_length=512
args.max_epochs=3
args.batchsize=8
args.default_root_dir='./'
model = UniMCPipelines(args, pretrained_model_path)

train_data = []
dev_data = []
test_data = [
        {"texta": "放弃了途观L和荣威RX5，果断入手这部车，外观霸气又好开", 
         "textb": "", 
         "question": "下面新闻属于哪一个类别？", 
         "choice": [
            "房产", 
            "汽车", 
            "教育", 
            "科技"
            ], 
         "answer": "汽车", 
         "label": 1, 
         "id": 7759}
    ]

if args.train:
    model.train(train_data, dev_data)
result = model.predict(test_data)
for line in result[:20]:
    print(line)


```

## 引用 Citation

如果您在您的工作中使用了我们的模型，可以引用我们的[论文](https://arxiv.org/abs/2210.08590)：

If you are using the resource for your work, please cite the our [paper](https://arxiv.org/abs/2210.08590):

```text
@article{unimc,
  author    = {Ping Yang and
               Junjie Wang and
               Ruyi Gan and
               Xinyu Zhu and
               Lin Zhang and
               Ziwei Wu and
               Xinyu Gao and
               Jiaxing Zhang and
               Tetsuya Sakai},
  title     = {Zero-Shot Learners for Natural Language Understanding via a Unified Multiple Choice Perspective},
  journal   = {CoRR},
  volume    = {abs/2210.08590},
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
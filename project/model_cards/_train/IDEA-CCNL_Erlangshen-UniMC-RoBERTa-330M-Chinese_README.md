---
license: apache-2.0
# inference: false

# inference:
#   parameters:
tags:
- classification
- zero-shot
---

# Erlangshen-UniMC-RoBERTa-330M-Chinese

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
| 通用 General | 自然语言理解 NLU | 二郎神 Erlangshen | RoBERTa |     330M    |     Chinese     |

## 模型信息 Model Information

我们为零样本学习者提出了一种与输入无关的新范式，从某种意义上说，它与任何格式兼容并适用于一系列语言任务，例如文本分类、常识推理、共指解析、情感分析。我们的方法将零样本学习转化为多项选择任务，避免常用的大型生成模型（如 FLAN）中的问题。它不仅增加了模型的泛化能力，而且显着减少了对参数的需求。我们证明了这种方法可以在通用语言基准上取得最先进的性能，并在自然语言推理和文本分类等任务上产生令人满意的结果。更多详细信息可以参考我们的[论文](https://arxiv.org/abs/2210.08590)或者[GitHub](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/unimc/)

We propose an new paradigm for zero-shot learners that is input-agnostic, in the sense that  it is compatible with any format and applicable to a list of language tasks, such as text classification, commonsense  reasoning, coreference resolution, sentiment analysis.
Our approach converts zero-shot learning into multiple choice tasks, 
avoiding problems in commonly used large generative models such as FLAN. It not only adds generalization ability to the models, but also reduces the needs of parameters significantly. We demonstrate that this approach leads to state-of-the-art performance on common language benchmarks, and produces satisfactory results on tasks such as natural language inference and text classification. For more details, please refer to our [paper](https://arxiv.org/abs/2210.08590) or [github](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/unimc/)

### 下游效果 Performance


**Few-shot**
| Model      | eprstmt    | csldcp   | tnews     | iflytek  | ocnli     | bustm     | chid      | csl      | wsc       | Avg       |
|------------|------------|----------|-----------|----------|-----------|-----------|-----------|----------|-----------|-----------|
| [FineTuning](https://arxiv.org/pdf/2107.07498.pdf)-RoBERTa-110M  | 65.4       | 35.5     | 49        | 32.8     | 33        | 60.7      | 14.9      | 50       | 55.6      | 44.1      |
| [FineTuning](https://arxiv.org/pdf/2107.07498.pdf)-ERNIE1.0-110M | 66.5 | 57   | 516  | 42.1 | 32   | 60.4 | 15    | 60.1 | 50.3 | 48.34 |
| [PET](https://arxiv.org/pdf/2107.07498.pdf)-ERNIE1.0-110M        | 84   | 59.9 | 56.4 | 50.3 | 38.1 | 58.4 | 40.6  | 61.1 | 58.7 | 56.39 |
| [P-tuning](https://arxiv.org/pdf/2107.07498.pdf)-ERNIE1.0-110M   | 80.6 | 56.6 | 55.9 | 52.6 | 35.7 | 60.8 | 39.61 | 51.8 | 55.7 | 54.37 |
| [EFL](https://arxiv.org/pdf/2107.07498.pdf)-ERNIE1.0-110M        | 76.7 | 47.9 | 56.3 | 52.1 | 48.7 | 54.6 | 30.3  | 52.8 | 52.3 | 52.7  |
| [UniMC-RoBERTa-110M](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-RoBERTa-110M-Chinese) | 88.64      | 54.08    | 54.32     | 48.6     | 66.55     | 73.76     | 67.71     | 52.54    | 59.92     | 62.86     |
| [UniMC-RoBERTa-330M](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-RoBERTa-330M-Chinese) | 89.53      | 57.3     | 54.25     | 50       | 70.59     | 77.49     | 78.09     | 55.73    | 65.16     | 66.46     |
| [UniMC-MegatronBERT-1.3B](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-MegatronBERT-1.3B-Chinese) | **89.278** | **60.9** | **57.46** | 52.89    | **76.33** | **80.37** | **90.33** | 61.73    | **79.15** | **72.05** |

**Zero-shot**

| Model         | eprstmt   | csldcp    | tnews     | iflytek   | ocnli     | bustm    | chid     | csl      | wsc       | Avg       |
|---------------|-----------|-----------|-----------|-----------|-----------|----------|----------|----------|-----------|-----------|
| [GPT](https://arxiv.org/pdf/2107.07498.pdf)-110M      | 57.5      | 26.2      | 37        | 19        | 34.4      | 50       | 65.6     | 50.1     | 50.3      | 43.4      |
| [PET](https://arxiv.org/pdf/2107.07498.pdf)-RoBERTa-110M      | 85.2      | 12.6      | 26.1      | 26.6      | 40.3      | 50.6     | 57.6     | 52.2     | 54.7      | 45.1      |
| [NSP-BERT](https://arxiv.org/abs/2109.03564)-110M      | 86.9      | 47.6      | 51        | 41.6      | 37.4      | 63.4     | 52       | **64.4** | 59.4      | 55.96     |
| [ZeroPrompt](https://arxiv.org/abs/2201.06910)-T5-1.5B    | -         | -         | -         | 16.14     | 46.16     | -        | -        | -        | 47.98     | -         |
|  [Yuan1.0-13B](https://arxiv.org/abs/2110.04725)  | 88.13     | 38.99     | 57.47     | 38.82     | 48.13     | 59.38    | 86.14    | 50       | 38.99     | 56.22     |
| [ERNIE3.0-240B](https://arxiv.org/abs/2107.02137) | 88.75     | **50.97** | **57.83** | **40.42** | 53.57     | 64.38    | 87.13    | 56.25    | 53.46     | 61.41     |
| [UniMC-RoBERTa-110M](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-RoBERTa-110M-Chinese)    | 86.16     | 31.26     | 46.61     | 26.54     | 66.91     | 73.34    | 66.68    | 50.09    | 53.66     | 55.7      |
| [UniMC-RoBERTa-330M](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-RoBERTa-330M-Chinese)     | 87.5      | 30.4      | 47.6      | 31.5      | 69.9      | 75.9     | 78.17    | 49.5     | 60.55     | 59.01     |
| [UniMC-MegatronBERT-1.3B](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-MegatronBERT-1.3B-Chinese)     | **88.79** | 42.06     | 55.21     | 33.93     | **75.57** | **79.5** | **89.4** | 50.25    | **66.67** | **64.53** |

**Full dataset**

|             Model                               | AFQMC | TNEWS1.1 | IFLYTEK | OCNLI | CMNLI | WSC1.1 | CSL   | CHID  | C3    |
|--------------------------------------------|-------|----------|---------|-------|-------|--------|-------|-------|-------|
| RoBERTa-Base                               | 74.06 | 57.5     | 60.36   | 74.3  | 79.73 | 83.48  | 85.37 |    -   |     -  |
| RoBERTa-Large                              | 74.88 | 58.79    | 61.52   | 77.7  | 81.4  | 89.14  | 86    |    -   |    -   |
| [Erlangshen-MegatronBert-1.3B](https://huggingface.co/IDEA-CCNL/Erlangshen-MegatronBert-1.3B) 「Finetuning」              | 76.08 | 59.38    | 62.34   | 79.14 | 81    | 92.43  | 87.2  | 84.65 | 86.77 |
| [Erlangshen-UniMC-MegatronBERT-1.3B-Chinese](https://huggingface.co/IDEA-CCNL/Erlangshen-UniMC-MegatronBERT-1.3B-Chinese) | 77.09 | 60.4     | 62.67   | 83.05 | 84.76 | 93.74  | 87.67 | 85.93 | 86.54 |


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
pretrained_model_path = 'IDEA-CCNL/Erlangshen-UniMC-RoBERTa-330M-Chinese'
args.learning_rate=2e-5
args.max_length=512
args.max_epochs=3
args.batchsize=8
args.default_root_dir='./'
model = UniMCPipelines(args,pretrained_model_path)

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
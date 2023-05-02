---
language: 
  - zh

license: apache-2.0

tags:
  - classification

inference: false

---

# Erlangshen-MacBERT-325M-NLI-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

3.25亿参数的MacBERT，在NLI任务上进行预训练，并在FewCLUE的OCNLI任务上微调。

The MacBERT with 325M parameters is pre-trained for Chinese NLI tasks, and finetuned on task OCNLI from FewCLUE.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General  | 自然语言理解 NLU | 二郎神 Erlangshen | MacBERT      |      325M     |   Chinese     |

## 模型信息 Model Information


为了提高模型在NLI上的效果，我们收集了大量NLI进行预训练，随后在FewCLUE的OCNLI任务进行微调，所有的训练均基于我们提出的UniMC框架。最终结果表明，3.25亿参数的模型通过我们的训练策略在NLI任务上可以达到1.3亿参数大模型相当的效果。

To improve the model performance on the NLI task, we collected numerous NLI datasets for pre-training. Then the model was finetuned on a specific NLI task, OCNLI from FewCLUE. All the training is based on the UniMC framework we proposed. The results show that our model with 325M parameters could achieve comparable performance to the model with 1.3B parameters on the NLI task via our training strategies.

### 下游效果 Performance

BUSTM任务上的效果：

The results on BUSTM:

| Model                                         | BUSTM  | 
| --------------------------------------------- | ------ | 
| Erlangshen-UniMC-MegatronBERT-1.3B-Chinese    | 76.34  |
| **Erlangshen-MacBERT-325M-NLI-Chinese**       | 74.42  | 

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
model_path='IDEA-CCNL/Erlangshen-MacBERT-325M-NLI-Chinese'
args.learning_rate=2e-5
args.max_length=512
args.max_epochs=3
args.batchsize=8
args.default_root_dir='./'
model = UniMCPipelines(args,model_path)
train_data = []
dev_data = []
test_data = [
        {"task_type":"自然语言推理",
         "texta": "七五期间开始,国家又投资将武汉市区的部分土堤改建为钢筋泥凝土防水墙", 
         "textb": "八五期间会把剩下的土堤都改建完", 
         "question": "根据这段话",  
         "label": 'neutral', 
         "id": 1}
    ]
if args.train:
    model.train(train_data, dev_data)
result = model.predict(test_data)
for line in result[:20]:
    print(line)


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
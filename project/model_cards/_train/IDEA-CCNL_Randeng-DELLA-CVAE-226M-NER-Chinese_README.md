---
language: zh
tags:
- VAE
- CVAE
- NER
- Data Augmentation
inference: False
---

# Randeng-DELLA-226M-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

在悟道数据集上进行通用预训练的Deep VAE模型后又在命名实体识别任务的数据上微调的CVAE模型。其中编码器和解码器都是GPT-2架构。可以在给定命名实体和其类别后生成包含该命名实体的句子。

A deep VAE model pretrained on Wudao dataset and finetinued on NER dataset. Both encoder and decoder are based on GPT-2 architecture. This model is capable of generating a sentence given the named entity and its entity type.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General | 受控文本生成 CTG | 燃灯 Randeng | DELLA |     226M      |    条件变分自编码器-中文 CVAE-Chinese    |


## 模型信息 Model Information

参考论文 Reference Paper：[Fuse It More Deeply! A Variational Transformer with Layer-Wise Latent Variable Inference for Text Generation](https://arxiv.org/abs/2207.06130)

本模型使用了Della论文里的循环潜在向量架构，但对于解码器生成并未采用原论文的low-rank-tensor-product来进行信息融合，而是使用了简单的线性变换后逐位逐词添加的方式。该方式对于开放域数据集的预训练稳定性有较大正向作用。

Note that although we adopted the layer-wise recurrent latent variables structure as the paper, we did not use the low-rank-tensor-product to fuse the latent vectors to the decoder hidden states. Instead we applied a simple linear transformation on the latent vectors and then add them to the hidden states independently. 


## 使用 Usage

```python
# Checkout the latest Fengshenbang-LM directory and run following script under Fengshenbang-LM root directory 

import torch
from torch.nn.utils.rnn import pad_sequence
from fengshen.models.deepVAE.deep_vae import Della
from transformers.models.bert.tokenization_bert import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("IDEA-CCNL/Randeng-DELLA-CVAE-226M-NER-Chinese")
vae_model = Della.from_pretrained("IDEA-CCNL/Randeng-DELLA-CVAE-226M-NER-Chinese")

special_tokens_dict = {'bos_token': '<BOS>', 'eos_token': '<EOS>', 'additional_special_tokens': ['<ENT>', '<ENS>']}
tokenizer.add_special_tokens(special_tokens_dict)

device = 0
model = vae_model.model.to(device)
ent_token_type_id = tokenizer.additional_special_tokens_ids[0]
ent_token_sep_id = tokenizer.additional_special_tokens_ids[1]
bos_token_id, eos_token_id = tokenizer.bos_token_id, tokenizer.eos_token_id
decoder_target, decoder_entities = [], []
entity_list = [('深圳', '地点/地理位置'), ('昨天', '时间')]

for ent in entity_list:
    entity_name = tokenizer.convert_tokens_to_ids(tokenizer.tokenize(ent[0]))
    entity_type = tokenizer.convert_tokens_to_ids(tokenizer.tokenize(ent[1]))
    decoder_entities.extend(entity_name + [ent_token_type_id] + entity_type + [ent_token_sep_id])
decoder_entities.extend([bos_token_id]) # for generation 
decoder_target.append(torch.tensor(decoder_entities, dtype=torch.long))
inputs = pad_sequence(decoder_target, batch_first=True, padding_value=0)

encoder_outputs = model.encoder(input_ids=inputs.to(device))
prior_z_list, prior_output_list = model.get_cond_prior_vecs(encoder_outputs.hidden_states[1:], 
    inputs, sample=True, beta_logvar=0.)
outputs = model.decoder.generate(input_ids=inputs.to(device), layer_latent_vecs=prior_z_list, labels=None,
    label_ignore=model.pad_token_id, num_return_sequences=32, max_new_tokens=256,
    eos_token_id=tokenizer.eos_token_id, pad_token_id=tokenizer.pad_token_id,
    no_repeat_ngram_size=-1, do_sample=True, top_p=0.8)

print(tokenizer.decode(inputs[0]))
gen_sents = []
for idx in range(len(outputs)):
    sent_len= 512 if eos_token_id not in outputs[idx].tolist() else outputs[idx].tolist().index(eos_token_id) + 1
    start_loc = outputs[idx].tolist().index(bos_token_id) 
    gen_sent = tokenizer.decode(outputs[idx][start_loc:sent_len]).replace(' ', '')
    if all([ent[0] in gen_sent for ent in entity_list]):
        gen_sents.append(gen_sent)
for s in gen_sents:
    print(s)
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
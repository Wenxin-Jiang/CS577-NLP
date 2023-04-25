---
license: apache-2.0

language: zh
inference: false
tags:
- text-generation
- dialogue-generation
- pytorch
- inference acceleration
- gpt2
- gpt3
---
# YuYan-Dialogue

YuYan is a series of Chinese language models with different size, developed by Fuxi AI lab, Netease.Inc. They are trained on a large Chinese novel dataset of high quality. 

YuYan is in the same family of decoder-only models like [GPT2 and GPT-3](https://arxiv.org/abs/2005.14165). As such, it was pretrained using the self-supervised causal language modedling objective.

YuYan-Dialogue is a dialogue model by fine-tuning the YuYan-11b on a large multi-turn dialogue dataset of high quality. It has very strong conversation generation capabilities. 

## Model Inference Acceleration 

As the model size increases, the model inference time increases and more computational resources are required. 

Therefore, we developed our own transformer model inference acceleration framework, [EET](https://github.com/NetEase-FuXi/EET.git). More details are in [Easy and Efficient Transformer: Scalable Inference Solution For Large NLP Model](https://aclanthology.org/2022.naacl-industry.8/).

We combine our language model with the EET inference framework to provide industrial-grade inference reasoning performance.

## How to use

Our model is trained based on the [fairseq](https://github.com/facebookresearch/fairseq). As a result, the inference and finetuning depend on it.

For inference, we modify some parts of the original fairseq codes. Mainly 
> fairseq-0.12.2/fairseq/sequence_generator.py

We integrate the EET with sequence_generator. We replace the eos token to a token unlikely to be sampled to ensure the generated text length. The repetition penalty trick is also modified. You can change the penalty strength by adjusting the value of `self.ban_weight`.  

Then, to keep the eos token in the final generated text, we change the line 75 `include_eos=False` to `include_eos=True` in
> fairseq-0.12.2/fairseq/data/dictionary.py 

Finally, to pass in parameters in python scripts, we remove the line 67 ~ line 69 in
>fairseq-0.12.2/fairseq/dataclass/utils.py

Below are the install tutorial.

```
# install pytorch
pip install torch==1.8.1 # install pytorch

# install fairseq
unzip fairseq-0.12.2.zip
cd fairseq-0.12.2
pip  install.

# install EET
git clone https://github.com/NetEase-FuXi/EET.git
cd EET
pip install .

# install transformers (EET requirements)
pip install transformers==4.23

# make a folder, move the dictionary file and model file into it.
mkdir transformer_lm_gpt2_xxl_dialogue
mv dict.txt transformer_lm_gpt2_xxl_dialogue/
mv checkpoint_best_part_*.pt transformer_lm_gpt2_xxl_dialogue/

```
`inference.py` is a script to provide a interface to initialize the EET object and sequence_generator. It includes some pre-process and post-process functions for text input and output. You can modify the script according to your needs. 

In addition, it provide a simple object to organize the dialogue generation and dialogue history.

After the environment is ready, several lines of codes can realize the inference.

``` python

from inference import Inference, Dialogue
model_path = "transformer_lm_gpt2_xxl_dialogue/checkpoint_best.pt"
data_path = "transformer_lm_gpt2_xxl_dialogue"
eet_batch_size = 10  # max inference batch size, adjust according to cuda memory, 40GB memory is necessary 
inference = Inference(model_path, data_path, eet_batch_size)
dialogue_model = Dialogue(inference)
dialogue_model.get_repsonse("你好啊")
```
## Citation
If you find the technical report or resource is useful, please cite the following technical report in your paper.
- https://aclanthology.org/2022.naacl-industry.8/
```
@inproceedings{li-etal-2022-easy,
    title = "Easy and Efficient Transformer: Scalable Inference Solution For Large {NLP} Model",
    author = "Li, Gongzheng  and
      Xi, Yadong  and
      Ding, Jingzhen  and
      Wang, Duan  and
      Luo, Ziyang  and
      Zhang, Rongsheng  and
      Liu, Bai  and
      Fan, Changjie  and
      Mao, Xiaoxi  and
      Zhao, Zeng",
    booktitle = "Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies: Industry Track",
    month = jul,
    year = "2022",
    address = "Hybrid: Seattle, Washington + Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.naacl-industry.8",
    doi = "10.18653/v1/2022.naacl-industry.8",
    pages = "62--68"
}

```
## Contact Us
You can also contact us by email:

xiyadong@corp.netease.com, dingjingzhen@corp.netease

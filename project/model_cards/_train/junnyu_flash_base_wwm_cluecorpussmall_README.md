---
license: mit
inference: False
---

# PS: 效果不怎么好，体验一下就行了。。。。。。wwm-MLM最终准确率55.5左右。
# cluner NER实验(globalpointer的结果差不多，softmax结果差好多- -)
```python
# flash base  + globalpointer
04/08/2022 10:53:34 - INFO - __main__ - ADDRESS = Score(f1=0.607703, precision=0.64939, recall=0.571046, tp=213, pred=328, gold=373)
04/08/2022 10:53:34 - INFO - __main__ - BOOK = Score(f1=0.8125, precision=0.873134, recall=0.75974, tp=117, pred=134, gold=154)
04/08/2022 10:53:34 - INFO - __main__ - COMPANY = Score(f1=0.818304, precision=0.832877, recall=0.804233, tp=304, pred=365, gold=378)
04/08/2022 10:53:34 - INFO - __main__ - GAME = Score(f1=0.854305, precision=0.834951, recall=0.874576, tp=258, pred=309, gold=295)
04/08/2022 10:53:34 - INFO - __main__ - GOVERNMENT = Score(f1=0.823529, precision=0.775, recall=0.878543, tp=217, pred=280, gold=247)
04/08/2022 10:53:34 - INFO - __main__ - MOVIE = Score(f1=0.810997, precision=0.842857, recall=0.781457, tp=118, pred=140, gold=151)
04/08/2022 10:53:34 - INFO - __main__ - NAME = Score(f1=0.874042, precision=0.890625, recall=0.858065, tp=399, pred=448, gold=465)
04/08/2022 10:53:34 - INFO - __main__ - ORGANIZATION = Score(f1=0.813986, precision=0.836207, recall=0.792916, tp=291, pred=348, gold=367)
04/08/2022 10:53:34 - INFO - __main__ - POSITION = Score(f1=0.78478, precision=0.808824, recall=0.762125, tp=330, pred=408, gold=433)
04/08/2022 10:53:34 - INFO - __main__ - SCENE = Score(f1=0.683805, precision=0.738889, recall=0.636364, tp=133, pred=180, gold=209)
04/08/2022 10:53:34 - INFO - __main__ - micro_f1 = Score(f1=0.79175, precision=0.809524, recall=0.77474, tp=2380, pred=2940, gold=3072)
04/08/2022 10:53:34 - INFO - __main__ - macro_f1 = Score(f1=0.788395, precision=0.808275, recall=0.771906, tp=0, pred=0, gold=0)
04/08/2022 10:53:34 - INFO - __main__ - mean_f1 = 0.790072

# flash base  + softmax
04/08/2022 11:10:44 - INFO - __main__ - ADDRESS = Score(f1=0.568987, precision=0.522422, recall=0.624665, tp=233, pred=446, gold=373)
04/08/2022 11:10:44 - INFO - __main__ - BOOK = Score(f1=0.750789, precision=0.730061, recall=0.772727, tp=119, pred=163, gold=154)
04/08/2022 11:10:44 - INFO - __main__ - COMPANY = Score(f1=0.75528, precision=0.711944, recall=0.804233, tp=304, pred=427, gold=378)
04/08/2022 11:10:44 - INFO - __main__ - GAME = Score(f1=0.811502, precision=0.767372, recall=0.861017, tp=254, pred=331, gold=295)
04/08/2022 11:10:44 - INFO - __main__ - GOVERNMENT = Score(f1=0.738636, precision=0.69395, recall=0.789474, tp=195, pred=281, gold=247)
04/08/2022 11:10:44 - INFO - __main__ - MOVIE = Score(f1=0.74359, precision=0.720497, recall=0.768212, tp=116, pred=161, gold=151)
04/08/2022 11:10:44 - INFO - __main__ - NAME = Score(f1=0.831967, precision=0.794521, recall=0.873118, tp=406, pred=511, gold=465)
04/08/2022 11:10:44 - INFO - __main__ - ORGANIZATION = Score(f1=0.754054, precision=0.747989, recall=0.760218, tp=279, pred=373, gold=367)
04/08/2022 11:10:44 - INFO - __main__ - POSITION = Score(f1=0.742729, precision=0.720174, recall=0.766744, tp=332, pred=461, gold=433)
04/08/2022 11:10:44 - INFO - __main__ - SCENE = Score(f1=0.628842, precision=0.621495, recall=0.636364, tp=133, pred=214, gold=209)
04/08/2022 11:10:44 - INFO - __main__ - micro_f1 = Score(f1=0.736335, precision=0.703979, recall=0.77181, tp=2371, pred=3368, gold=3072)
04/08/2022 11:10:44 - INFO - __main__ - macro_f1 = Score(f1=0.732638, precision=0.703043, recall=0.765677, tp=0, pred=0, gold=0)
04/08/2022 11:10:44 - INFO - __main__ - mean_f1 = 0.734486


# bert base + globalpointer
04/08/2022 11:22:48 - INFO - __main__ - ADDRESS = Score(f1=0.641558, precision=0.622166, recall=0.662198, tp=247, pred=397, gold=373)
04/08/2022 11:22:48 - INFO - __main__ - BOOK = Score(f1=0.813115, precision=0.821192, recall=0.805195, tp=124, pred=151, gold=154)
04/08/2022 11:22:48 - INFO - __main__ - COMPANY = Score(f1=0.823684, precision=0.819372, recall=0.828042, tp=313, pred=382, gold=378)
04/08/2022 11:22:48 - INFO - __main__ - GAME = Score(f1=0.841762, precision=0.811321, recall=0.874576, tp=258, pred=318, gold=295)
04/08/2022 11:22:48 - INFO - __main__ - GOVERNMENT = Score(f1=0.827324, precision=0.778571, recall=0.882591, tp=218, pred=280, gold=247)
04/08/2022 11:22:48 - INFO - __main__ - MOVIE = Score(f1=0.82392, precision=0.826667, recall=0.821192, tp=124, pred=150, gold=151)
04/08/2022 11:22:48 - INFO - __main__ - NAME = Score(f1=0.861345, precision=0.840164, recall=0.883621, tp=410, pred=488, gold=464)
04/08/2022 11:22:48 - INFO - __main__ - ORGANIZATION = Score(f1=0.804911, precision=0.806011, recall=0.803815, tp=295, pred=366, gold=367)
04/08/2022 11:22:48 - INFO - __main__ - POSITION = Score(f1=0.805046, precision=0.799544, recall=0.810624, tp=351, pred=439, gold=433)
04/08/2022 11:22:48 - INFO - __main__ - SCENE = Score(f1=0.702703, precision=0.722222, recall=0.684211, tp=143, pred=198, gold=209)
04/08/2022 11:22:48 - INFO - __main__ - micro_f1 = Score(f1=0.795833, precision=0.783528, recall=0.808531, tp=2483, pred=3169, gold=3071)
04/08/2022 11:22:48 - INFO - __main__ - macro_f1 = Score(f1=0.794537, precision=0.784723, recall=0.805606, tp=0, pred=0, gold=0)
04/08/2022 11:22:48 - INFO - __main__ - mean_f1 = 0.795185
```

# cmeee + globalpointer
```python
04/08/2022 11:50:41 - INFO - __main__ - bod = Score(f1=0.639522, precision=0.642318, recall=0.63675, tp=3746, pred=5832, gold=5883)
04/08/2022 11:50:41 - INFO - __main__ - dep = Score(f1=0.473988, precision=0.650794, recall=0.372727, tp=41, pred=63, gold=110)
04/08/2022 11:50:41 - INFO - __main__ - dis = Score(f1=0.716959, precision=0.704479, recall=0.729889, tp=3602, pred=5113, gold=4935)
04/08/2022 11:50:41 - INFO - __main__ - dru = Score(f1=0.756328, precision=0.829329, recall=0.695139, tp=1001, pred=1207, gold=1440)
04/08/2022 11:50:41 - INFO - __main__ - equ = Score(f1=0.518703, precision=0.638037, recall=0.436975, tp=104, pred=163, gold=238)
04/08/2022 11:50:41 - INFO - __main__ - ite = Score(f1=0.322533, precision=0.503448, recall=0.23727, tp=219, pred=435, gold=923)
04/08/2022 11:50:41 - INFO - __main__ - mic = Score(f1=0.746967, precision=0.75614, recall=0.738014, tp=431, pred=570, gold=584)
04/08/2022 11:50:41 - INFO - __main__ - pro = Score(f1=0.611138, precision=0.614138, recall=0.608167, tp=1251, pred=2037, gold=2057)
04/08/2022 11:50:41 - INFO - __main__ - sym = Score(f1=0.47969, precision=0.495738, recall=0.464649, tp=1919, pred=3871, gold=4130)
04/08/2022 11:50:41 - INFO - __main__ - micro_f1 = Score(f1=0.622061, precision=0.638329, recall=0.606601, tp=12314, pred=19291, gold=20300)
04/08/2022 11:50:41 - INFO - __main__ - macro_f1 = Score(f1=0.585092, precision=0.648269, recall=0.54662, tp=0, pred=0, gold=0)
04/08/2022 11:50:41 - INFO - __main__ - mean_f1 = 0.603576
```
# install
- https://github.com/JunnYu/FLASHQuad_pytorch

# usage
```python
import torch
from flash import FLASHForMaskedLM
from transformers import BertTokenizerFast
tokenizer = BertTokenizerFast.from_pretrained("junnyu/flash_base_wwm_cluecorpussmall")
model = FLASHForMaskedLM.from_pretrained("junnyu/flash_base_wwm_cluecorpussmall")
model.eval()
text = "天气预报说今天的天[MASK]很好，那么我[MASK]一起去公园玩吧！"
inputs = tokenizer(text, return_tensors="pt", padding="max_length", max_length=512,  return_token_type_ids=False) #这里必须是512，不然结果可能不对。
with torch.no_grad():
    pt_outputs = model(**inputs).logits[0]

pt_outputs_sentence = "pytorch: "
for i, id in enumerate(tokenizer.encode(text)):
    if id == tokenizer.mask_token_id:
        val,idx = pt_outputs[i].softmax(-1).topk(k=5)
        tokens = tokenizer.convert_ids_to_tokens(idx)
        new_tokens = []
        for v,t in zip(val.cpu(),tokens):
            new_tokens.append(f"{t}+{round(v.item(),4)}")
        pt_outputs_sentence += "[" + "||".join(new_tokens) + "]"
    else:
        pt_outputs_sentence += "".join(
            tokenizer.convert_ids_to_tokens([id], skip_special_tokens=True))
print(pt_outputs_sentence)
# pytorch: 天气预报说今天的天[气+0.994||天+0.0015||空+0.0014||晴+0.0005||阳+0.0003]很好，那么我[们+0.9563||就+0.0381||也+0.0032||俩+0.0004||来+0.0002]一起去公园玩吧！
```
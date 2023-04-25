---
language: 
- multilingual
- en 
- ar 
- bg 
- de 
- el 
- es 
- fr 
- hi 
- ru 
- sw 
- th 
- tr 
- ur 
- vi 
- zh
tags: 
  - deberta
  - deberta-v3
  - mdeberta
  - fill-mask
thumbnail: https://huggingface.co/front/thumbnails/microsoft.png
license: mit
---

## DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing

[DeBERTa](https://arxiv.org/abs/2006.03654) improves the BERT and RoBERTa models using disentangled attention and enhanced mask decoder. With those two improvements, DeBERTa out perform RoBERTa on a majority of NLU tasks with 80GB training data. 

In [DeBERTa V3](https://arxiv.org/abs/2111.09543), we further improved the efficiency of DeBERTa using ELECTRA-Style pre-training with Gradient Disentangled Embedding Sharing. Compared to DeBERTa,  our V3 version significantly improves the model performance on downstream tasks.  You can find more technique details about the new model from our [paper](https://arxiv.org/abs/2111.09543).

Please check the [official repository](https://github.com/microsoft/DeBERTa) for more implementation details and updates.

mDeBERTa is multilingual version of DeBERTa which use the same structure as DeBERTa and was trained with CC100 multilingual data.
The mDeBERTa V3 base model comes with 12 layers and a hidden size of 768. It has 86M backbone parameters  with a vocabulary containing 250K tokens which introduces 190M parameters in the Embedding layer.  This model was trained using the 2.5T CC100 data as XLM-R.


#### Fine-tuning on NLU tasks

We present the dev results on XNLI with zero-shot cross-lingual transfer setting, i.e. training with English data only, test on other languages.

| Model        |avg | en |  fr| es  | de  | el  | bg  | ru  |tr   |ar   |vi   | th  | zh | hi  | sw  | ur  | 
|--------------| ----|----|----|---- |--   |--   |--   | --  |--   |--   |--   | --  | -- | --  | --  | --  |
| XLM-R-base   |76.2 |85.8|79.7|80.7 |78.7 |77.5 |79.6 |78.1 |74.2 |73.8 |76.5 |74.6 |76.7| 72.4| 66.5| 68.3|
| mDeBERTa-base|**79.8**+/-0.2|**88.2**|**82.6**|**84.4** |**82.7** |**82.3** |**82.4** |**80.8** |**79.5** |**78.5** |**78.1** |**76.4** |**79.5**| **75.9**| **73.9**| **72.4**|

#### Fine-tuning with HF transformers

```bash
#!/bin/bash

cd transformers/examples/pytorch/text-classification/

pip install datasets

output_dir="ds_results"

num_gpus=8

batch_size=4

python -m torch.distributed.launch --nproc_per_node=${num_gpus} \
  run_xnli.py \
  --model_name_or_path microsoft/mdeberta-v3-base \
  --task_name $TASK_NAME \
  --do_train \
  --do_eval \
  --train_language en \
  --language en \
  --evaluation_strategy steps \
  --max_seq_length 256 \
  --warmup_steps 3000 \
  --per_device_train_batch_size ${batch_size} \
  --learning_rate 2e-5 \
  --num_train_epochs 6 \
  --output_dir $output_dir \
  --overwrite_output_dir \
  --logging_steps 1000 \
  --logging_dir $output_dir

```

### Citation

If you find DeBERTa useful for your work, please cite the following papers:

``` latex
@misc{he2021debertav3,
      title={DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}, 
      author={Pengcheng He and Jianfeng Gao and Weizhu Chen},
      year={2021},
      eprint={2111.09543},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

``` latex
@inproceedings{
he2021deberta,
title={DEBERTA: DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION},
author={Pengcheng He and Xiaodong Liu and Jianfeng Gao and Weizhu Chen},
booktitle={International Conference on Learning Representations},
year={2021},
url={https://openreview.net/forum?id=XPZIaotutsD}
}
```

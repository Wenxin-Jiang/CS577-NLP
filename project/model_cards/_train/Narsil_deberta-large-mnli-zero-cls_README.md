---
language: en
tags: 
- deberta-v1
- deberta-mnli
tasks: mnli
thumbnail: https://huggingface.co/front/thumbnails/microsoft.png
license: mit
pipeline_tag: zero-shot-classification
---

## DeBERTa: Decoding-enhanced BERT with Disentangled Attention

[DeBERTa](https://arxiv.org/abs/2006.03654) improves the BERT and RoBERTa models using disentangled attention and enhanced mask decoder. It outperforms BERT and RoBERTa on  majority of NLU tasks with 80GB training data. 

Please check the [official repository](https://github.com/microsoft/DeBERTa) for more details and updates.

This is the DeBERTa large model fine-tuned with MNLI task.

#### Fine-tuning on NLU tasks

We present the dev results on SQuAD 1.1/2.0 and several GLUE benchmark tasks.

| Model                     | SQuAD 1.1 | SQuAD 2.0 | MNLI-m/mm   | SST-2 | QNLI | CoLA | RTE    | MRPC  | QQP   |STS-B |
|---------------------------|-----------|-----------|-------------|-------|------|------|--------|-------|-------|------|
|                           | F1/EM     | F1/EM     | Acc         | Acc   | Acc  | MCC  | Acc    |Acc/F1 |Acc/F1 |P/S   |
| BERT-Large                | 90.9/84.1 | 81.8/79.0 | 86.6/-      | 93.2  | 92.3 | 60.6 | 70.4   | 88.0/-       | 91.3/- |90.0/- |
| RoBERTa-Large             | 94.6/88.9 | 89.4/86.5 | 90.2/-      | 96.4  | 93.9 | 68.0 | 86.6   | 90.9/-       | 92.2/- |92.4/- |
| XLNet-Large               | 95.1/89.7 | 90.6/87.9 | 90.8/-      | 97.0  | 94.9 | 69.0 | 85.9   | 90.8/-       | 92.3/- |92.5/- |
| [DeBERTa-Large](https://huggingface.co/microsoft/deberta-large)<sup>1</sup> | 95.5/90.1 | 90.7/88.0 | 91.3/91.1| 96.5|95.3| 69.5| 91.0| 92.6/94.6| 92.3/- |92.8/92.5 |
| [DeBERTa-XLarge](https://huggingface.co/microsoft/deberta-xlarge)<sup>1</sup> | -/-  | -/-  | 91.5/91.2| 97.0 | - | -    | 93.1   | 92.1/94.3    | -    |92.9/92.7|
| [DeBERTa-V2-XLarge](https://huggingface.co/microsoft/deberta-v2-xlarge)<sup>1</sup>|95.8/90.8| 91.4/88.9|91.7/91.6| **97.5**| 95.8|71.1|**93.9**|92.0/94.2|92.3/89.8|92.9/92.9|
|**[DeBERTa-V2-XXLarge](https://huggingface.co/microsoft/deberta-v2-xxlarge)<sup>1,2</sup>**|**96.1/91.4**|**92.2/89.7**|**91.7/91.9**|97.2|**96.0**|**72.0**| 93.5| **93.1/94.9**|**92.7/90.3** |**93.2/93.1** |
--------
#### Notes.
 - <sup>1</sup> Following RoBERTa, for RTE, MRPC, STS-B, we fine-tune the tasks based on [DeBERTa-Large-MNLI](https://huggingface.co/microsoft/deberta-large-mnli), [DeBERTa-XLarge-MNLI](https://huggingface.co/microsoft/deberta-xlarge-mnli), [DeBERTa-V2-XLarge-MNLI](https://huggingface.co/microsoft/deberta-v2-xlarge-mnli), [DeBERTa-V2-XXLarge-MNLI](https://huggingface.co/microsoft/deberta-v2-xxlarge-mnli). The results of SST-2/QQP/QNLI/SQuADv2 will also be slightly improved when start from MNLI fine-tuned models, however, we only report the numbers fine-tuned from pretrained base models for those 4 tasks.
 - <sup>2</sup> To try the **XXLarge** model with **[HF transformers](https://huggingface.co/transformers/main_classes/trainer.html)**, you need to specify **--sharded_ddp**
 
```bash  
cd transformers/examples/text-classification/
export TASK_NAME=mrpc
python -m torch.distributed.launch --nproc_per_node=8 run_glue.py   --model_name_or_path microsoft/deberta-v2-xxlarge   \\\n--task_name $TASK_NAME   --do_train   --do_eval   --max_seq_length 128   --per_device_train_batch_size 4   \\\n--learning_rate 3e-6   --num_train_epochs 3   --output_dir /tmp/$TASK_NAME/ --overwrite_output_dir --sharded_ddp --fp16
```

### Citation

If you find DeBERTa useful for your work, please cite the following paper:

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


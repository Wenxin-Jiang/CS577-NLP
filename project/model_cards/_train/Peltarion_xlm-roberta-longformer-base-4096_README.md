---
tags:
- longformer
language: multilingual
license: apache-2.0
datasets:
- wikitext
---

## XLM-R Longformer Model   
XLM-R Longformer is a XLM-R model, that has been extended to allow sequence lengths up to 4096 tokens, instead of the regular 512. The model was pre-trained from the XLM-RoBERTa checkpoint using the Longformer [pre-training scheme](https://github.com/allenai/longformer/blob/master/scripts/convert_model_to_long.ipynb) on the English WikiText-103 corpus.     
  
The reason for this was to investigate methods for creating efficient Transformers for low-resource languages, such as Swedish, without the need to pre-train them on long-context datasets in each respecitve language. The trained model came as a result of a master thesis project at [Peltarion](https://peltarion.com/) and was fine-tuned on multilingual quesion-answering tasks, with code available [here](https://github.com/MarkusSagen/Master-Thesis-Multilingual-Longformer#xlm-r).   
  
Since both XLM-R model and Longformer models are large models, it it recommended to run the models with NVIDIA Apex (16bit precision), large GPU and several gradient accumulation steps.

## How to Use  
The model can be used as expected to fine-tune on a downstream task.    
For instance for QA.  

```python
import torch
from transformers import AutoModel, AutoTokenizer

MAX_SEQUENCE_LENGTH = 4096
MODEL_NAME_OR_PATH = "markussagen/xlm-roberta-longformer-base-4096"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME_OR_PATH,
    max_length=MAX_SEQUENCE_LENGTH,
    padding="max_length",
    truncation=True,
)

model = AutoModelForQuestionAnswering.from_pretrained(
    MODEL_NAME_OR_PATH, 
    max_length=MAX_SEQUENCE_LENGTH,
)


```

## Training Procedure   
The model have been trained on the WikiText-103 corpus, using a **48GB** GPU with the following training script and parameters. The model was pre-trained for 6000 iterations and took ~5 days. See the full [training script](https://github.com/MarkusSagen/Master-Thesis-Multilingual-Longformer/blob/main/scripts/finetune_qa_models.py) and [Github repo](https://github.com/MarkusSagen/Master-Thesis-Multilingual-Longformer) for more information
```sh
wget https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-103-raw-v1.zip
unzip wikitext-103-raw-v1.zip   

export DATA_DIR=./wikitext-103-raw

scripts/run_long_lm.py \
    --model_name_or_path xlm-roberta-base \
    --model_name xlm-roberta-to-longformer \
    --output_dir ./output \
    --logging_dir ./logs \
    --val_file_path $DATA_DIR/wiki.valid.raw \
    --train_file_path $DATA_DIR/wiki.train.raw \
    --seed 42 \
    --max_pos 4096 \
    --adam_epsilon 1e-8 \
    --warmup_steps 500 \
    --learning_rate 3e-5 \
    --weight_decay 0.01 \
    --max_steps 6000 \
    --evaluate_during_training \
    --logging_steps 50 \
    --eval_steps 50 \
    --save_steps 6000  \
    --max_grad_norm 1.0 \
    --per_device_eval_batch_size 2 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 64 \
    --overwrite_output_dir \
    --fp16 \
    --do_train \
    --do_eval
```


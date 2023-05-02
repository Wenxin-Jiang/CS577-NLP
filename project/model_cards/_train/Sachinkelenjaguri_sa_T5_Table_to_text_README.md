import pandas as pd

import os

import torch

from transformers import T5Tokenizer, T5ForConditionalGeneration

from transformers.optimization import  Adafactor 

import time

import warnings

warnings.filterwarnings('ignore')


tokenizer = T5Tokenizer.from_pretrained('Sachinkelenjaguri/sa_T5_Table_to_text')

model = T5ForConditionalGeneration.from_pretrained('Sachinkelenjaguri/sa_T5_Table_to_text', return_dict=True)


def generate(text):

  model.eval()
  input_ids = tokenizer.encode("WebNLG:{} </s>".format(text), return_tensors="pt")  # Batch size 1

  s = time.time()
  outputs = model.generate(input_ids)
  gen_text=tokenizer.decode(outputs[0]).replace('<pad>','').replace('</s>','')
  elapsed = time.time() - s
  print('Generated in {} seconds'.format(str(elapsed)[:4]))
  
  return gen_text



generate(' Russia | leader | Putin')
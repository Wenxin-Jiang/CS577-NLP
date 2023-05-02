---
language: de
tags:
- pytorch
- tf
- Gelectra
datasets:
- mlqa
metrics:
- f1
- em
---

### QA Model trained on MLQA dataset for german langauge.

MODEL used for fine tuning is GELECTRA Large by deepset.ai



## MLQA DEV (german)
EM: 64.27 \
F1: 77.39

## XQUAD TEST (german)
EM: 66.38 \
F1: 82.25 

## Hyperparameters

per_gpu_train_batch_size 4 \
per_gpu_eval_batch_size 32 \
gradient_accumulation_steps 8 \
learning_rate 3e-5 \
num_train_epochs 1.0 \
max_seq_length 384 \
doc_stride 128 

## Model inferencing:
```python
!pip install -q transformers
from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="Sahajtomar/GELECTRAQA",
    tokenizer="Sahajtomar/GELECTRAQA"
)

qa_pipeline({
    'context': "Vor einigen Jahren haben Wissenschaftler ein wichtiges Mutagen identifiziert, das in unseren eigenen Zellen liegt: APOBEC, ein Protein, das normalerweise als Schutzmittel gegen Virusinfektionen fungiert. Heute hat ein Team von Schweizer und russischen Wissenschaftlern unter der Leitung von Sergey Nikolaev, Genetiker an der Universität Genf (UNIGE) in der Schweiz, entschlüsselt, wie APOBEC eine Schwäche unseres DNA-Replikationsprozesses ausnutzt, um Mutationen in unserem Genom zu induzieren.",
    'question': "Welches Mutagen schützt vor Virusinfektionen?"
    
})

# output

{'answer': 'APOBEC', 'end': 121, 'score': 0.987, 'start': 115} 

## Even complex queries can be answered pretty well

qa_pipeline({
    "context": "Es wird erwartet, dass sich schwarze Löcher mit Sternmasse bilden,
                wenn sehr massive Sterne am Ende ihres Lebenszyklus 
                zusammenbrechen. Nachdem sich ein Schwarzes Loch gebildet hat, 
                kann es weiter wachsen,indem es Masse aus seiner Umgebung 
                absorbiert. Durch Absorption anderer Sterne und Verschmelzung mit 
                anderen Schwarzen Löchern können sich  supermassereiche Schwarze 
                Löcher mit Millionen von Sonnenmassen (M☉) bilden.  Es besteht 
                Konsens darüber, dass in den Zentren der meisten Galaxien
                supermassereiche Schwarze Löcher existieren.",
    'question': "Wie Sonnenmassen entstehen?"


})

#output

{'answer': 'Durch Absorption anderer Sterne und Verschmelzung mit anderen Schwarzen Löchern',
 'end': 332,
 'score': 0.23970196,
 'start': 253}
    

```

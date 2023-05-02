---
language: id
inference: false
---

# SQuAD IndoBERT-Lite Base Model

Fine-tuned IndoBERT-Lite from IndoBenchmark using Translated SQuAD datasets.

## How to use

### Using pipeline
```python
from transformers import BertTokenizerFast, pipeline
tokenizer = BertTokenizerFast.from_pretrained(
    'Wikidepia/albert-bahasa-uncased-squad'
)
nlp = pipeline('question-answering', model="Wikidepia/albert-bahasa-uncased-squad", tokenizer=tokenizer)
QA_input = {
    'question': 'Kapan orang Normandia berada di Normandia?',
    'context': 'The Normans (Norman: Nourmands; French: Normands; Latin: Normanni) adalah orang-orang yang pada abad ke-10 dan ke-11 memberikan nama mereka ke Normandia, sebuah wilayah di Prancis. Mereka adalah keturunan dari Norse (\ "Norman \" berasal dari \ "Norseman \") perampok dan perompak dari Denmark, Islandia dan Norwegia yang, di bawah pemimpin mereka Rollo, setuju untuk bersumpah setia kepada Raja Charles III dari Francia Barat. Melalui generasi asimilasi dan pencampuran dengan penduduk asli Franka dan Romawi-Gaul, keturunan mereka secara bertahap akan bergabung dengan budaya Francia Barat yang berbasis di Karoling. Identitas budaya dan etnis orang Normandia yang berbeda awalnya muncul pada paruh pertama abad ke-10, dan terus berkembang selama abad-abad berikutnya.'
}
res = nlp(QA_input)
print(res)
```

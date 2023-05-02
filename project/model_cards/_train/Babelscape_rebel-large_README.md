---
language:
- en
widget:
- text: "Punta Cana is a resort town in the municipality of Higuey, in La Altagracia Province, the eastern most province of the Dominican Republic"
tags:
- seq2seq
- relation-extraction
datasets:
- Babelscape/rebel-dataset
model-index:
- name: REBEL
  results:
  - task:
      name: Relation Extraction
      type: Relation-Extraction
    dataset:
      name: "CoNLL04"
      type: CoNLL04
    metrics:
       - name: RE+ Macro F1 
         type: re+ macro f1
         value: 76.65
  - task:
      name: Relation Extraction
      type: Relation-Extraction
    dataset:
      name: "NYT"
      type: NYT
    metrics:
       - name: F1  
         type: f1
         value: 93.4
license: cc-by-nc-sa-4.0
---
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/rebel-relation-extraction-by-end-to-end/relation-extraction-on-nyt)](https://paperswithcode.com/sota/relation-extraction-on-nyt?p=rebel-relation-extraction-by-end-to-end)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/rebel-relation-extraction-by-end-to-end/relation-extraction-on-conll04)](https://paperswithcode.com/sota/relation-extraction-on-conll04?p=rebel-relation-extraction-by-end-to-end)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/rebel-relation-extraction-by-end-to-end/joint-entity-and-relation-extraction-on-3)](https://paperswithcode.com/sota/joint-entity-and-relation-extraction-on-3?p=rebel-relation-extraction-by-end-to-end)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/rebel-relation-extraction-by-end-to-end/relation-extraction-on-ade-corpus)](https://paperswithcode.com/sota/relation-extraction-on-ade-corpus?p=rebel-relation-extraction-by-end-to-end)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/rebel-relation-extraction-by-end-to-end/relation-extraction-on-re-tacred)](https://paperswithcode.com/sota/relation-extraction-on-re-tacred?p=rebel-relation-extraction-by-end-to-end)
# REBEL <img src="https://i.ibb.co/qsLzNqS/hf-rebel.png" width="30" alt="hf-rebel" border="0" style="display:inline; white-space:nowrap;">: Relation Extraction By End-to-end Language generation
This is the model card for the Findings of EMNLP 2021 paper [REBEL: Relation Extraction By End-to-end Language generation](https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf). We present a new linearization approach and a reframing of Relation Extraction as a seq2seq task. The paper can be found [here](https://github.com/Babelscape/rebel/blob/main/docs/EMNLP_2021_REBEL__Camera_Ready_.pdf). If you use the code, please reference this work in your paper:

    @inproceedings{huguet-cabot-navigli-2021-rebel-relation,
        title = "{REBEL}: Relation Extraction By End-to-end Language generation",
        author = "Huguet Cabot, Pere-Llu{\'\i}s  and
          Navigli, Roberto",
        booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
        month = nov,
        year = "2021",
        address = "Punta Cana, Dominican Republic",
        publisher = "Association for Computational Linguistics",
        url = "https://aclanthology.org/2021.findings-emnlp.204",
        pages = "2370--2381",
        abstract = "Extracting relation triplets from raw text is a crucial task in Information Extraction, enabling multiple applications such as populating or validating knowledge bases, factchecking, and other downstream tasks. However, it usually involves multiple-step pipelines that propagate errors or are limited to a small number of relation types. To overcome these issues, we propose the use of autoregressive seq2seq models. Such models have previously been shown to perform well not only in language generation, but also in NLU tasks such as Entity Linking, thanks to their framing as seq2seq tasks. In this paper, we show how Relation Extraction can be simplified by expressing triplets as a sequence of text and we present REBEL, a seq2seq model based on BART that performs end-to-end relation extraction for more than 200 different relation types. We show our model{'}s flexibility by fine-tuning it on an array of Relation Extraction and Relation Classification benchmarks, with it attaining state-of-the-art performance in most of them.",
    }

The original repository for the paper can be found [here](https://github.com/Babelscape/rebel)

Be aware that the inference widget at the right does not output special tokens, which are necessary to distinguish the subject, object and relation types. For a demo of REBEL and its pre-training dataset check the [Spaces demo](https://huggingface.co/spaces/Babelscape/rebel-demo).

## Pipeline usage

```python
from transformers import pipeline

triplet_extractor = pipeline('text2text-generation', model='Babelscape/rebel-large', tokenizer='Babelscape/rebel-large')
# We need to use the tokenizer manually since we need special tokens.
extracted_text = triplet_extractor.tokenizer.batch_decode([triplet_extractor("Punta Cana is a resort town in the municipality of Higuey, in La Altagracia Province, the eastern most province of the Dominican Republic", return_tensors=True, return_text=False)[0]["generated_token_ids"]])
print(extracted_text[0])
# Function to parse the generated text and extract the triplets
def extract_triplets(text):
    triplets = []
    relation, subject, relation, object_ = '', '', '', ''
    text = text.strip()
    current = 'x'
    for token in text.replace("<s>", "").replace("<pad>", "").replace("</s>", "").split():
        if token == "<triplet>":
            current = 't'
            if relation != '':
                triplets.append({'head': subject.strip(), 'type': relation.strip(),'tail': object_.strip()})
                relation = ''
            subject = ''
        elif token == "<subj>":
            current = 's'
            if relation != '':
                triplets.append({'head': subject.strip(), 'type': relation.strip(),'tail': object_.strip()})
            object_ = ''
        elif token == "<obj>":
            current = 'o'
            relation = ''
        else:
            if current == 't':
                subject += ' ' + token
            elif current == 's':
                object_ += ' ' + token
            elif current == 'o':
                relation += ' ' + token
    if subject != '' and relation != '' and object_ != '':
        triplets.append({'head': subject.strip(), 'type': relation.strip(),'tail': object_.strip()})
    return triplets
extracted_triplets = extract_triplets(extracted_text[0])
print(extracted_triplets)
```

## Model and Tokenizer using transformers

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def extract_triplets(text):
    triplets = []
    relation, subject, relation, object_ = '', '', '', ''
    text = text.strip()
    current = 'x'
    for token in text.replace("<s>", "").replace("<pad>", "").replace("</s>", "").split():
        if token == "<triplet>":
            current = 't'
            if relation != '':
                triplets.append({'head': subject.strip(), 'type': relation.strip(),'tail': object_.strip()})
                relation = ''
            subject = ''
        elif token == "<subj>":
            current = 's'
            if relation != '':
                triplets.append({'head': subject.strip(), 'type': relation.strip(),'tail': object_.strip()})
            object_ = ''
        elif token == "<obj>":
            current = 'o'
            relation = ''
        else:
            if current == 't':
                subject += ' ' + token
            elif current == 's':
                object_ += ' ' + token
            elif current == 'o':
                relation += ' ' + token
    if subject != '' and relation != '' and object_ != '':
        triplets.append({'head': subject.strip(), 'type': relation.strip(),'tail': object_.strip()})
    return triplets

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Babelscape/rebel-large")
model = AutoModelForSeq2SeqLM.from_pretrained("Babelscape/rebel-large")
gen_kwargs = {
    "max_length": 256,
    "length_penalty": 0,
    "num_beams": 3,
    "num_return_sequences": 3,
}

# Text to extract triplets from
text = 'Punta Cana is a resort town in the municipality of Higüey, in La Altagracia Province, the easternmost province of the Dominican Republic.'

# Tokenizer text
model_inputs = tokenizer(text, max_length=256, padding=True, truncation=True, return_tensors = 'pt')

# Generate
generated_tokens = model.generate(
    model_inputs["input_ids"].to(model.device),
    attention_mask=model_inputs["attention_mask"].to(model.device),
    **gen_kwargs,
)

# Extract text
decoded_preds = tokenizer.batch_decode(generated_tokens, skip_special_tokens=False)

# Extract triplets
for idx, sentence in enumerate(decoded_preds):
    print(f'Prediction triplets sentence {idx}')
    print(extract_triplets(sentence))
```
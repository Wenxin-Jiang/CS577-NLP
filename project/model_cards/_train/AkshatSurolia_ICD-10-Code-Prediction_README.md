---
license: apache-2.0
tags:
- text-classification
datasets:
- Mimic III
---

# Clinical BERT for ICD-10 Prediction

The Publicly Available Clinical BERT Embeddings paper contains four unique clinicalBERT models: initialized with BERT-Base (cased_L-12_H-768_A-12) or BioBERT (BioBERT-Base v1.0 + PubMed 200K + PMC 270K) & trained on either all MIMIC notes or only discharge summaries.  
 
---

## How to use the model

Load the model via the transformers library:

    from transformers import AutoTokenizer, BertForSequenceClassification
    tokenizer = AutoTokenizer.from_pretrained("AkshatSurolia/ICD-10-Code-Prediction")
    model = BertForSequenceClassification.from_pretrained("AkshatSurolia/ICD-10-Code-Prediction")
    config = model.config

Run the model with clinical diagonosis text:

    text = "subarachnoid hemorrhage scalp laceration service: surgery major surgical or invasive"
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)

Return the Top-5 predicted ICD-10 codes:

    results = output.logits.detach().cpu().numpy()[0].argsort()[::-1][:5]
    return [ config.id2label[ids] for ids in results]
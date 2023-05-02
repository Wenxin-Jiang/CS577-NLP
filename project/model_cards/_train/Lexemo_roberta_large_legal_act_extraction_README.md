---
language: en
license: mit
metrics:
- seqeval
widget:
- text: "When Member States adopt those measures, they shall contain a reference to this Directive or be accompanied by such reference on the occasion of their official publication. They shall also include a statement that references in existing laws, regulations and administrative provisions to Article 9 of Directive 97/23/EC shall be construed as references to Article 13 of this Directive. Member States shall determine how such reference is to be made and how that statement is to be formulated."
  example_title: "Example 1"
- text: "2. Member States shall adopt and publish, by 18 July 2016, the laws, regulations and administrative provisions necessary to comply with Article 2(15) to (32), Articles 6 to 12, 14, 17 and 18, Article 19(3) to (5), Articles 20 to 43, 47 and 48 and Annexes I, II, III and IV. They shall forthwith communicate the text of those measures to the Commission."
  example_title: "Example 2"
- text: "When applying Article 84(1), point (a), of Regulation (EU) No 575/2013 (CRR) in respect of subsidiary institutions in third countries, should the excess capital attributable to minorities be determined by applying, namely in subparagraph (i), the provisions and requirements of CRR, together with any additional local requirements, to the extent these have to be met with CET1 capital? Although the wording of Article 84(1)(a)(i) CRR seems clear, different interpretations have arisen as to how it applies in practice, particularly in the case of third country institutions operating under a regulatory framework different from CRD IV/CRR."
  example_title: "Example 3"

---

# Legal act Extraction Model

With growing legal complexity keeping track of changes in interconnectivity and hierarchical structure of the legislation is a challenging task. Entity extraction technique (also known as token classification) facilitates document analysis by assigning a label to each word in a text. 

A way to decide which data elements are to be extracted and how they should be labeled mostly depends on a particular business problem and is limited only by a tokenization process meaning that an element shouldn’t be less than a token as split by a tokenizer. So as long as these data elements correspond to at least one whole token they could represent legal terms, legal entities, legal parties, deadlines and so on. 

This model is fine-tuned to label mentioned legal acts and their articles. Extracted information could be used to create an interconnectivity map for legal acts.

## Model Description

This model is a fine-tuned checkpoint of [RoBERTa-large](https://huggingface.co/roberta-large).
More details about RoBERTa large are available in [RoBERTa large model card](https://huggingface.co/roberta-large).

| Id       | Label                                      | Description                                                             |
| -------- | ------------------------------------------ | ----------------------------------------------------------------------- | 
| 0        | O                                          | Not a legal act and not an article                                      | 
| 1        | abbreviation_relevant_following_act        | A legal act abbreviation relevant to the following legal act            | 
| 2        | abbreviation_relevant_previous_act         | A legal act abbreviation relevant to a previously mentioned legal act   | 
| 3        | another_act                                | A legal act                                                             | 
| 4        | another_act_abbreviation                   | A legal act mentioned as an abbreviation                                | 
| 5        | another_act_equal_previous_act             | An assumed legal act introduced previously                              | 
| 6        | another_act_sequence_end                   | Inside a sequence of legal acts                                         | 
| 7        | another_act_sequence_start                 | At the beginning of a sequence of legal acts                            | 
| 8        | another_article_equal_previous_article     | An assumed article introduced previously                                | 
| 9        | article_current                            | An article mentioning itself                                            | 
| 10       | article_relevant_current_act               | An article of the same legal act as the one being processed             | 
| 11       | article_relevant_current_act_range_end     | A range end of articles belonging to the current act                    | 
| 12       | article_relevant_current_act_range_start   | A range start of articles belonging to the current act                  | 
| 13       | article_relevant_following_act             | An article of a following legal act                                     | 
| 15       | article_relevant_following_act_range_end   | A range end of articles belonging to a following act                    | 
| 16       | article_relevant_following_act_range_start | A range start of articles belonging to a following legal act            | 
| 17       | article_relevant_previous_act              | An article of a previously mentioned legal act                          | 
| 18       | article_relevant_previous_act_range_end    | A range end of articles belonging to a previously mentioned legal act   | 
| 19       | article_relevant_previous_act_range_start  | A range start of articles belonging to a previously mentioned legal act | 
| 20       | current_act                                | A legal act mentioning itself                                           | 
| 21       | treaty_abbreviation                        | A treaty mentioned as an abbreviation                                   | 
| 22       | treaty_name                                | A treaty                                                                | 
| 23       | service_label                              | A token comprising more than 1 label                                    | 

## Intended Uses & Limitations 
The model could be used to extract mentioned legal acts and their articles.

### Limitations
This legal-act extraction model is very domain-specific and will perform well on legal texts. It's not recommended to use this model for other domains, but you are free to test it out.
It was intended for English documents only.

### How To Use
```python
from transformers import (
    TokenClassificationPipeline,
    RobertaForTokenClassification,
    RobertaTokenizerFast,
)

legal_act_extraction_model = RobertaForTokenClassification.from_pretrained(
    'Lexemo/roberta_large_legal_act_extraction')
tokenizer = RobertaTokenizerFast.from_pretrained("roberta-large")
pypeline = TokenClassificationPipeline(model=legal_act_extraction_model, 
                                        tokenizer=tokenizer, 
                                        aggregation_strategy='simple')

```
```python
# Inference
import pandas as pd
from tabulate import tabulate

text = """When Member States adopt those measures, they shall contain a 
reference to this Directive or be accompanied by such reference on the 
occasion of their official publication. They shall also include a statement 
that references in existing laws, regulations and administrative provisions 
to Article 9 of Directive 97/23/EC shall be construed as references to 
Article 13 of this Directive. Member States shall determine how such 
reference is to be made and how that statement is to be formulated."""

entities = pypeline(text)
df = pd.DataFrame(entities)
print(tabulate(df, showindex=True, headers=df.columns))
```

```
# Output
    entity_group                       score  word                  start    end
--  ------------------------------  --------  ------------------  -------  -----
 0  current_act                     0.999999  Directive                80     89
 1  article_relevant_following_act  0.999995  9                       296    297
 2  another_act                     0.999999  Directive 97/23/EC      301    319
 3  article_relevant_following_act  0.999996  13                      364    366
 4  current_act                     0.999999  Directive               375    384

```

## Fine-tuning hyper-parameters

- learning_rate = 2e-5
- batch_size = 4
- weight_decay=0.01
- max_seq_length = 514
- num_train_epochs = 56

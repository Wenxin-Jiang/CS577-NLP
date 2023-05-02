---
language: en
widget:
- text: "translate English to SQL: Tell me a feel good story over last day"
  example_title: Last day 1
- text: "translate English to SQL: feel good story since yesterday"
  example_title: Last day 2
- text: "translate English to SQL: Show me sports stories since yesterday with team equal Red Sox"
  example_title: Last day with filter
- text: "translate English to SQL: Breaking news summarized"
  example_title: Summary
- text: "translate English to SQL: Breaking news translated to fr"
  example_title: Translate to French
inference:
  parameters:
    max_length: 512
license: apache-2.0
library_name: txtai
---

# T5-small finedtuned to generate txtai SQL

[T5 small](https://huggingface.co/t5-small) fine-tuned to generate [txtai](https://github.com/neuml/txtai) SQL. This model takes natural language queries and builds txtai-compatible SQL statements.

txtai supports both natural language queries

```
Tell me a feel good story
Show me stories about wildlife
Sports stories about hockey
```

and SQL statements

```
select * from txtai where similar("Tell me a feel good story") and
entry >= date('now', '-1 day')
```

This model bridges the gap between the two and enables natural language queries with filters.

```
Tell me a feel good story since yesterday
Show me sports stories since yesterday with team equal Red Sox
Breaking news summarized
Breaking news translated to fr
```

## Custom query syntax

This model is an example of creating a custom query syntax that can be translated into SQL txtai can understand. Any query syntax can be created. This one supports English but a similar strategy can be deployed to support other languages. Natural language can be translated to functions, query clauses, column selection and more. 

See [t5-small-bashsql](https://huggingface.co/NeuML/t5-small-bashsql) for a model that translates Bash like commands into txtai SQL.

## Model training

This model was trained using scripts that can be [found here](https://github.com/neuml/txtai/tree/master/models/txtsql).

Steps to train:

```bash
python generate.py txtsql.csv
python train.py txtsql.csv t5-small-txtsql
```

---
language: en
widget:
- text: "translate Bash to SQL: find -name \"feel good story\" -mtime -1"
  example_title: Last day
- text: "translate Bash to SQL: find -name \"show me sports stories\" -mtime -1 -team \"Red Sox\""
  example_title: Last day with filter
- text: "translate Bash to SQL: find -name \"breaking news\" -summary"
  example_title: Summary
- text: "translate Bash to SQL: find -name \"breaking news\" -translate fr"
  example_title: Translate to French
inference:
  parameters:
    max_length: 512
license: apache-2.0
library_name: txtai
---

# T5-small finedtuned to generate txtai SQL

[T5 small](https://huggingface.co/t5-small) fine-tuned to generate [txtai](https://github.com/neuml/txtai) SQL. This model takes [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) like commands and builds txtai-compatible SQL statements.

```
find -name "feel good story" -mtime -1
find -name "show me sports stories" -mtime -1 -team \"Red Sox\"
find -name "breaking news" -summary
find -name "breaking news" -translate fr
```

## Custom query syntax

This model is an example of creating a custom query syntax that can be translated into SQL txtai can understand. Any query syntax can be created. This one supports Bash-like commands but a similar strategy can be deployed to support other languages. Natural language can be translated to functions, query clauses, column selection and more.

See [t5-small-txtsql](https://huggingface.co/NeuML/t5-small-txtsql) for a model that translates natural language statements into txtai SQL.

## Model training

This model was trained using scripts that can be [found here](https://github.com/neuml/txtai/tree/master/models/bashsql).

Steps to train:

```bash
python generate.py bashsql.csv
python train.py bashsql.csv t5-small-bashsql
```

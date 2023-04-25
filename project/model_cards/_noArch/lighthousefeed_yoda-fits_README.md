---
tags:
- autotrain
- summarization
language:
- es
widget:
- text: "Goodthreads Camiseta Entallada de Algodón con Manga Corta, Cuello Redondo y Bolsillo Hombre"
datasets:
- gazquez/autotrain-data-yoda-fits
co2_eq_emissions:
  emissions: 18.026996827523217
---

# What is YODA

YODA is a series of models for Google Feed product optimization. We aim to increase the market reach for ecommerce by augmenting and improving certain metadata like short titles, colors, measures and more. YODA is being used in production by +300 companies with +3.5M products.

## FITS - First Intergalactic Title Shortener

Trained with more than 2M lines of long and short titles from real products, the FITS model is capable of extracting the key features of an already short text. It generates a short title for better SEM (Search Engine Marketing) and product position in google indexes.

### The problem with product titles

Product titles are not long text with a common sense or clear context. Words in product titles may be disorganized or may not make sense at all. 
Detecting context or meaning in short sentences raises a problem and with abstractive summarization, we may see certain decorations or errors on the model output.

To palliate that problem we run some post-processing on our model later on our custom API. You may contact [Iván R. Gázquez](mailto:ivan@gazquez.com) (lead ML developer) for any problem or inquiry.

## Validation Metrics

- Loss: 1.179
- Rouge1: 62.134
- Rouge2: 40.392
- RougeL: 60.269
- RougeLsum: 60.293
- Gen Len: 9.153

## Usage

You can use cURL to access this model:

```
$ curl -X POST -H "Authorization: Bearer YOUR_HUGGINGFACE_API_KEY" -H "Content-Type: application/json" -d '{"inputs": "I love AutoTrain"}' https://api-inference.huggingface.co/gazquez/autotrain-yoda-fits-1539355334
```
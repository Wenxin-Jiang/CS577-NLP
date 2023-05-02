---
language: es
tags:
- summarization
- sagemaker
- mt5
- spanish
license: apache-2.0
datasets:
- mlsum - es
model-index:
- name: mt5-small-mlsum
  results:
  - task: 
      type: summarization  # Required. Example: automatic-speech-recognition
      name: abstractive summarization  # Optional. Example: Speech Recognition
    dataset:
      type: mlsum  # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: mlsum-es  # Required. Example: Common Voice zh-CN
      args: es         # Optional. Example: zh-CN
    metrics:
       - name: rouge1
         type: rouge1
         value: 26.0756
       - name: rouge2
         type: rouge2
         value: 8.4669
       - name: rougeL
         type: rougeL
         value: 20.8167
       - name: rougeLsum
         type: rougeLsum
         value: 21.0822
widget:
   - text: "La chocotorta, el tradicional y práctico antojo dulce de los argentinos, fue elegida como el mejor postre del mundo por críticos de restaurants internacionales, a casi 40 años de su creación. El ránking Taste Atlas ubicó primero en su lista al postre insignia local de galletitas, queso crema y dulce de leche, por delante del helado de pistacho italiano y la tarta alemana de manzana. “Este postre argentino sin hornear fue influenciado por la cocina italiana y se inspiró en el famoso tiramisú italiano. Está elaborado con tres ingredientes básicos argentinos: galletas de chocolate, dulce de leche y queso crema”, explica la página web que exhorta a los turistas de todo el mundo a que prueben la chocotorta. En la votación, superó también a los waffles belgas y el zserbó húngaro. A nivel local le sigue el alfajor, con 4,2 puntos contra los 4,7 de la torta. En el texto que acompaña al listón dorado de “postre número uno“, los expertos enseñan además cómo se hacen las chocotortas, paso por paso. “Las galletas se ablandan en leche y se cubren con una combinación de queso crema y dulce de leche. Las formas de la chocotorta pueden variar, mientras que las galletas se pueden remojar con leche con chocolate, café o incluso licor de café”, detallan. Por último, adjudican su creación a una “campaña de márketing” diseñada para promover las galletitas icónicas que le dan su nombre. La chocotorta, infaltable en los cumpleaños argentinos, fue creada en 1982 por una creativa de las agencias más importantes del país, Marité Mabragaña."
---
## mt5-small-mlsum
This model was trained on the Spanish section of MLSum: https://paperswithcode.com/sota/abstractive-text-summarization-on-mlsum based on mt5-small.

## Hyperparameters
{
    "dataset_config": "es",
    "dataset_name": "mlsum",
    "do_eval": true,
    "do_predict": true,
    "do_train": true,
    "fp16": true,
    "max_target_length": 64,
    "model_name_or_path": "google/mt5-small",
    "num_train_epochs": 10,
    "output_dir": "/opt/ml/checkpoints",
    "per_device_eval_batch_size": 4,
    "per_device_train_batch_size": 4,
    "predict_with_generate": true,
    "sagemaker_container_log_level": 20,
    "sagemaker_program": "run_summarization.py",
    "save_strategy": "epoch",
    "seed": 7,
    "summary_column": "summary",
    "text_column": "text"
}
## Usage

```
article = """ La chocotorta, el tradicional y práctico antojo dulce de los argentinos, fue elegida como el mejor postre del mundo por críticos de restaurants internacionales, a casi 40 años de su creación. El ránking Taste Atlas ubicó primero en su lista al postre insignia local de galletitas, queso crema y dulce de leche, por delante del helado de pistacho italiano y la tarta alemana de manzana. “Este postre argentino sin hornear fue influenciado por la cocina italiana y se inspiró en el famoso tiramisú italiano. Está elaborado con tres ingredientes básicos argentinos: galletas de chocolate, dulce de leche y queso crema”, explica la página web que exhorta a los turistas de todo el mundo a que prueben la chocotorta. En la votación, superó también a los waffles belgas y el zserbó húngaro. A nivel local le sigue el alfajor, con 4,2 puntos contra los 4,7 de la torta. En el texto que acompaña al listón dorado de “postre número uno", los expertos enseñan además cómo se hacen las chocotortas, paso por paso. “Las galletas se ablandan en leche y se cubren con una combinación de queso crema y dulce de leche. Las formas de la chocotorta pueden variar, mientras que las galletas se pueden remojar con leche con chocolate, café o incluso licor de café”, detallan. Por último, adjudican su creación a una “campaña de márketing” diseñada para promover las galletitas icónicas que le dan su nombre. La chocotorta, infaltable en los cumpleaños argentinos, fue creada en 1982 por una creativa de las agencias más importantes del país, Marité Mabragaña.  """

from transformers import pipeline
summarizer = pipeline("summarization", model="LeoCordoba/mt5-small-mlsum")
summarizer(article, min_length=5, max_length=64)
```
result: [{'summary_text': 'El ránking Taste Atlas ubicó primero en su lista al postre insignia local de galletitas, queso crema y dulce de leche'}]

## Results
| metric | score |
| --- | ----- |
| eval_rouge1 | 26.4352 |
| eval_rouge2 | 8.9293 |
| eval_rougeL | 21.2622 |
| eval_rougeLsum | 21.5518 |
| test_rouge1 | 26.0756 |
| test_rouge2 | 8.4669 |
| test_rougeL | 20.8167 |
| test_rougeLsum | 21.0822 |

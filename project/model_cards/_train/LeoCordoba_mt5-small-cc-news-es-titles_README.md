---

language: es

tags:

- summarization

- mt5

- spanish

license: apache-2.0

datasets:

- LeoCordoba/CC-NEWS-ES-titles

model-index:
- name: mt5-small-ccnews-titles-es
  results:
  - task: 
      name: Abstractive Text Summarization
      type: abstractive-text-summarization

    dataset:
      name: "CCNEWS-ES-titles" 
      type: LeoCordoba/CC-NEWS-ES-titles
      
    metrics:
       - name: Validation ROGUE-1
         type: rogue-1
         value: 22.6623
       - name: Validation ROGUE-2
         type: rogue-2
         value: 7.7894
       - name: Validation ROGUE-L
         type: rogue-l
         value: 19.8015
       - name: Validation ROGUE-Lsum
         type: rogue-lsum
         value: 19.8092
       - name: Test ROGUE-1
         type: rogue-1
         value: 22.9263
       - name: Test ROGUE-2
         type: rogue-2
         value: 7.9146
       - name: Test ROGUE-L
         type: rogue-l
         value: 20.0272
       - name: Test ROGUE-Lsum
         type: rogue-lsum
         value: 20.0387
        
widget:

   - text: "La chocotorta, el tradicional y práctico antojo dulce de los argentinos, fue elegida como el mejor postre del mundo por críticos de restaurants internacionales, a casi 40 años de su creación. El ránking Taste Atlas ubicó primero en su lista al postre insignia local de galletitas, queso crema y dulce de leche, por delante del helado de pistacho italiano y la tarta alemana de manzana. “Este postre argentino sin hornear fue influenciado por la cocina italiana y se inspiró en el famoso tiramisú italiano. Está elaborado con tres ingredientes básicos argentinos: galletas de chocolate, dulce de leche y queso crema”, explica la página web que exhorta a los turistas de todo el mundo a que prueben la chocotorta. En la votación, superó también a los waffles belgas y el zserbó húngaro. A nivel local le sigue el alfajor, con 4,2 puntos contra los 4,7 de la torta. En el texto que acompaña al listón dorado de “postre número uno“, los expertos enseñan además cómo se hacen las chocotortas, paso por paso. “Las galletas se ablandan en leche y se cubren con una combinación de queso crema y dulce de leche. Las formas de la chocotorta pueden variar, mientras que las galletas se pueden remojar con leche con chocolate, café o incluso licor de café”, detallan. Por último, adjudican su creación a una “campaña de márketing” diseñada para promover las galletitas icónicas que le dan su nombre. La chocotorta, infaltable en los cumpleaños argentinos, fue creada en 1982 por una creativa de las agencias más importantes del país, Marité Mabragaña."

---

## Hyperparameters

{

    "max_target_length": 64,

    "model_name_or_path": "google/mt5-small",

    "num_train_epochs": 3,

    "seed": 7,

    "summary_column": "output_text",

    "text_column": "text",

    "encoder_max_length" : 512,

    "decoder_max_length" :36,

    "batch_size" : 128

}

## Usage

```
article = """ La chocotorta, el tradicional y práctico antojo dulce de los argentinos, fue elegida como el mejor postre del mundo por críticos de restaurants internacionales, a casi 40 años de su creación. El ránking Taste Atlas ubicó primero en su lista al postre insignia local de galletitas, queso crema y dulce de leche, por delante del helado de pistacho italiano y la tarta alemana de manzana. “Este postre argentino sin hornear fue influenciado por la cocina italiana y se inspiró en el famoso tiramisú italiano. Está elaborado con tres ingredientes básicos argentinos: galletas de chocolate, dulce de leche y queso crema”, explica la página web que exhorta a los turistas de todo el mundo a que prueben la chocotorta. En la votación, superó también a los waffles belgas y el zserbó húngaro. A nivel local le sigue el alfajor, con 4,2 puntos contra los 4,7 de la torta. En el texto que acompaña al listón dorado de “postre número uno", los expertos enseñan además cómo se hacen las chocotortas, paso por paso. “Las galletas se ablandan en leche y se cubren con una combinación de queso crema y dulce de leche. Las formas de la chocotorta pueden variar, mientras que las galletas se pueden remojar con leche con chocolate, café o incluso licor de café”, detallan. Por último, adjudican su creación a una “campaña de márketing” diseñada para promover las galletitas icónicas que le dan su nombre. La chocotorta, infaltable en los cumpleaños argentinos, fue creada en 1982 por una creativa de las agencias más importantes del país, Marité Mabragaña.  """

from transformers import pipeline

summarizer = pipeline("summarization", model="LeoCordoba/mt5-small-ccnews-titles-es")

summarizer(article, min_length=5, max_length=64)

```
## Results
| metric | score |
| --- | ----- |
| eval_loss | 2.879085063934326 |
| eval_rouge1 | 22.6623 |
| eval_rouge2 | 7.7894 |
| eval_rougeL | 19.8015, |
| eval_rougeLsum | 19.8092 |
| eval_gen_len | 17.1839 |
| test_loss | 2.878429412841797 |
| test_rouge1 | 22.9263 |
| test_rouge2 | 7.9146 |
| test_rougeL | 20.0272 |
| test_rougeLsum | 20.0387 |
| test_gen_len | 17.1696 |
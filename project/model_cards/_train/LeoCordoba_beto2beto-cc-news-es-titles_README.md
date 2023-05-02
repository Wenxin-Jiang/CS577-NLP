---
language: es
tags:
- summarization
- spanish
- beto2beto
- encoder-decoder
license: apache-2.0
datasets:
- LeoCordoba/CC-NEWS-ES-titles
model-index:
- name: beto2beto-ccnews-titles-es
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
         value: 23.7478
       - name: Validation ROGUE-2
         type: rogue-2
         value: 7.3616
       - name: Validation ROGUE-L
         type: rogue-l
         value: 20.6615
       - name: Validation ROGUE-Lsum
         type: rogue-lsum
         value: 20.7371
       - name: Test ROGUE-1
         type: rogue-1
         value: 23.7415
       - name: Test ROGUE-2
         type: rogue-2
         value: 7.3548
       - name: Test ROGUE-L
         type: rogue-l
         value: 20.746
       - name: Test ROGUE-Lsum
         type: rogue-lsum
         value: 20.8149
         
widget:
- text: | 
    La chocotorta, el tradicional y práctico antojo dulce de los argentinos, fue elegida como el mejor postre del mundo por críticos de restaurants internacionales, a casi 40 años de su creación. El ránking Taste Atlas ubicó primero en su lista al postre insignia local de galletitas, queso crema y dulce de leche, por delante del helado de pistacho italiano y la tarta alemana de manzana. “Este postre argentino sin hornear fue influenciado por la cocina italiana y se inspiró en el famoso tiramisú italiano. Está elaborado con tres ingredientes básicos argentinos: galletas de chocolate, dulce de leche y queso crema”, explica la página web que exhorta a los turistas de todo el mundo a que prueben la chocotorta. En la votación, superó también a los waffles belgas y el zserbó húngaro. A nivel local le sigue el alfajor, con 4,2 puntos contra los 4,7 de la torta. En el texto que acompaña al listón dorado de “postre número uno“, los expertos enseñan además cómo se hacen las chocotortas, paso por paso. “Las galletas se ablandan en leche y se cubren con una combinación de queso crema y dulce de leche. Las formas de la chocotorta pueden variar, mientras que las galletas se pueden remojar con leche con chocolate, café o incluso licor de café”, detallan. Por último, adjudican su creación a una “campaña de márketing” diseñada para promover las galletitas icónicas que le dan su nombre. La chocotorta, infaltable en los cumpleaños argentinos, fue creada en 1982 por una creativa de las agencias más importantes del país, Marité Mabragaña.

---
## Hyperparameters


{

    "num_train_epochs": 3,

    "seed": 7,

    "summary_column": "output_text",

    "text_column": "text",

    "encoder_max_length" : 512,

    "decoder_max_length" :36,

    "batch_size" : 256

}
## Usage

## Results
| key | value |
| --- | ----- |
| eval loss | 4.539857387542725|
| eval_rouge1 |23.7478  |
| eval_rouge2 |7.3616 |
| eval_rougeL |20.6615 |
| eval_rougeLsum |20.7371 |
| eval_gen_len| 16.1806|
|test loss | 4.515065670013428|
| test_rouge1 | 23.7415|
| test_rouge2 | 7.3548|
| test_rougeL | 20.746|
| test_rougeLsum | 20.8149|
| test_gen_len| 16.1926|


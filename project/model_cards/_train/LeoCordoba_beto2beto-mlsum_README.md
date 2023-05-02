---
language: es
tags:
- summarization
- spanish
- encoder-decoder
- beto
license: apache-2.0
datasets:
- mlsum - es
model-index:
- name: beto2beto-mlsum
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
         value: 25.8639
       - name: rouge2
         type: rouge2
         value: 8.911
       - name: rougeL
         type: rougeL
         value: 21.2426
       - name: rougeLsum
         type: rougeLsum
         value: 21.5859
widget:
- text: | 
    La chocotorta, el tradicional y práctico antojo dulce de los argentinos, fue elegida como el mejor postre del mundo por críticos de restaurants internacionales, a casi 40 años de su creación. El ránking Taste Atlas ubicó primero en su lista al postre insignia local de galletitas, queso crema y dulce de leche, por delante del helado de pistacho italiano y la tarta alemana de manzana. “Este postre argentino sin hornear fue influenciado por la cocina italiana y se inspiró en el famoso tiramisú italiano. Está elaborado con tres ingredientes básicos argentinos: galletas de chocolate, dulce de leche y queso crema”, explica la página web que exhorta a los turistas de todo el mundo a que prueben la chocotorta. En la votación, superó también a los waffles belgas y el zserbó húngaro. A nivel local le sigue el alfajor, con 4,2 puntos contra los 4,7 de la torta. En el texto que acompaña al listón dorado de “postre número uno", los expertos enseñan además cómo se hacen las chocotortas, paso por paso. “Las galletas se ablandan en leche y se cubren con una combinación de queso crema y dulce de leche. Las formas de la chocotorta pueden variar, mientras que las galletas se pueden remojar con leche con chocolate, café o incluso licor de café”, detallan. Por último, adjudican su creación a una “campaña de márketing” diseñada para promover las galletitas icónicas que le dan su nombre. La chocotorta, infaltable en los cumpleaños argentinos, fue creada en 1982 por una creativa de las agencias más importantes del país, Marité Mabragaña.

---
## beto2beto-mlsum
This model was trained on the Spanish section of MLSum: https://paperswithcode.com/sota/abstractive-text-summarization-on-mlsum.

## Hyperparameters
    {
    "dataset_config": "es",
    "dataset_name": "mlsum",
    "do_eval": true,
    "do_predict": true,
    "do_train": true,
    "fp16": true,
    "max_target_length": 64,
    "num_train_epochs": 10,
    "per_device_eval_batch_size": 4,
    "per_device_train_batch_size": 4,
    "predict_with_generate": true,
    "sagemaker_container_log_level": 20,
    "sagemaker_program": "run_summarization.py",
    "seed": 7,
    "summary_column": "summary",
    "text_column": "text"
}
## Usage
## Results
| metric | score |
| --- | ----- |
| validation_loss | 2.5021677017211914 |
| validation_rouge1 | 26.1256 |
| validation_rouge2 | 9.2552 |
| validation_rougeL | 21.4899 |
| validation_rougeLsum | 21.8194 |
| test_loss | 2.57672381401062 |
| test_rouge1 | 25.8639 |
| test_rouge2 | 8.911 |
| test_rougeL | 21.2426 |
| test_rougeLsum | 21.5859 |

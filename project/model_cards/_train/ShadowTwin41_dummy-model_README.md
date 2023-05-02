---
language: fr
license: mit
datasets:
- oscar
---

## Start with 
* Model description
  -> The model description provides basic details about the model. This includes the architecture, version, if it was introduced in a paper, if an original implementation is available, the author, and general information about the model. Any copyright should be attributed here. General information about training procedures, parameters, and important disclaimers can also be mentioned in this section.
  
* Intended uses & limitations
  -> Here you describe the use cases the model is intended for, including the languages, fields, and domains where it can be applied. This section of the model card can also document areas that are known to be out of scope for the model, or where it is likely to perform suboptimally.
  
* How to use
  -> This section should include some examples of how to use the model. This can showcase usage of the pipeline() function, usage of the model and tokenizer classes, and any other code you think might be helpful.
  
* Limitations and bias
  -> This part should indicate which dataset(s) the model was trained on. A brief description of the dataset(s) is also welcome.
  
* Training data
  -> In this section you should describe all the relevant aspects of training that are useful from a reproducibility perspective. This includes any preprocessing and postprocessing that were done on the data, as well as details such as the number of epochs the model was trained for, the batch size, the learning rate, and so on.
  
* Training procedure
  -> Here you should describe the metrics you use for evaluation, and the different factors you are mesuring. Mentioning which metric(s) were used, on which dataset and which dataset split, makes it easy to compare you model’s performance compared to that of other models. These should be informed by the previous sections, such as the intended users and use cases.
  
* Evaluation results
  -> Finally, provide an indication of how well the model performs on the evaluation dataset. If the model uses a decision threshold, either provide the decision threshold used in the evaluation, or provide details on evaluation at different thresholds for the intended uses.
  
  https://github.com/huggingface/hub-docs/blame/main/modelcard.md
---
license: cc-by-nc-4.0
---
This model is a fine-tuned version of RoBERTa-large [1]. It was trained on 1,400 employee reviews to measure corporate culture. More specifically, it measures the **culture dimension “clan”** of the Competing Values Framework [2,3]. An organization that exhibits a clan culture is characterized by an emphasis to **collaborate** [2]. 

The model assigns one of three possible labels:

0 (**neutral**): Text does not allow any inference about a clan culture. <br />
1 (**positive**): Text contains information in line with a clan culture. <br />
2 (**negative**): Text contains information in opposite to a clan culture. <br />


For details on the model and its performance, see Koch and Pasch (2022). Please cite this article when using the model: <br />
Koch, Sebastian; Pasch, Stefan (2022): CultureBERT: Fine-Tuning Transformer Based Language Models for Corporate Culture. Available online at http://arxiv.org/abs/2212.00509.

Please see the following **tutorial** on how to apply CultureBERT to measure corporate culture in your own text documents: https://github.com/Stefan-Pasch/CultureBERT

Other References:

[1] Liu, Y.; Ott, M.; Goyal, N.; Du, J.; Joshi, M.; Chen, D.; ... & Stoyanov, V. (2019). Roberta: A robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692. 

[2] Cameron, Kim S.; Quinn, Robert E. (2011): Diagnosing and Changing Organizational Culture. Based on the Competing Values Framework. 3rd ed. San Francisco (CA): Jossey-Bass.

[3] Quinn, Robert E.; Rohrbaugh, John (1983): A Spatial Model of Effectiveness Criteria: Towards a Competing Values Approach to Organizational Analysis. In Management Science 29 (3), pp. 363–377. DOI: 10.1287/mnsc.29.3.363.

---
tags:
- autotrain
- summarization
language:
- en
widget:
- text: "Positivity towards meat consumption remains strong, despite evidence of negative environmental and ethical outcomes. Although awareness of these repercussions is rising, there is still public resistance to removing meat from our diets. One potential method to alleviate these effects is to produce in vitro meat: meat grown in a laboratory that does not carry the same environmental or ethical concerns. However, there is limited research examining public attitudes towards in vitro meat, thus we know little about the capacity for it be accepted by consumers. This study aimed to examine perceptions of in vitro meat and identify potential barriers that might prevent engagement. Through conducting an online survey with US participants, we identified that although most respondents were willing to try in vitro meat, only one third were definitely or probably willing to eat in vitro meat regularly or as a replacement for farmed meat. Men were more receptive to it than women, as were politically liberal respondents compared with conservative ones. Vegetarians and vegans were more likely to perceive benefits compared to farmed meat, but they were less likely to want to try it than meat eaters. The main concerns were an anticipated high price, limited taste and appeal and a concern that the product was unnatural. It is concluded that people in the USA are likely to try in vitro meat, but few believed that it would replace farmed meat in their diet."
datasets:
- vegancreativecompass/autotrain-data-scitldr-for-vegan-studies
co2_eq_emissions:
  emissions: 57.779835625872906
---
# About This Model

This model has been trained to take abstracts of scientific studies about veganism & animal rights and turn them into single-sentence takeaways for vegan businesses and animal activists to apply to their activism. The dataset was curated by scraping TLDRs and abstracts from Semantic Scholar and having vegan activists and marketing professionals from VEG3 review the usefulness of a random sample of the dataset to ensure their relevance to vegan businesses and animal activists.


# Model Trained Using AutoTrain

- Problem type: Summarization
- Model ID: 1923365100
- CO2 Emissions (in grams): 57.7798

## Validation Metrics

- Loss: 0.711
- Rouge1: 44.317
- Rouge2: 30.335
- RougeL: 41.369
- RougeLsum: 41.198
- Gen Len: 17.855

## Usage

You can use cURL to access this model:

```
curl https://api-inference.huggingface.co/models/VEG3/TLDR-Vegan-Studies \
	-X POST \
	-d '{"inputs":"ABSTRACT"}' \
	-H "Authorization: Bearer YOURAPIKEY"

```
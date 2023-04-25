---
license: mit
language:
- en
library_name: tensorflowtts
pipeline_tag: reinforcement-learning
---
Model used for solving Capacitated Vehicle Routing Problem (CVRP). The CVRP is a variant of the vehicle routing problem (VRP) in which vehicles have a limited carrying capacity and must visit a set of customer locations to deliver or collect items.
Model is based on GitHub repo [HERE](https://github.com/d-eremeev/ADM-VRP), and was used for medium.com article **"Vaccine Supply Chain Optimization with AI-Powered Capacitated Vehicle Routing Problem(CVRP)"**.

**Dynamic Attention Model (AM-D) Approach**:
After vehicle returns to depot, the remaining nodes could be considered as a new (smaller) instance (graph) to be solved.
Idea: update embedding of the remaining nodes using encoder after agent arrives back to depot.
**Implementation**:
- Force RL agent to wait for others once it arrives to .
- When every agent is in depot, apply encoder with mask to the whole batch.


If you want to train your own model with AM-D approach:
1. Prepare data (depo location Lat/Long, nodes location Lat/Long and capacity of the vehicles)
2. Transform data with TensorFlow tranform_to_tensor [Here is Gist](https://gist.github.com/PiotrKrosniak/f488eea5b31a2d61e21554041a1ee59b) example with transforming from Pandas Data Frame
3. Train the model using 

![alt text](https://huggingface.co/peterkros/cvrp-model/blob/main/newplot.png)



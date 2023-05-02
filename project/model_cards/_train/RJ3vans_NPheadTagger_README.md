Input a noun phrase (NP) and the model will tag its syntactic head as HEAD.
Non-head tokens will be tagged as NA.

The model is intended to tag multiple heads in compound NPs. It is not 
intended to tag all heads in complex NPs.

The training data is derived from a dataset in which NPs are identified 
using the Berkeley neural parser which does not identify the heads of 
syntactic constituents. The training data includes erroneous NPs in 
which each token is tagged as ERROR.

Examples you might try include:

The bottle of ginger beer

John, Peter, and Mary, who lives in Sri Lanka

The man who won the race
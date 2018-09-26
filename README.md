# TF_IDF_IR_System
A Python implementation of a TF-IDF domain specific News retrieval system based on input keywords.

To compile and run the python code, first have python installed along with the NLTK library. Then Download the NLTK datasets available on their website, since our dataset for training and testing is a part of that.

The program processes a data set,inputs a query,and calculates the tf-idf index of words relative to the query, returning the 10 most relevant documents of the results along with the scores they secured. 
The dataset is first imported, followed by the definition of functions, followed by their use according to requirement. 
The last important step is the calculation of the tf-idf index followed by their ranking based on scores.

Since a timer is also implemented, the average time from our tests to create an inverted index is 4 seconds while searching through the final dictionary to output results is about 0.003 seconds.

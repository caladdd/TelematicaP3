# Special Topics in Telematics - Project 3

# TF-IDF (Term Frequency-Inverse Document Frequency)

 A central question in text mining and natural language processing is how to quantify what a document is about. There are dif
 
  One measure of how important a word may be is its term frequency (TF), how frequently a word occurs in a document [1]. This is a statitical measure used to weight how important a word is to a document in a collection or corpus (a large and structured set of texts) [2]. Though, there may be some words that appear a lot but are not important. This is the case for words like "the", "is", "of", in English. These words are usually added to a list of stopwords, which are words that should be removed before analysis. The list of stopwords may change depending of the topic to analyze, some words are more important than others in some topics [1].


 


 Variations of the TF-IDF weighting scheme are often used by search engines as a central tool in scoring and ranking a document's relevance given a user query.

One of the simplest ranking functions is computed by summing the TF-IDF for each query term; many more sophisticated ranking functions are variants of this simple model.

TF-IDF can be successfully used for stop-words filtering in various subject fields including text summarization and classification.

# References

[1] https://cran.r-project.org/web/packages/tidytext/vignettes/tf_idf.html
[2] https://en.wikipedia.org/wiki/Tf%E2%80%93idf
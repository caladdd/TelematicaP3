# Special Topics in Telematics - Project 3

# TF-IDF (Term Frequency-Inverse Document Frequency)

A central question in text mining and natural language processing is how to quantify what a document is about. There are different ways to achieve this, for example TF or IDF [1].

One measure of how important a word may be is its term frequency (tf), how frequently a word occurs in a document [1]. This is a statistical measure used to weight how important a word is to a document in a collection or corpus (a large and structured set of texts) [2]. Though, there may be some words that appear a lot but are not important. This is the case for words like "the", "is", "of", in English. These words are usually added to a list of stopwords, which are words that should be removed before analysis. The list of stopwords may change depending of the topic to analyze, some words are more important than others in some topics [1].

In the other hand, we have the inverse document frequency (idf) which decreases the weight for commonly used words and increases the weight for words that are not used very much in a collection of documents [1].

When we combine both measures we can calculate a term’s tf-idf, which represent how important a word is to a collection of documents[1].

# LDA (Latent Dirichlet allocation)

Latent Dirichlet allocation (LDA) is a topic model that generates topics based on word frequency from a set of documents [3]. A topic model is a type of statistical model for discovering the abstract "topics" that occur in a collection of documents [4].

A topic is the probability distribution over words. We could characterize a document with the list of topics based on the vocabularies it used and the probability distribution of individual topics. This method converts the text information into word frequency vector, building the numeric foundation for data modeling. However, it oversimplifies the complexity of text mining because it does not take the word sequence into consideration, causing confusing to determine the major topic while there are multiple topics in the same document [5]. 

Latent Dirichlet Allocation (LDA) is the text mining method developed by David Blei (Computer Science Professor at Columbia University), Andrew Ng (co-founder of Coursera), and Michael Jordan (advisor of David Blei and Andrew Ng). As an unsupervised learning (no prior label for data structure) method [5].
The generative process of LDA:
Take a topic from a document
Take a word from the chosen topic from 1
Repeat 1 and 2 until every single word was matched with a topic in the document.

# References

[1] https://cran.r-project.org/web/packages/tidytext/vignettes/tf_idf.html 
[2] https://en.wikipedia.org/wiki/Tf%E2%80%93idf
[3] https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html 
[4] https://en.wikipedia.org/wiki/Topic_model 
[5] https://edlab.tc.columbia.edu/blog/13139-Topic-Modeling-with-LDA-in-NLP-data-mining-in-Pressible 



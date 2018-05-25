# Special Topics in Telematics - Project 3

# TF-IDF (Term Frequency-Inverse Document Frequency)

A central question in text mining and natural language processing is how to quantify what a document is about. There are different ways to achieve this, for example TF or IDF [1].

One measure of how important a word may be is its term frequency (TF), how frequently a word occurs in a document [1]. This is a statistical measure used to weight how important a word is to a document in a collection or corpus (a large and structured set of texts) [2]. Though, there may be some words that appear a lot but are not important. This is the case for words like "the", "is", "of", in English. These words are usually added to a list of stop words, which are words that should be removed before analysis. The list of stop words may change depending of the topic to analyse, some words are more important than others in some topics [1].

In the other hand, we have the inverse document frequency (IDF) which decreases the weight for commonly used words and increases the weight for words that are not used very much in a collection of documents [1].

When we combine both measures we can calculate a term’s TF-IDF that represents how important a word is to a collection of documents [1].

# LDA (Latent Dirichlet Allocation)

Latent Dirichlet allocation (LDA) is a topic model that generates topics based on word frequency from a set of documents [3]. A topic model is a type of statistical model for discovering the abstract "topics" that occur in a collection of documents [4].

A topic is the probability distribution over words. We could characterize a document with the list of topics based on the vocabularies it used and the probability distribution of individual topics. This method converts the text information into word frequency vector, building the numeric foundation for data modeling. However, it oversimplifies the complexity of text mining because it does not take the word sequence into consideration, making it confusing to determine the major topic when there are multiple topics in the same document [5]. 

Latent Dirichlet Allocation (LDA) is the text mining method developed by David Blei (Computer Science Professor at Columbia University), Andrew Ng (co-founder of Coursera), and Michael Jordan (advisor of David Blei and Andrew Ng) as an unsupervised learning (no prior label for data structure) method [5]. The generative process of LDA is:
- Take a topic from a document
- Take a word from the chosen topic from 1
- Repeat 1 and 2 until every single word was matched with a topic in the document

Spark's implementation [13, 14] offers quite a few options to create the LDA model, but is still an experimental feature:
- **k**: the number of topics.
- **docConcentration**: Dirichlet parameter for prior over documents’ distributions over topics. If your documents are made up of a few dominant topics, choose a low value. Commonly know as *alpha*.
- **topicConcentration**: Dirichlet parameter for prior over topics’ distributions over words. If your topics are made up of a few dominant words, choose a low *beta*.
- **maxIter**: limit on the number of iterations.
- **optimizer**: the optimizer used to perform the calculation. The options are `'em'` for *EM optimizer* and `'online'` for Online Variational Bayes LDA Algorithm.

# Stemming and Lemmatization

For grammatical reasons, documents use different forms of the same word, such as *organize*, *organizes*, and *organizing*. Additionally, there are families of derivationally related words with similar meanings, such as *democracy*, *democratic*, and *democratization*. In many situations, it seems as if it would be useful for a search for one of these words to return documents that contain another word in the set. The goal of both stemming and lemmatization is to reduce inflectional forms and sometimes derivationally related forms of a word to a common base form [6]. 

Stemming refers to a heuristic process that chops off the ends of words in the hope of achieving this goal correctly most of the time, and often includes the removal of derivational affixes [6]. 

Lemmatization refers to a similar process, but doing things properly with the use of a vocabulary and morphological analysis of words, normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the lemma [6].

If confronted with the token *saw*, stemming might return just *s*, whereas lemmatization would attempt to return either *see* or *saw* depending on whether the use of the token was as a verb or a noun [6].

Modern lemmatization algorithms are used through external libraries, the most common ones being NLTK's [7] and Stanford's CoreNLP [8]. NLTK's is implemented based on Princeton University's WordNet [9, 10], a lexical database for English. Since this project is implemented using a third party cluster, we are unable to install any such libraries. We had to write our own algorithm, so we went for stemming algorithms. In our case we chose to implement the original Porter's Algorithm, which can be found in the author's webpage [11] and is also available in NLTK [12].

# References

[1] https://cran.r-project.org/web/packages/tidytext/vignettes/tf_idf.html 

[2] https://en.wikipedia.org/wiki/Tf%E2%80%93idf

[3] https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html 

[4] https://en.wikipedia.org/wiki/Topic_model 

[5] https://edlab.tc.columbia.edu/blog/13139-Topic-Modeling-with-LDA-in-NLP-data-mining-in-Pressible 

[6] https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html 

[7] http://www.nltk.org/ 

[8] https://stanfordnlp.github.io/CoreNLP/ 

[9] https://wordnet.princeton.edu/ 

[10] https://github.com/nltk/nltk/blob/develop/nltk/stem/wordnet.py 

[11] https://tartarus.org/martin/PorterStemmer/ 

[12] https://github.com/nltk/nltk/blob/develop/nltk/stem/porter.py 

[13] https://zerogravitylabs.ca/lda-topic-modeling-spark-mllib/

[14] https://spark.apache.org/docs/2.3.0/api/python/pyspark.ml.html#pyspark.ml.clustering.LDA


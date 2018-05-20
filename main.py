from pyspark.sql.functions import col, udf, struct
from pyspark.sql.types import *
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.ml.clustering import LDA
from pyspark.ml.linalg import Vectors, SparseVector

from preprocessing import cleanup_text

user = "magude29"

# load data
rawdata = spark.read.load(
    "hdfs:///user/" + user + "/datasets/airlines.csv", format="csv", header=True)

# preprocessing: normalize to lowercase only, remove stop words and perform stemming
# using the original Porter's Stemming Algorithm
udf_cleantext = udf(cleanup_text, ArrayType(StringType()))
clean_text = rawdata.withColumn("words", udf_cleantext(
    struct([rawdata[x] for x in rawdata.columns])))

# generate TF-IDF matrix
cv = CountVectorizer(inputCol="words", outputCol="rawFeatures", vocabSize=1000)
cvmodel = cv.fit(clean_text)
featurizedData = cvmodel.transform(clean_text)
vocab = cvmodel.vocabulary
vocab_broadcast = sc.broadcast(vocab)
idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)

# generate 25 data-driven topics using LDA (Latent Dirichlet Allocation) to cluster the
# TF-IDF matrix. "em" = expectation-maximization
lda = LDA(k=25, seed=123, optimizer="em", featuresCol="features")
ldamodel = lda.fit(rescaledData)
ldamodel.isDistributed()
ldamodel.vocabSize()
ldatopics = ldamodel.describeTopics()
udf_map_termID_to_Word = udf(lambda termIndices: [
                             vocab_broadcast.value[termID] for termID in termIndices], ArrayType(StringType()))
ldatopics_mapped = ldatopics.withColumn(
    "topic_desc", udf_map_termID_to_Word(ldatopics.termIndices))
ldatopics_mapped.select(ldatopics_mapped.topic,
                        ldatopics_mapped.topic_desc).show(25, False)
ldaResults = ldamodel.transform(rescaledData)

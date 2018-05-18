# Generate 25 Data-Driven Topics:
# "em" = expectation-maximization 
lda = LDA(k=25, seed=123, optimizer="em", featuresCol="features")
ldamodel = lda.fit(rescaledData)
 
ldamodel.isDistributed()
ldamodel.vocabSize()
 
ldatopics = ldamodel.describeTopics()
# Show the top 25 Topics
#ldatopics.show(25)

def map_termID_to_Word(termIndices):
    words = []
    for termID in termIndices:
        words.append(vocab_broadcast.value[termID])
    
    return words

udf_map_termID_to_Word = udf(map_termID_to_Word , ArrayType(StringType()))
ldatopics_mapped = ldatopics.withColumn("topic_desc", udf_map_termID_to_Word(ldatopics.termIndices))
ldatopics_mapped.select(ldatopics_mapped.topic, ldatopics_mapped.topic_desc).show(25,False)

ldaResults = ldamodel.transform(rescaledData)

#ldaResults.show()

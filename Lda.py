# Generate 25 Data-Driven Topics:
# "em" = expectation-maximization 
lda = LDA(k=25, seed=123, optimizer="em", featuresCol="features")
ldamodel = lda.fit(rescaledData)
 
ldamodel.isDistributed()
ldamodel.vocabSize()
 
ldatopics = ldamodel.describeTopics()
# Show the top 25 Topics
ldatopics.show(25)

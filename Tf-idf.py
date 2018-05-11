#hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
#featurizedData = hashingTF.transform(clean_text)
 
# Term Frequency Vectorization  - Option 2 (CountVectorizer)    : 
cv = CountVectorizer(inputCol="words", outputCol="rawFeatures", vocabSize = 1000)
cvmodel = cv.fit(clean_text)
featurizedData = cvmodel.transform(clean_text)
 
vocab = cvmodel.vocabulary
vocab_broadcast = sc.broadcast(vocab)
 
idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData) # TFIDF

from pyspark.sql.functions import col, udf, struct
from pyspark.sql.types import *
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.ml.clustering import LDA
from pyspark.ml.linalg import Vectors, SparseVector
import re

rawdata = spark.read.load("hdfs:///user/jcaladh/datasets/airlines.csv",format="csv", header=True)
exec(open("/home/jcaladh/top-telematica/TelematicaP3/Pre-processing.py").read())
exec(open("/home/jcaladh/top-telematica/TelematicaP3/Tf-idf.py").read())
exec(open("/home/jcaladh/top-telematica/TelematicaP3/Lda.py").read())
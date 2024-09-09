from pyspark import SparkConf, SparkContext
import time

conf = SparkConf().setAppName("WordCount")
sc = SparkContext(conf=conf)

t = time.time()
text_file = sc.textFile('hdfs:///HW1/medium.txt')

# Perform the word count
counts = (text_file
            .flatMap(lambda line: line.split())
            .map(lambda word: (word, 1))
            .reduceByKey(lambda a, b: a + b))


counts.saveAsTextFile('hdfs:///HW1/out/word_count_output')
print(f'Time taken: {time.time() - t}')
sc.stop()
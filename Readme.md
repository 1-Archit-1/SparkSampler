# Word Count and K-means using Spark and Hadoop

This repository contains code for performing Word Count and K-means clustering using Hadoop Map Reduce and Spark. Multiple configurations and datasets were used to identify performance metrics and compare results across different runs. 
Analysis results have been posted as a pdf. 

## Word Count

The Word Count example shows how to count occurrences of each word in a given text document using Hadoop and Spark. It utilizes MapReduce to process large datasets.

To run the Word Count example, follow these steps:

1. Install Spark and Hadoop on your system.
2. Configure Spark and Hadoop settings and environment variables.
3. Navigate to the `Word Count` directory.
4. You can use prexisting datasets, or you can create your own dataset using the dataset_generator.py
5. For Hadoop Map Reduce, you can use jar files to run your code. Here are the steps to follow:
    1. Build the WordCount.java file into a new jar file after altering configs. Or use the prexisting jar files. 
    2. Once you have the jar file, you can submit it to Hadoop.
    3. Hadoop will distribute the processing across the cluster and generate the output in the specified output path.
6. For Spark, submit the word_count_spark.py file to Yarn for execution

## K-means Clustering

The K-means Clustering example shows how to perform clustering analysis on a dataset using Spark Map Reduce. It partitions data into K clusters based on similarity.

To run the K-means Clustering example, follow these steps:

1. Install Spark and Hadoop on your system.
2. Configure Spark and Hadoop settings and environment variables.
3. Navigate to the `K-Means` directory.
4. The dataset used is the UCI wines dataset. 
5. The PCA_output.csv file is the dataset generated after reducing the dimensions to 2 using PCA.py
6. Modify the `k_means_mr.py` script to specify the desired number of clusters (K) and input data.
7. Execute the `k_means_mr.py` script on PCA_output.csv using the Spark and Hadoop cluster 
8. Execute the `k_means_broadcast.py` script with the required dataset for an optimized solution using centroid broadcasting
8. You can extend the dataset using the dataset_extender.py script. 


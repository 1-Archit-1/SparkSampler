from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler, PCA
from pyspark.ml.clustering import KMeans
from pyspark.ml import Pipeline
from ucimlrepo import fetch_ucirepo 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

spark = SparkSession.builder.appName("KMeansClustering").getOrCreate()
wine = fetch_ucirepo(id=109) 
x = wine.data.features 
y = wine.data.targets 

df_pandas = pd.concat([x, y], axis=1)
df_spark = spark.createDataFrame(df_pandas)

feature_columns = x.columns.tolist() 

 # List of feature column names
assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
assembled_data = assembler.transform(df_spark)

scaler = StandardScaler(inputCol='features', outputCol="scaled_features")
pca_model = PCA(k=2, inputCol="scaled_features", outputCol="pca_features")
kmeans = KMeans(k=4, seed=1, featuresCol="pca_features", predictionCol="prediction")
pipeline = Pipeline(stages=[assembler, scaler,pca_model])
model = pipeline.fit(df_spark)
predictions = model.transform(df_spark)

pandas_df = predictions.select("pca_features").toPandas()
values_df = pd.DataFrame(pandas_df['pca_features'].tolist())
print(values_df)
values_df.to_csv('output.csv' ,index=False)
from pyspark import SparkConf, SparkContext
import numpy as np
import time
from matplotlib import pyplot as plt
t1 = time.time()
conf = SparkConf().setAppName("KMeans")
sc = SparkContext(conf=conf)

data = sc.textFile("hdfs:///HW1/smallest.csv")
data = data.map(lambda line: np.array([float(x) for x in line.split(',')]))

k = 3 #Number of clusters

centroids = data.takeSample(False, k)

def euclidean_distance(p1, p2):
    return sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))])

# assign each point to nearest centroid
def assign_to_nearest_centroid(point, centroids):
    distances = [euclidean_distance(point, centroid) for centroid in centroids]
    return [distances.index(min(distances)), ([point], 1)]

def update_centroid(cluster):
    points, count = cluster
    new_centroid = tuple([sum([point[i] for point in points]) / count for i in range(len(points[0]))])
    return new_centroid

converged = False
limit = 5
n=0

while not converged and n <limit:
    n+=1
    clusters = data.map(lambda point: assign_to_nearest_centroid(point, centroids))
    new_centroids = (clusters
        .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]), numPartitions=3) #Set number of reducers here
        .mapValues(update_centroid)
        .collect()
    )
    # Check for convergence
    converged = all([euclidean_distance(new_centroids[i][1], centroids[i]) < 1e-8 for i in range(k)])
    centroids = [new_centroid for (_, new_centroid) in new_centroids]

print("Final centroids:\n", centroids)
final_clusters = data.map(lambda point: assign_to_nearest_centroid(point, centroids)).collect()
print("Clusters:\n", final_clusters)

print(f'time taken {time.time()-t1}')

colors = ['r', 'g', 'b']  # Color for each cluster
for cluster_idx, color in enumerate(colors):
    cluster_points = np.array([point[1][0][0] for point in final_clusters if point[0] == cluster_idx])
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=color, label=f'Cluster {cluster_idx}')


# Labels and title
plt.title("K-Means Clustering")
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
plt.legend()
plt.show()
sc.stop()
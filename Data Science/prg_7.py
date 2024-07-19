# Consider the dataset spiral.txt (https://bit.ly/2Lm75Ly). 
# The first two columns in the dataset corresponds to the co-ordinates of each data point.
# The third column corresponds to the actual cluster label.
# Compute the rand index for the following methods:
# K – means Clustering
# Single – link Hierarchical Clustering 
# Complete link hierarchical clustering. 
# Also visualize the dataset and which algorithm will be able to recover the true clusters.

import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt

data = np.loadtxt("spiral.txt", delimiter="\t", skiprows=1)
X = data[:, :2]  # Features
y = data[:, 2]  # Actual cluster labels

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title('True Clusters')
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()

# K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_clusters = kmeans.fit_predict(X)

# Single-link Hierarchical Clustering
single_link = AgglomerativeClustering(n_clusters=3, linkage='single')
single_link_clusters = single_link.fit_predict(X)

# Complete-link Hierarchical Clustering
complete_link = AgglomerativeClustering(n_clusters=3, linkage='complete')
complete_link_clusters = complete_link.fit_predict(X)

rand_index_kmeans = adjusted_rand_score(y, kmeans_clusters)
rand_index_single_link = adjusted_rand_score(y, single_link_clusters)
rand_index_complete_link = adjusted_rand_score(y, complete_link_clusters)

print("Rand Index for K-means Clustering:", rand_index_kmeans)
print("Rand Index for Single-link Hierarchical Clustering:", rand_index_single_link)
print("Rand Index for Complete-link Hierarchical Clustering:", rand_index_complete_link)
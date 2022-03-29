#===================== Install required libraries ======================

# install required libraries
# pip install scikit-learn numpy

#===================== Import required libraries ======================

# importing required libraries
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_mutual_info_score
from sklearn.metrics.cluster import fowlkes_mallows_score

#========================== Hyperparameters ===========================

# Set Hyperparameters
eps = 0.5
min_samples = 5
dist = 'euclidean'
search_algo = 'auto'

#============================== Data set ===============================

# number of training points
n_samples = 1000
# number of features in data set
n_features = 2
# number of cluster centers
n_centers = 3
# cluster standard deviation
cluster_std = 1.0

# Generate Synthetic Data

X, y = make_blobs(n_samples=n_samples, 
            n_features=n_features, 
            centers=n_centers, 
            cluster_std=cluster_std)

#============================== Training ===============================

# Train DBSCAN Model
model = DBSCAN(eps=eps,
            min_samples=min_samples,
            metric=dist,
            algorithm=search_algo)
model.fit(X)

#============================== Testing ===============================

# get prediction labels for each data points
y_pred = model.labels_

# Adjusted Rand Score
print("\nAdjusted Rand Score : {}".format(
    np.round(adjusted_rand_score(y, y_pred), decimals=2)))

# Normalized Mutual Information Based Score
print("\nNormalized Mutual Information Based Score : {}".format(
    np.round(normalized_mutual_info_score(y, y_pred), decimals=2)))

# Adjusted Mutual Information (AMI) 
print("\nAdjusted Mutual Information (AMI) : {}".format(
    np.round(adjusted_mutual_info_score(y, y_pred), decimals=2)))

# Fowlkes-Mallows Score
print("\nFowlkes-Mallows Score : {}".format(
    np.round(fowlkes_mallows_score(y, y_pred), decimals=2)))

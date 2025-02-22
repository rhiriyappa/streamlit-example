#===================== Import required libraries ======================

# importing required libraries
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.metrics import plot_roc_curve
from sklearn.metrics import plot_precision_recall_curve

#========================== Hyperparameters ===========================

# Set Hyperparameters
penalty = 'l2'
max_iter = 100

#============================== Data set ===============================

# number of training points
n_samples = 1000
# number of features in data set
n_features = 10
# number of classes
n_classes = 2

# Generate Synthetic Data
X, y = make_classification(n_samples=n_samples,
                            n_features=n_features,
                            n_classes=n_classes,
                            random_state=42)

# Splitting the data into training and testing data 
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                    test_size = 0.2, 
                                    stratify=y, 
                                    random_state=42)

#============================== Training ===============================

# Train Logistic Regression Model
model = LogisticRegression(penalty=penalty, max_iter=max_iter)
model.fit(X_train, y_train)

#============================== Testing ===============================

# Testing model on train data

# get the prediction labels of the training data
cross_validation = cross_val_score(model, X_train, y_train, cv=5)

# evaluate and print the results
print("\nModel Performance on Training Data: {}".format(
    np.mean(cross_validation).round(2)))

# Testing model on test data

# get the prediction labels of the test data
y_pred = model.predict(X_test)
accuracy = model.score(X_test, y_test)

print("\nModel Performance on Test Data: {}".format(
    accuracy.round(2)))

# Compute the Precision
precision = precision_score(y_test, y_pred).round(2)
print("\nPrecision: {}".format(precision))

# Compute the Recall
recall = recall_score(y_test, y_pred).round(2)
print("\nRecall: {}".format(recall))

# Generate text reprot showing the main classification metrics
report = classification_report(y_test, y_pred)
print(report)

#=========================== Visualization ============================

fig, axes = plt.subplots(figsize=(10,6), ncols=2, sharey=True)
ax1, ax2 = axes

plot_roc_curve(model, X_test, y_test, ax=ax1)
ax1.set_title("ROC Curve")
plot_precision_recall_curve(model, X_test, y_test, ax=ax2)
ax2.set_title("Precision Recall Curve")
plt.show()

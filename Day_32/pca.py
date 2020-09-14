/* Create a dataset which is nonlinear and then apply PCA on the dataset. */
import matplotlib.pyplot as plt 
from sklearn.datasets import make_moons 

X, y = make_moons(n_samples = 500, noise = 0.02, random_state = 417) 

plt.scatter(X[:, 0], X[:, 1], c = y) 
plt.show() 

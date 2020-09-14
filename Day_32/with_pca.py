/* apply PCA on this dataset */

from sklearn.decomposition import PCA 
pca = PCA(n_components = 2) 
X_pca = pca.fit_transform(X) 

plt.title("PCA") 
plt.scatter(X_pca[:, 0], X_pca[:, 1], c = y) 
plt.xlabel("Component 1") 
plt.ylabel("Component 2") 
plt.show() 

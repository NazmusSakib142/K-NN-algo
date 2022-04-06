from sklearn import datasets
iris=datasets.load_iris()
dir(iris)
print(iris.keys())
print(iris.DESCR)
print(iris.data)
print(iris.feature_names)
print(iris.target_names)
print(iris.target)
print(iris.data.shape)
x=iris.data
y=iris.target
display(x)
display(y)
import seaborn as sns 
iris=sns.load_dataset('iris')
relation=iris.corr()
#display(relation)
sns.heatmap(relation,cmap='coolwarm',annot=True)

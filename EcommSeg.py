import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#for preprocessing model... normalize the dataset
from sklearn.preprocessing import MinMaxScaler
#for equality of clustering
from sklearn.metrics import silhouette_score
#for unsupervised data
from sklearn.cluster import KMeans
#class from yellowbrick
from yellowbrick.cluster import KElbowVisualizer

data=pd.read_excel("/content/ecom customer_data.xlsx")
data.head()

df=data.copy()
df.info()

df.describe()

#Check the duplicates
df[df.duplicated()]

df.isna().sum()

df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])

df.isna().sum().sum()

df.Gender.value_counts()

sns.countplot(data=df,x='Gender')
plt.show()

plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.countplot(data=df,x='Orders')

#Order count by each number
plt.subplot(1,2,2)
sns.countplot(data=df,x='Orders',hue='Gender')
plt.suptitle("Overall Orders VS Gender wise Orders")
plt.show()

col=list(df.columns[2:])
def dist_list(lst):
  plt.figure(figsize=(30,30))
  for i, col in enumerate(lst,1):
    plt.subplot(6,6,i)
    sns.boxplot(data=df,x=df[col])
dist_list(col)

#heatmap
plt.figure(figsize=(20,15))
sns.heatmap(df.iloc[:,3:].corr())
plt.show()

df.iloc[:2,:].hist(figsize=(40,30))
plt.show()

new_df=df.copy()
new_df['Total Dearch']=new_df.iloc[:,3:].sum(axis=1)

new_df.sort_values('Total Dearch', ascending=False)

plt.figure(figsize=(13,8))
plt_data=new_df.sort_values('Total Dearch', ascending=False)[['Cust_ID','Gender','Total Dearch']].head(10)
sns.barplot(data=plt_data,x='Cust_ID',y='Total Dearch',hue='Gender')
plt.title("Top 10 Cust_ID based on Total Searches")
plt.show()

x=df.iloc[:,2:].values
x

scale=MinMaxScaler()
features=scale.fit_transform(x)
features

inertia=[]
for i in range(1,16):
  k_means=KMeans(n_clusters=i)
  k_means.fit(features)
  inertia.append(k_means.inertia_)

#elbow graph
plt.figure(figsize=(20,7))
plt.subplot(1,2,1)
plt.plot(range(1,16),inertia, 'bo-')
plt.xlabel('No of clusters'),plt.ylabel('Inertia')

plt.subplot(1,2,2)
kmeans=KMeans()
visualize=KElbowVisualizer(kmeans,k=(1,16))
visualize.fit(features)
plt.title("Elbow Graph and Elbow Visualizer")
visualize.poof()
plt.show()

silhoutte_avg=[]
for i in range(2,16):
  kmeans=KMeans(n_clusters=i)
  cluster_labels=kmeans.fit_predict(features)
  #Silhouette score
  silhoutte_avg.append(silhouette_score(features,cluster_labels))

plt.figure(figsize=(10,7))
plt.plot(range(2,16),silhoutte_avg,'bX-')
plt.xlabel('Values of K'),plt.ylabel('Silhouette Score')
plt.title('Silhouette analysis for optional K')
plt.show()

model=KMeans(n_clusters=3)
model=model.fit(features)

y_km=model.predict(features)
centers=model.cluster_centers_

df['Cluster']=pd.DataFrame(y_km)
df.to_csv("Cluster_data", index=False)

df["Cluster"].value_counts()

sns.countplot(data=df,x='Cluster')
plt.show()

c_df=pd.read_csv('Cluster_data')
c_df.head()

c_df['Total Dearch']=c_df.iloc[:,3:38].sum(axis=1)

cl_0=c_df.groupby(['Cluster','Gender'], as_index=False).sum().query('Cluster==0')
cl_0

plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
sns.countplot(data=c_df.query('Cluster==0'),x='Gender')
plt.title('Customers count')

plt.subplot(1,2,2)
sns.barplot(data=cl_0,x='Gender',y='Total Dearch')
plt.title('Total Seach by gender')
plt.suptitle('No. of customers and their total seachers in "Cluster 0"')
plt.show()

cl_1=c_df.groupby(['Cluster','Gender'], as_index=False).sum().query('Cluster==1')
cl_1

plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
sns.countplot(data=c_df.query('Cluster==0'),x='Gender')
plt.title('Customers count')

plt.subplot(1,2,2)
sns.barplot(data=cl_1,x='Gender',y='Total Dearch')
plt.title('Total Seach by gender')
plt.suptitle('No. of customers and their total seachers in "Cluster 0"')
plt.show()

cl_2=c_df.groupby(['Cluster','Gender'], as_index=False).sum().query('Cluster==1')
cl_2

plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
sns.countplot(data=c_df.query('Cluster==0'),x='Gender')
plt.title('Customers count')

plt.subplot(1,2,2)
sns.barplot(data=cl_2,x='Gender',y='Total Dearch')
plt.title('Total Seach by gender')
plt.suptitle('No. of customers and their total seachers in "Cluster 0"')
plt.show()

final_df=c_df.groupby(by='Cluster',as_index=False).sum()
final_df

plt.figure(figsize=(15,6))
sns.countplot(data=c_df,x='Cluster',hue='Gender')
plt.title('Total Customer on each Cluster')
plt.show()

plt.figure(figsize=(15,6))
plt.subplot(1,2,1)
sns.barplot(data=final_df,x='Cluster',y='Total Dearch')
plt.title('Total Searches by each group')

plt.subplot(1,2,2)
sns.barplot(data=final_df,x='Cluster',y='Orders')
plt.title('Past Orders by each group')
plt.suptitle('Number of times customer searched the products and their past orders')
plt.show()

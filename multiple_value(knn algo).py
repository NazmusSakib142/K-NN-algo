import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = {     
    'k':[[50,110],[65,130],[70,140],[75,135],[80,140],[55,120]],
    'r':[[90,145],[100,150],[110,145],[95,151],[101,160],[104,154]],
    'g':[[55,120],[85,138],[88,142],[87,144],[89,141]],
    'y':[[105,155],[98,150],[91,150],[92,146],[93,149]]
    }

def scatter_plot(new_sample):
    for i in dataset:
        for j in dataset[i]:
            plt.scatter(j[0],j[1],s=50,color=i)
            
    plt.scatter(new_sample[0],new_sample[1],s=100,color='b')
    plt.show()
    

def knn(dataset,predict,k=5):
    distance=[]
    for group in dataset:
        for features in dataset[group]:
            euclidian=np.linalg.norm(np.array(features)-np.array(predict))
            distance.append([euclidian,group])
    votes=[i[1] for i in sorted(distance)[:k]]
    vote_result=Counter(votes).most_common(1)[0][0]
    print(vote_result)
    return vote_result 

while True:
    new_arr=input('Enter new sample :').split(',')
    new_sample=[]
    new_sample.append(int(new_arr[0]))
    new_sample.append(int(new_arr[1]))
    if new_sample==[0,0]:
        break
    else:
        print(new_sample)
        scatter_plot(new_sample)
        result=knn(dataset,new_sample,k=5)
        
        if result=='k':
            print('corona')
        elif result=='r':
            print('Diabetes')
        elif result=='g':
            print('cancer')
        elif result=='r':
            print('Asthma')

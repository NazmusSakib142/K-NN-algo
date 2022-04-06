import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = {     
    'k':[[50,110],[65,130],[70,140],[55,120],[85,138],[88,142],[87,144],[89,141],[75,135],[80,140],[55,120]],
    'r':[[90,145],[100,150],[110,145],[105,155],[98,150],[91,150],[92,146],[93,149],[95,151],[101,160],[104,154]]            
    }

def scatter_plot(new_feat):
        
    for i in dataset:
        for ii in dataset[i]:
            plt.scatter(ii[0], ii[1], s=100, color=i)
        
    plt.scatter(new_feat[0],new_feat[1],color='b')    
    plt.show()   
        

def K_NN(data,predict,k=7):
    
    distances = []
    
    for group in data:
        for features in data[group]:
            
            euclidian_distance=np.linalg.norm(np.array(features)-np.array(predict))
            
            distances.append([euclidian_distance,group])
            
    print(distances)        
    votes = [i[1] for i in sorted(distances)[:k]]
    print(votes)
    vote_result=Counter(votes).most_common(1)[0][0]
    return vote_result
    
while True:
    
    new_arr = input('Add new sample [weight,height]= ').split(',')    

    new_feat = []
    new_feat.append(int(new_arr[0]))
    new_feat.append(int(new_arr[1]))
    
    if new_feat==[0,0]:
        break        
    else:
        #print(new_feat)
        scatter_plot(new_feat)
        result = K_NN(dataset,new_feat,k=7)
        print('Result',result)
        if result=='k':
            print('Footballer')
        else:
            print('Wrestler')

import numpy as np

def Trimmed_Mean(List, percentage ):
    # The size of the list in question 
    size = len(List);
    k = int( round(size*(float (percentage)/100)/2))

    print(np.mean(List[k+1:size-k]))

Data = [1,4,2,5,6,8,9,10]

Trimmed_Mean(Data, 10)
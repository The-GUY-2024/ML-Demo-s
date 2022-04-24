num_list = [5,5,5,5]

# This a basic arithmetic mean function 
def mean(list):
    N = len(num_list)
    adding = 0
    for t in range(len(num_list)):

        #add all the values in the list 
        adding =  adding + int(num_list[t]) 
#Get the arithmetic mean  
    mean = adding / len(num_list);

#Display the result
    print("The arithmetic Mean: " + str(mean))
    print("The sum of numbers: " + str(adding))
    print("The total numbers: " + str(len(num_list)))

mean(num_list)
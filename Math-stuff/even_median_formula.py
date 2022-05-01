odd = [20,100,45, 55,800,7800]

#Set the list to be in ascending Order
odd.sort()
print("Ascending Order " + str(odd))

#get the size of the list 
list_size = len(odd)


#since list start at 0 insted of 1 the formula need to be change a little

f_v = int(list_size/2 - 1)

s_v = int(list_size/2) 



# add the values  & divide by 2

add = int(odd[f_v] + odd[s_v])

median = add/2
print("The median is: " + str(median))

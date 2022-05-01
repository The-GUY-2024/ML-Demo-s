odd = [11, 15 ,20 ,18 ,46,25,24,40,1]

#Set the list to be in ascending Order 
odd.sort()
print("Order " + str(odd))


#Get the size of the list 
size_odd = len(odd)

#this is the formula in use (Very simple)
term = int((size_odd + 1)/2 )



#You need to substract 1 since list start at 0 insted of 1 
term = term - 1 


median= odd[term]

print("The median is " + str(median))

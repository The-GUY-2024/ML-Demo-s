import csv



#Define the headers of the csv file 
header = ['Num-of-TV','Num-of-houses']

file_data= [
    {'Num-of-TV': 1, 'Num-of-houses': 30},
    {'Num-of-TV': 2, 'Num-of-houses': 200},
    {'Num-of-TV': 3, 'Num-of-houses': 100},
    {'Num-of-TV': 4, 'Num-of-houses': 25}
]

# open the file 
with open('weighted_mean.csv','w')as file:
#create a csv writer
    writer = csv.DictWriter(file,fieldnames=header)


    #Write the header file
    writer.writeheader()
    #write the rows to the file
    writer.writerows(file_data)

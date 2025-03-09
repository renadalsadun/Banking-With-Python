import csv 
	
# opening the CSV file 
with open('data.csv', mode ='r')as file: #The ‘with‘ keyword is used along with the open() method as it simplifies exception handling and automatically closes the CSV file.


	
# reading the CSV file 
    csvFile = csv.reader(file, delimiter=';') 
	
# displaying the contents of the CSV file 
    for lines in csvFile: 
		    print(lines) 

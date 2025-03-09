import csv 
	



def reading_from_file(file_name):
    # opening the CSV file 
    with open(f'{file_name}.csv', mode ='r')as file: #The ‘with‘ keyword is used along with the open() method as it simplifies exception handling and automatically closes the CSV file.
        return csv.reader(file, delimiter=';') 


#     for lines in csvFile: print(lines)
  

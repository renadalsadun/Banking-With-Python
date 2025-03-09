import csv 
	

header = [ 'account_id' , 'first_name' , 'last_name' , 'password' , 'balance_checking' , 'balance_savings' ] 


content = []
def reading_from_file(file_name):
    with open(f'{file_name}.csv', mode='r') as file_reader:
        content = csv.reader( file_reader , delimiter = ';' )
        data = [dict(zip(header, row)) for row in content]
        return data

customers = reading_from_file('data')



print(type(customers))
print(customers)

class Customer():
    def __init__(self):
        pass




# def reading_from_file(file_name):

#     '''
#     Create a new file, append header, the append the data readed from 'data.csv'
#     '''

#     open("bank_data.csv", "w")

#     with open(f'bank_data.csv', mode ='a')as file_write: #The ‘with‘ keyword is used along with the open() method as it simplifies exception handling and automatically closes the CSV file.
#         csvwriter = csv.writer(file_write, delimiter=';') 
#         csvwriter.writerow((header))
#         with open(f'{file_name}.csv', mode ='r')as file_read: #The ‘with‘ keyword is used along with the open() method as it simplifies exception handling and automatically closes the CSV file.
#             content = csv.reader(file_read, delimiter=';') 
#             for lines in content :
#                 csvwriter.writerow((lines))
         
# reading_from_file('data')

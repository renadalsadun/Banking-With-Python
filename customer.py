import csv 
	

header = [ 'account_id' , 'first_name' , 'last_name' , 'password' , 'balance_checking' , 'balance_savings' ] 


content = []

def reading_from_file(file_name):

    '''
    reads the data from file_name file, and compines it in a dictionary with the header
    '''


    with open(f'{file_name}.csv', mode='r') as file_reader:
        content = csv.reader( file_reader , delimiter = ';' )
        data = [dict(zip(header, row)) for row in content]
        return data



# # debugging
# print(type(customers))
# print(customers)
# #end of debugging 

class Customer():

    all_customers = []
    next_account_id = 10001

    def __init__(self, first_name, last_name, password , balance_checking = None , balance_savings = None, account_id = None ):
        
        #if condition becausee existing customers - i.e. data- have id's but future customers do not 
        if not account_id:
            self.account_id = Customer.next_account_id
        Customer.next_account_id += 1
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = balance_checking
        self.balance_savings = balance_savings



    def add_new_customer(self, first_name, last_name, password , balance_checking = None , balance_savings = None ):

        new_customer = Customer(first_name, last_name, password, balance_checking, balance_savings )

        # add to all customers list 
        Customer.all_customers.append(new_customer) 


    def __str__ (self):
        return f'Account ID: {self.account_id}, Name {self.first_name} {self.last_name}'
        

# adding the customers in data.csv file to the Customer class!!    
existing_customers = reading_from_file('data')
for existing_customer in existing_customers:
    Customer.add_new_customer(
        existing_customer['account_id'],
        existing_customer['first_name'],
        existing_customer['last_name'],
        existing_customer['password'],
        existing_customer['balance_checking'],
        existing_customer['balance_savings']
    )

for customer in Customer.all_customers:

    print(customer)




    
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

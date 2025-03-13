
import csv
from datetime import datetime
import os

header = [ 'account_id' , 'first_name' , 'last_name' , 'password' , 'balance_checking' , 'balance_savings' ] 

transaction_header = ['timestamp', 'account_id', 'transaction_type', 'amount', 'balance']

content = []

def reading_from_file(file_name):

    '''
    reads the data from file_name file, and compines it in a dictionary with the header
    '''

    try:
        with open(f'{file_name}.csv', mode='r') as file_reader:
            content = csv.reader( file_reader , delimiter = ';' )
            data = [dict(zip(header, line)) for line in content]
            return data

    
    except FileNotFoundError:
        print(f"Error: File '{file_name}.csv' was not found")
        return [dict.fromkeys(header, '')]

    except csv.Error:
        print(f"Error: Could not read the CSV file '{file_name}.csv")
        return [dict.fromkeys(header, '')]


    
def write_to_file(file_name, customer):

    '''
    Appends a new customer's data to the CSV file without removing previous data
    '''

    try:
        # to check if file exsits or not
        file = os.path.isfile(f"{file_name}.csv") #returns true if file exists, false if it doesnt
        
        if file and os.stat(f"{file_name}.csv").st_size == 0:  # file exists BUT is empty
            write_header = True
        else:
            write_header = False

        with open(f"{file_name}.csv", mode="a", newline="") as file_writer:
            writer = csv.writer(file_writer, delimiter=";")

            
            if not file or write_header:  #if it doesnt exists , or it exists but empty
                writer.writerow(header)



            writer.writerow([
                customer.account_id,
                customer.first_name,
                customer.last_name,
                customer.password,
                customer.balance_checking,
                customer.balance_savings
            ])
    except Exception as e:
        print(f"Error writing to file: {e}")



def find_customer_index(file_name, account_id):

    '''
    reads the data from the file and returns the row index of the customer with the account_id  
    '''

    try:
        with open(f'{file_name}.csv', mode='r', newline='') as infile:
            reader = csv.reader( infile , delimiter = ';' )
            rows = list(reader)
        
# header = [ 0: 'account_id' , 1: 'first_name' , 2: 'last_name' , 3: 'password' , 4: 'balance_checking' , 5: 'balance_savings' ] 

        for index, row in enumerate(rows[1:]): # to skip header!
            if row[0] == account_id: # row[0] is the account id!!! 
                return index + 1 #1 is the header we skipped :)
            
        return -1  # if not found :(
    

    except FileNotFoundError:
        print(f"Error: File '{file_name}.csv' was not found")
        return -1

    except csv.Error:
        print(f"Error: Could not read the CSV file '{file_name}.csv")
        return -1



def log_transaction(account_id, transaction_type, amount, balance):
    
    '''
    logs a transaction in the transactions.csv file '
    '''

    try:
        # to check if file exsits or not
        file = os.path.isfile("transactions.csv") #returns true if file exists, false if it doesnt
        if file and os.stat("transactions.csv").st_size == 0:  # file exists BUT is empty
            write_header = True
        else:
            write_header = False

        with open("transactions.csv", mode="a", newline="") as file_writer:
            writer = csv.writer(file_writer, delimiter=";")

            if not file or write_header: #if it doesnt exists , or it exists but empty
                writer.writerow(transaction_header)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([timestamp, account_id, transaction_type, amount, balance])
    except Exception as e:
        print(f"Error logging transaction: {e}")



def update_file(file_name, row_index, col_index, new_value):

    '''
    updates the value at a specific row and column in the passed file
    reads the data from the file, modifies the value at the specified row and column, 
    and then writes the updated data back to the file (re-write the whole file :( )
    '''

    with open(file_name, mode='r', newline='') as infile:
        reader = csv.reader(infile, delimiter=';')
        rows = list(reader) #list of lists(rows)

    if row_index < len(rows) and col_index < len(rows[row_index]):
        rows[row_index][col_index] = new_value
    else:
        print("Error: Index out of range")
        return

    with open(file_name, mode='w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter=';')
        writer.writerows(rows)



def get_password(file_name, account_id):

    '''
    gets the password for a specific customer using their account_id
    reads the data from the file and checks the account_id to return the corresponding password
    '''

    try:
        with open(f'{file_name}.csv', mode='r', newline='') as infile:
            reader = csv.reader( infile , delimiter = ';' )
            rows = list(reader)
        
# header = [ 0: 'account_id' , 1: 'first_name' , 2: 'last_name' , 3: 'password' , 4: 'balance_checking' , 5: 'balance_savings' ] 

        for index, row in enumerate(rows[1:]): # to skip header!
            if row[0] == account_id: # row[0] is the account id!!! 
                return row[3] # row 3 is the password
            
    
        return None  # if not found :(
    
    except FileNotFoundError:
        print(f"Error: File '{file_name}.csv' not found")
        return None
    
    except csv.Error:
        print(f"Error: Could not read the CSV file '{file_name}.csv")
        return None



def get_transactions_by_account_id(file_name, account_id):

    '''
    reads transactions from a CSV file and filters by account_id, returns the list, or none
    '''


    transactions = []
    
    with open(f'{file_name}.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        
        next(reader, None)#skip header 
        
        for row in reader:
            if row[1] == str(account_id):  # row [1] is the account_id in the transactions.csv!
                transactions.append(row)
    
    return transactions



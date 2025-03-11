
import csv
from datetime import datetime


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
    """Appends a new customer's data to the CSV file without removing previous data"""
    try:
        with open(f"{file_name}.csv", mode="a", newline="") as file_writer:
            writer = csv.writer(file_writer, delimiter=";")
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

def log_transaction(account_id, transaction_type, amount, balance):
    """ Logs a transaction in the transactions.csv file """
    try:
        with open("transactions.csv", mode="a", newline="") as file_writer:
            writer = csv.writer(file_writer, delimiter=";")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([timestamp, account_id, transaction_type, amount, balance])
    except Exception as e:
        print(f"Error logging transaction: {e}")

def update_file(file_name, customer):
    pass

import csv 
	
############################################### READING FILE

header = [ 'account_id' , 'first_name' , 'last_name' , 'password' , 'balance_checking' , 'balance_savings' ] 


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

    


############################################### END OF READING FILE



###############################################  CUSTOMER CLASS

class Customer():

    all_customers = []
    next_account_id = 10001

    def __init__(self, first_name, last_name, password , balance_checking = None , balance_savings = None, account_id = None ):
        
        #if condition becausee existing customers - i.e. data- have id's but future customers do not 
        if account_id:
            self.account_id = int(account_id)
            
        else:
            self.account_id = Customer.next_account_id
            
        Customer.next_account_id += 1
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = float(balance_checking)
        self.balance_savings = float(balance_savings)

    @classmethod
    def find_costumer( cls , account_id ):
        for customer in Customer.all_customers:
            if customer.account_id == account_id:
                return customer
            
        return None # if the customer id is not valid, return none ;;


    @classmethod
    def get_number_of_customers(cls):
        return len(cls.all_customers)

    @classmethod
    def add_new_customer(cls, first_name, last_name, password , balance_checking = None , balance_savings = None , account_id = None  ):

        new_customer = Customer(first_name, last_name, password, balance_checking, balance_savings , account_id )

        # add to all customers list 
        cls.all_customers.append(new_customer)
        return new_customer




    def __str__ (self):
        return f'Account ID: {self.account_id}, Name: {self.first_name} {self.last_name}'



############################################### END OF CUSTOMER CLASS

if __name__ == "__main__":
    existing_customers = reading_from_file("data")

# adding the customers in data.csv file to the Customer class!!    
    if existing_customers[0]['account_id'] != '':
        for existing_customer in existing_customers:
            Customer.add_new_customer(
                existing_customer["first_name"],
                existing_customer["last_name"],
                existing_customer["password"],
                existing_customer["balance_checking"],
                existing_customer["balance_savings"],
                existing_customer["account_id"],
            )


    # debugging
    Customer.add_new_customer('renad', 'alsadun', 'password', '0292.2', '0.0' )

    for customer in Customer.all_customers:
        print(customer)

    print(Customer.next_account_id)
    #end of debugging



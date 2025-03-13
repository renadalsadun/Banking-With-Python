

import csv
from access_file import reading_from_file, write_to_file
from termcolor import colored
############################################### CUSTOMER CLASS

class Customer():

    all_customers = []
    next_account_id = 10001

    def __init__(self, first_name, last_name, password , balance_checking = None , balance_savings = None, account_id = None ):
        
        #if condition becausee existing customers - i.e. data- have id's but future 
        #customers -i.e. cashier made customers- do not have id's and will have the generated id instead
        
        if account_id:
            self.account_id = int(account_id)
            
        else:
            self.account_id = Customer.next_account_id
            
        Customer.next_account_id += 1
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = float(balance_checking) if balance_checking is not None else 0.0
        self.balance_savings = float(balance_savings) if balance_savings is not None else 0.0



    @classmethod
    def find_customer( cls , account_id ): 
        '''
        retuns customer object is customer exists, otherwise returns none
        '''
        for customer in Customer.all_customers:
            if customer.account_id == account_id:
                return customer
            
        return None # if the customer id is not valid, return none ;;



    @classmethod
    def get_number_of_customers(cls):
        '''
        returns the total number of customers
        '''
        return len(cls.all_customers)



    @classmethod
    def add_new_customer(cls, first_name, last_name, password , balance_checking = None , balance_savings = None , account_id = None  ):
        '''
        creates a new customer, if first/last name or password were not provided returns none
        if the customer is created, appends it to customer list, and the database -bank.csv file-
        '''

        if not first_name or not last_name or not password:
            print("Error: First Name, Last Name, and Password cannot be empty")
            return None

        try:
            new_customer = Customer(first_name, last_name, password, balance_checking, balance_savings , account_id )
        except Exception as e:
            print(f"Error creating customer: {e}")
            return None

        # add to all customers list 
        cls.all_customers.append(new_customer) 
        write_to_file("bank", new_customer)
        # print("Customer added successfully!\nCustomer details: ", new_customer)
        return new_customer



    @classmethod
    def login(cls, account_id, password):

                customer = cls.find_customer(account_id)  
                if customer and customer.password == password: #if the customer found and the pass is correct
                    return customer  # return the logged in customer
                else:
                    return None



    def set_checking_balance( self , new_balance ):
        '''
        setter for checking balance
        '''
        self.balance_checking = new_balance



    def set_savings_balance( self , new_balance ):
        '''
        setter for savings balance
        '''

        self.balance_savings = new_balance



    def get_checking_balance( self ):
        '''
        getter for checking balance
        '''

        return self.balance_checking 



    def get_savings_balance( self ):
        '''
        getter for savings balance
        '''
        return self.balance_savings



    def __str__ (self):
        return f'Account ID: {self.account_id}, Name: {self.first_name} {self.last_name}, Password: {self.password}'



############################################### END OF CUSTOMER CLASS

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
            existing_customer["account_id"]
        )


    # debugging
    # Customer.add_new_customer('renad', 'alsadun', 'password', '0292.2', 0.0 )

    # for customer in Customer.all_customers:
    #     print(customer)

    # print(Customer.next_account_id)
    #end of debugging




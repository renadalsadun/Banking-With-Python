from customer import Customer
from access_file import log_transaction #(account_id, transaction_type, amount, balance)


class Account():

    def __init__(self, customer: Customer , activity = True , overdraft = 0 ):
        self.customer = customer
        self.checking_balance = customer.get_checking_balance()
        self.saving_balance = customer.get_saving_balance()
        self.activity = activity
        self.overdraft = overdraft



    def is_active(self):

        if self.overdraft < 2:
            self.activity = True
        
        else:
            self.activity = False
            
        return self.activity



    def check_balance( self , balance , amount ):

        '''
        Returns True if the operation is valid, otherwise returns False 
        
        '''

        if self.is_active():

            if balance - (amount + 35) >= -100:
                return True
            
            else:
                return False
            
        else:
            return False



    def update_checking_balance(self, new_balance):
        self.customer.set_checking_balance(new_balance)



    def update_saving_balance(self, new_balance):
        self.customer.set_saving_balance(new_balance)



    def withdraw_from_savings( self , amount ):

        if self.check_balance( self.saving_balance , amount ):
            
            if self.overdraft == 0:
                if self.saving_balance - amount < 0:
                    self.saving_balance -= ( amount + 35 )
                    self.overdraft += 1
                    self.update_saving_balance(self.saving_balance)
                    print('Overdraft! Charged $35 fee') 
                    log_transaction( self.customer.account_id, "withdrawal from savinf", amount, self.customer.balance_savings)



                else:
                    self.saving_balance = self.saving_balance - amount
                    self.update_saving_balance(self.saving_balance)
                    log_transaction( self.customer.account_id, "withdrawal from saving", amount, self.customer.balance_savings)

                print(f'Withdrawal successful. New saving balance: ${self.saving_balance}')

            elif self.overdraft == 1:
                if self.saving_balance - (amount + 35) >= -100:
                    self.saving_balance -= (amount + 35)
                    self.update_saving_balance(self.saving_balance)
                    self.overdraft += 1
                    print('Overdraft! Charged $35 fee')
                    log_transaction( self.customer.account_id, "withdrawal from savinf", amount, self.customer.balance_savings) 
                    self.is_active()

                else:
                    print( " not enough funds to withdraw! " )
        else:
            print( " not enough funds to withdraw! " )



    def withdraw_from_checking( self , amount ):

        if self.check_balance( self.checking_balance , amount ):
            
            if self.overdraft == 0:
                if self.checking_balance - amount < 0:
                    if self.checking_balance - (amount + 35) >= -100:
                        self.checking_balance -= ( amount + 35 )
                        self.overdraft += 1
                        self.update_checking_balance(self.checking_balance)
                        log_transaction( self.customer.account_id, "withdrawal from checking", amount, self.customer.balance_checking)
                        print('Overdraft! Charged $35 fee') 
                    else:
                        print ("can not withdraw, not enough funds!")

                else:
                    self.checking_balance -=  amount
                    self.update_checking_balance(self.checking_balance)
                    log_transaction( self.customer.account_id, "withdrawal from checking", amount, self.customer.balance_checking)

                    
                print(f'Withdrawal successful. New checking balance: ${self.checking_balance}')

            elif self.overdraft == 1:
                if self.checking_balance - (amount + 35) >= -100:
                    self.checking_balance -= (amount + 35)
                    self.update_checking_balance(self.checking_balance)
                    log_transaction( self.customer.account_id, "withdrawal from checking", amount, self.customer.balance_checking)

                    self.overdraft += 1
                    print('Overdraft! Charged $35 fee') 
                    print(f'Withdrawal successful. New checking balance: ${self.checking_balance}')
                    self.is_active()

                else:
                    print( " not enough funds to withdraw! " )
        else:
            print( " not enough funds to withdraw! " )



    def deposite(self, account, amount):
        if account == 'checking':
            self.checking_balance += amount
            self.update_checking_balance(self.checking_balance)
            print(f'Deposite successful. New checking balance: ${self.checking_balance}')
            log_transaction( self.customer.account_id, "deposit from checking", amount, self.customer.balance_checking)


        elif account == 'saving':
            self.saving_balance += amount
            self.update_saving_balance(self.saving_balance)
            print(f'Deposite successful. New saving balance: ${self.saving_balance}')
            log_transaction( self.customer.account_id, "deposit from saving", amount, self.customer.balance_savings)

        else:
            print('wrong account, deposite not successful')



    def transfer( self, amount, account, target_account_id ):

        target_customer = Customer.find_customer(target_account_id)

        #if the customer was found
        if target_customer:

        # CASE 1: transfering between accounts of the same customer
            if target_account_id == self.customer.account_id: 

                #  CHECKING -> SAVING
                if account.lower() == 'checking':
                    
                    #to determine if the withdrawal waas successfully made 
                    old_checking = self.checking_balance
                    self.withdraw_from_checking(amount)

                    #if the withdrawal failed
                    if old_checking == self.checking_balance:
                        print("Transfer failed! ")

                    # if the withdrawal was successful
                    else:
                        self.deposite('saving', amount)
                        print("Transfer from checking to savings was successful!")


                # SAVING -> CHECKING
                elif account.lower() == 'saving':
                                        
                    #to determine if the withdrawal waas successfully made 
                    old_saving = self.saving_balance
                    self.withdraw_from_savings(amount)

                    #if the withdrawal failed
                    if old_saving == self.saving_balance:
                        print("Transfer failed! ")

                    # if the withdrawal was successful
                    else:
                        self.deposite('checking', amount)
                        print("Transfer from saving to checking was successful!")


                else:
                    print (f'Account ({account}) is not correct, enter either checking or saving!')

        # CASE 2: transfering to another customer's account (only to target customer’s checking)       
            else:
                target_account = Account(target_customer)
                if account.lower() == 'checking':
                    
                    #to determine if the withdrawal waas successfully made 
                    old_checking = self.checking_balance
                    self.withdraw_from_checking(amount)

                    #if the withdrawal failed
                    if old_checking == self.checking_balance:
                        print("Transfer failed! ")

                    # if the withdrawal was successful
                    else:
                        target_account.deposite('checking', amount)
                        print(f"Transfer to account {target_account_id} was successful!")



                elif account.lower() == 'saving':
                                        
                    #to determine if the withdrawal waas successfully made 
                    old_saving = self.saving_balance
                    self.withdraw_from_savings(amount)

                    #if the withdrawal failed
                    if old_saving == self.saving_balance:
                        print("Transfer failed! ")

                    # if the withdrawal was successful
                    else:
                        target_account.deposite('checking', amount)
                        print(f"Transfer to account {target_account_id} was successful!")


                
                else:
                    print (f'Account ({account}) is not correct, enter either checking or saving!')

    #if the target customer was not found
        else:
            print (f'Account with id number {target_account_id} was not found')



############################ Debugging

test_customer = Customer("Test", "User", "password", balance_checking=100, balance_savings=100)
test_account = Account(test_customer)
print(f'\ncurrent checking balance = {test_account.checking_balance}\ncurrent activity = {test_account.activity}\ncurrent overdraft = {test_account.overdraft}\n')
print('operation to be done : withdraw 100\nrun result: \n')
# First overdraft (should allow and charge $35 fee)
test_account.withdraw_from_checking(100)  # Expect overdraft warning

print(f'\ncurrent checking balance = {test_account.checking_balance}\ncurrent activity = {test_account.activity}\ncurrent overdraft = {test_account.overdraft}\n')
print('operation to be done : withdraw 5\nrun result: \n')

# Second overdraft (should allow and charge another $35 fee, leading to deactivation)
test_account.withdraw_from_checking(5)  # Expect overdraft warning and deactivation

print(f'\ncurrent checking balance = {test_account.checking_balance}\ncurrent activity = {test_account.activity}\ncurrent overdraft = {test_account.overdraft}\n')
print('operation to be done : withdraw 5\nrun result: \n')

# Third withdrawal (should be blocked)
test_account.withdraw_from_checking(5)  # Expect "Transaction failed" message
print(f'\ncurrent checking balance = {test_account.checking_balance}\ncurrent activity = {test_account.activity}\ncurrent overdraft = {test_account.overdraft}\n')


print('operation to be done : withdraw 5\nrun result: \n')

# Third withdrawal (should be blocked)
test_account.withdraw_from_checking(5)  # Expect "Transaction failed" message
print(f'\ncurrent checking balance = {test_account.checking_balance}\ncurrent activity = {test_account.activity}\ncurrent overdraft = {test_account.overdraft}\n')


# Checking if account is actually inactive
is_active_status = test_account.is_active()
is_active_status

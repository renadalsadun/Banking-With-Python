from customer import Customer
from access_file import log_transaction #(account_id, transaction_type, amount, balance)


class Account():

    def __init__(self, customer: Customer , activity = True , overdraft = 0 ):
        self.customer = customer
        self.checking_balance = customer.get_checking_balance()
        self.savings_balance = customer.get_savings_balance()
        self.activity = activity
        self.overdraft = overdraft



    def is_active(self):
        '''
        checks the overdraft, if it is less than 2, the account is active. otherwise the account is not active
        '''
        if self.overdraft < 2:
            self.activity = True
        
        else:
            self.activity = False
            
        return self.activity



    def check_balance( self , balance , amount ):

        '''
        Returns True if the operation is valid (will not exceed the limit), otherwise returns False 
        
        '''

        if self.is_active():

            if balance - (amount + 35) >= -100:
                return True
            
            else:
                return False
            
        else:
            return False



    def update_checking_balance(self, new_balance):
        '''
        updates the checking balance for the customer 
        '''
        self.customer.set_checking_balance(new_balance)



    def update_savings_balance(self, new_balance):        
        '''
        updates the savings balance for the customer 
        '''

        self.customer.set_savings_balance(new_balance)



    def withdraw_from_savings( self , amount ):
        '''
        checks if the account is active. if it is proceeds with the withdrawal transaction
        withdraws the amount from the savings account if it doesn't result in a negative balance, otherwise the withdrawal is not processed
        '''
        if self.activity:
            if self.savings_balance - amount < 0: # it the balance will be negative
                print(f'Not enough funds to withdraw!\nsavings account balance : {self.savings_balance}')
            else:
                self.savings_balance -= amount
                self.update_savings_balance(self.savings_balance)
                log_transaction( self.customer.account_id, "withdrawal from savings", amount, self.savings_balance)
                print(f'Withdrawal successful. New savings balance: ${self.savings_balance}')
        else:
            print(f"Account is Deactivated! Deposit the required amount into Checking Account to activate it!\nRequired Amount: {self.checking_balance} ")



    def withdraw_from_checking( self , amount ):
        '''
        checks if the account is active. if it is proceeds with the withdrawal transaction
        withdraws the amount from the checking account if it doesn't exceed the limit (-100), otherwise the withdrawal is not processed
        updates overdraft based on account status, deactivates account if the overdraft reached 2
        '''
        successful_withdraw_flag = True
        if self.activity:
            if self.check_balance( self.checking_balance , amount ):
                
                if self.overdraft == 0:
                    if self.checking_balance - amount < 0: #if the balance will go negative
                        if self.checking_balance - (amount + 35) >= -100: # if it won't go below the limit
                            self.checking_balance -= ( amount + 35 )
                            self.overdraft += 1
                            self.update_checking_balance(self.checking_balance)
                            log_transaction( self.customer.account_id, "withdrawal from checking", amount, self.customer.balance_checking)
                            print('Overdraft! Charged $35 fee') 
                            successful_withdraw_flag = True

                        else:                                             # if it does go below the limit!
                            print ("Can not withdraw, not enough funds!")
                            successful_withdraw_flag = False 

                    else:
                        self.checking_balance -=  amount
                        self.update_checking_balance(self.checking_balance)
                        log_transaction( self.customer.account_id, "withdrawal from checking", amount, self.customer.balance_checking)
                        successful_withdraw_flag = True
                        
                    if successful_withdraw_flag:    
                        print(f'Withdrawal successful. New checking balance: ${self.checking_balance}')

                elif self.overdraft == 1:
                    if self.checking_balance - (amount + 35) >= -100: # wont go below limit
                        self.checking_balance -= (amount + 35)
                        self.update_checking_balance(self.checking_balance)
                        log_transaction( self.customer.account_id, "withdrawal from checking", amount, self.customer.balance_checking)

                        self.overdraft += 1
                        print('Overdraft! Charged $35 fee') 
                        print(f'Withdrawal successful. New checking balance: ${self.checking_balance}')
                        self.is_active()
                        if not self.activity:
                            print(f"Account is Deactivated! Deposit the required amount into Checking Acoount to activate it\nRequired Amount: {self.checking_balance} ")


                    else:
                        print( "Not enough funds to withdraw! " )
            else:
                print( "Not enough funds to withdraw! " )
        else:
            print(f"Account is Deactivated! Deposit the required amount to activate it\nRequired Amount: {self.checking_balance} ")



    def deposit(self, account, amount):
        '''
        deposit the amount in either savings or checking accounts, updates the customer, logs the transaction,
        and check if the account will be reactivated after the deposit in checking account
        '''

        if account == 'checking':
            self.checking_balance += amount
            self.update_checking_balance(self.checking_balance)
            print(f'Deposit successful! New checking balance: ${self.checking_balance}')
            log_transaction( self.customer.account_id, "Deposit from checking", amount, self.checking_balance)
            self.reactivate_account()

        elif account == 'savings':
            self.savings_balance += amount
            self.update_savings_balance(self.savings_balance)
            print(f'Deposit successful! New savings balance: ${self.savings_balance}')
            log_transaction( self.customer.account_id, "Deposit from savings", amount, self.savings_balance)

        else:
            print('Wrong account, deposite not successful')



    def transfer( self, amount, account, target_account_id ):
        '''
        transfers the amount between accounts
        transfers can occur:
        1. Between the checking and savings accounts of the same customer
        2. From the checking or savings account of one customer (logged in) to the checking account of another customer

        if the withdrawal is successful, the corresponding deposit is made in the target account
        if the withdrawal fails (due to insufficient funds), the transfer is aborted
        '''

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
                        self.deposit('savings', amount)
                        print(f"Transfering {amount} from checking to savings was successful!")


                # SAVING -> CHECKING
                elif account.lower() == 'savings':
                    
                    #to determine if the withdrawal waas successfully made 
                    old_savings = self.savings_balance
                    self.withdraw_from_savings(amount)

                    #if the withdrawal failed
                    if old_savings == self.savings_balance:
                        print("Transfer failed! ")

                    # if the withdrawal was successful
                    else:
                        self.deposit('checking', amount)
                        print(f"Transfering ${amount} from savings to checking was successful!")


                else:
                    print (f'Account ({account}) is not correct, enter either checking or savings!')

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
                        target_account.deposit('checking', amount)
                        target_account.customer.set_checking_balance(target_account.checking_balance)

                        print(f"Transfering ${amount} to account {target_account_id} was successful!")
                        



                elif account.lower() == 'savings':
                                        
                    #to determine if the withdrawal waas successfully made 
                    old_savings = self.savings_balance
                    self.withdraw_from_savings(amount)

                    #if the withdrawal failed
                    if old_savings == self.savings_balance:
                        print("Transfer failed! ")

                    # if the withdrawal was successful
                    else:
                        target_account.deposit('checking', amount)
                        print(f"Transfering {amount} to account {target_account_id} was successful!")


                
                else:
                    print (f'Account ({account}) is not correct, enter either checking or savings!')

    #if the target customer was not found
        else:
            print (f'Account with id number {target_account_id} was not found')



    def reactivate_account(self):
        '''
        reactivates the account if it is deactivated
        the account will be reactivated only if the balance is not ,
        by resetting the overdraft to zero and the activity to true
        note: the method is also used to reset overdrafts if the customer deposits the required amount!
        '''
        if self.checking_balance >= 0:
            self.overdraft = 0
            if not self.is_active():
                self.is_active()
                print(f"Account Reactivated! cuurent checking balance {self.checking_balance}")


































############################ Debugging
if __name__ == '__main__':

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

    test_account.deposit('checking',500)  # Expect "Transaction failed" message
    print(f'\ncurrent checking balance = {test_account.checking_balance}\ncurrent activity = {test_account.activity}\ncurrent overdraft = {test_account.overdraft}\n')

    # Checking if account is actually inactive
    is_active_status = test_account.is_active()
    is_active_status

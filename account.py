from customer import Customer




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

        if self.is_active( self):

            if balance - amount - 35 >= -100:
                return True
            
            else:
                return False
            
        else:
            return False



    def withdraw_from_savings( self , amount ):

        if self.check_balance( self.saving_balance , amount ):
            
            if self.overdraft == 0:
                if self.saving_balance - amount < 0:
                    self.saving_balance -= ( amount + 35 )
                    self.overdraft += 1
                    self.update_saving_balance(self.saving_balance)
                    print('Overdraft! Charged $35 fee') 


                else:
                    self.saving_balance = self.saving_balance - amount
                    self.update_saving_balance(self.saving_balance)
                    
                print(f'Withdrawal successful. New saving balance: ${self.saving_balance}')

            elif self.overdraft == 1:
                if self.saving_balance - (amount + 35) >= -100:
                    self.saving_balance -= (amount + 35)
                    self.update_saving_balance(self.saving_balance)
                    self.overdraft += 1
                    print('Overdraft! Charged $35 fee') 
                    self.is_active()

                else:
                    print( " not enough funds to withdraw! " )
                    

    

    def update_checking_balance(self, new_balance):
        self.customer.set_checking_balance(new_balance)

    def update_saving_balance(self, new_balance):
        self.customer.set_saving_balance(new_balance)


    def withdraw_from_checking( self , amount ):

        if self.check_balance( self.checking_balance , amount ):
            
            if self.overdraft == 0:
                if self.checking_balance - amount < 0:
                    self.checking_balance -= ( amount + 35 )
                    self.overdraft += 1
                    self.update_checking_balance(self.checking_balance)
                    print('Overdraft! Charged $35 fee') 


                else:
                    self.checking_balance -=  amount
                    self.update_checking_balance(self.checking_balance)
                    
                print(f'Withdrawal successful. New checking balance: ${self.checking_balance}')

            elif self.overdraft == 1:
                if self.checking_balance - (amount + 35) >= -100:
                    self.checking_balance -= (amount + 35)
                    self.update_checking_balance(self.checking_balance)
                    self.overdraft += 1
                    print('Overdraft! Charged $35 fee') 
                    print(f'Withdrawal successful. New checking balance: ${self.checking_balance}')
                    self.is_active()

                else:
                    print( " not enough funds to withdraw! " )
                    
    def deposite(self, account, amount):
        if account == 'checking':
            self.checking_balance += amount
            self.update_checking_balance(self.checking_balance)
            print(f'Deposite successful. New checking balance: ${self.checking_balance}')

        elif account == 'saving':
            self.saving_balance += amount
            self.update_saving_balance(self.saving_balance)
            print(f'Deposite successful. New saving balance: ${self.saving_balance}')

        else:
            print('wrong account, deposite not successful')

    def transfer( self, amount, account, target_account_id ):
        if account == 'checking':
            self.withdraw_from_checking(amount)
            targer_customer = Customer.find_costumer(target_account_id)
            if targer_customer:
                target_account = Account(targer_customer)
                target_account.deposite(amount)
            else:
                print('target not found')

            self.customer.set_checking_balance(self.checking_balance + amount)
            self.update_checking_balance(self.checking_balance)
            print(f'Deposite successful. New checking balance: ${self.checking_balance}')

        elif account == 'saving':
            self.customer.set_saving_balance(self.saving_balance + amount)
            self.update_saving_balance(self.saving_balance)
            print(f'Deposite successful. New saving balance: ${self.saving_balance}')

        else:
            print('wrong account, deposite not successful')



    # @classmethod
    # def overdraft(cls):
    #     pass




# class Account():
#     def __init__(self):
#         pass

#     @classmethod
#     def check_balance(cls):
#         pass

#     @classmethod
#     def withdraw_from_savings( cls, customer, amount ):
#         pass

#     @classmethod
#     def withdraw_from_checking( cls , customer , amount ):
#         pass

#     @classmethod
#     def transfer( cls, amount, customer, target_account_id , target_account ):
#         pass

#     @classmethod
#     def overdraft(cls):
#         pass

#     @classmethod 
#     def is_active(cls):
#         pass
from customer import Customer 
from access_file import reading_from_file, write_to_file
from account import Account
import unittest



#####################################################################################
#                           CUSTOMER CLASS TESTS                                    #
##################################################################################### 



class Test_Customer(unittest.TestCase):


    def setUp(self): 
        Customer.all_customers.clear()
        Customer.next_account_id = 10001



# reading_from_file() Method Testing:
#   - successfully read files 
#   - returns list with dictionary header if file not found
    
    def test_reading_from_file(self):
        header = [ 'account_id' , 'first_name' , 'last_name' , 'password' , 'balance_checking' , 'balance_savings' ] 

        test_reading_valid = reading_from_file('data')
        self.assertIsNotNone(test_reading_valid)
        self.assertEqual(test_reading_valid[0]['account_id'], '10001')
        test_reading_invalid = reading_from_file('not valid')
        self.assertEqual(test_reading_invalid, [dict.fromkeys(header, '')])
        




# add_new_customer() Method Testing:
#   - successfully adds a new customer to the all_customers list
#   - successfully assign the newly added customer's attributes (first name, last name, password, checking balance, saving balance)
#   - successfully assign a unique account id
#   - confirms that calling add_new_customer() without optional parameters doesn't break functionality
#   - increments next_account_id 
#   - successfully adds a customer with default balance values if not provided
#   - succseefully adds a customer if only balance checking or only balance saving is provided


    def test_add_new_customer(self):
        customer = Customer.add_new_customer('fname', 'lastname', 'password', 100 , 90)

        self.assertEqual(len(Customer.all_customers), 1)

        self.assertEqual(customer.first_name, 'fname')
        self.assertEqual(customer.last_name, 'lastname')
        self.assertEqual(customer.password, 'password')
        self.assertEqual(customer.balance_checking, 100)
        self.assertEqual(customer.balance_savings, 90)
        self.assertEqual(customer.account_id, 10001)
        self.assertEqual(Customer.next_account_id, 10002)
        customer_default = Customer.add_new_customer('default', 'user', 'password')
        self.assertEqual(customer_default.balance_checking, 0.0)
        self.assertEqual(customer_default.balance_savings, 0.0)
        customer_only_checking_account = Customer.add_new_customer('name', 'name2', 'password',   90)
        self.assertEqual(customer_only_checking_account.balance_checking, 90.0)
        self.assertEqual(customer_only_checking_account.balance_savings, 0.0)

        customer_only_saving_account = Customer.add_new_customer('name', 'name2', 'password',balance_savings = 90)
        self.assertEqual(customer_only_saving_account.balance_checking, 0.0)
        self.assertEqual(customer_only_saving_account.balance_savings, 90.0)



# Test for find_customer() Method:
#   - successfully finds a customer by their account id
#   - successfully returns the found customer instance 
#   - successfully returns none if the provided argument -account id- was invalid

    def test_find_customer(self):
        added_customer = Customer.add_new_customer('Renad', 'Alsadun', 'PASS@WORD', 1000, 500)
        found_customer = Customer.find_customer(int(added_customer.account_id))
        self.assertIsNotNone(found_customer)
        self.assertEqual(found_customer.first_name, 'Renad')
        self.assertIsNone(Customer.find_customer(0000))
        

        invalid_customer = Customer.add_new_customer('invalid', 'user', 'password', 'string balance!', None)
        self.assertIsNone(invalid_customer)
        invalid_customer_2 = Customer.add_new_customer('', '', '', None, None)
        self.assertIsNone(invalid_customer_2)




#####################################################################################
#                                ACCOUNT CLASS TESTS                                #
#####################################################################################

class Test_Account(unittest.TestCase):

    def setUp(self): 
        self.customer_1 = Customer.add_new_customer("Test", "User1", "password", balance_checking=100, balance_savings=100)
        self.account_1 = Account(self.customer_1)
        self.customer_2 = Customer.add_new_customer("Test2", "user2", "password2", balance_checking=200, balance_savings=150)
        self.account_2 = Account(self.customer_2)


# Test for is_active() Method:
#   - returns true is the account overdraft is 1 or 0
#   - returns flase (deactivates the account) if the overdraft is 2
#   - successfully updates the activity status correctly

    def test_is_active(self):
        self.account_1.overdraft = 0
        self.assertTrue(self.account_1.is_active())

        self.account_1.overdraft = 1
        self.assertTrue(self.account_1.is_active())

        self.account_1.overdraft = 2
        self.assertFalse(self.account_1.is_active())
        self.assertFalse(self.account_1.activity)

        self.account_1.overdraft = 1        
        self.assertTrue(self.account_1.is_active())
        self.assertTrue(self.account_1.activity)


# Test for check_balance() Method:
#   - returns true when there are enough funds and the account is active
#   - returns false when the account is deactivated and the balance is sufficient
#   - returns false when there aren't enough funds after the $35 fee
#   - returns false when the account is active but the balance will go below the minimum
#   - returns False if the account is deactivated

    def test_check_balance(self):

        self.account_1.activity = True
        self.assertTrue(self.account_1.check_balance(self.account_1.checking_balance, 50))
        
        self.assertFalse(self.account_1.check_balance(self.account_1.checking_balance, 165.5))

        self.account_1.overdraft = 2
        self.account_1.activity = self.account_1.is_active()
        self.assertFalse(self.account_1.check_balance(self.account_1.checking_balance, 10))
        
        self.account_1.overdraft = 1
        self.account_1.activity = self.account_1.is_active()
        self.assertFalse(self.account_1.check_balance(self.account_1.checking_balance, 200))

        self.assertTrue(self.account_1.check_balance(self.account_1.checking_balance, 40))


# Test for update_checking_balance() Method:

#   - updates the checking balance when a new value is passed
#   - updates the checking balance even when the new balance is 0.0
#   - updates the checking balance with a negative value

    def test_update_checking_balance(self):

        self.account_1.update_checking_balance(100)
        self.assertEqual(self.customer_1.balance_checking, 100)

        self.account_1.update_checking_balance(0.0)
        self.assertEqual(self.customer_1.balance_checking, 0.0)

        self.account_1.update_checking_balance(-100)
        self.assertEqual(self.customer_1.balance_checking, -100)

# Test for update_savings_balance() Method:

#   - updates the savings balance when a new value is passed
#   - updates the savings balance even when the new balance is 0.0
#   - updates the savings balance with a negative value

    def test_update_savings_balance(self):

        self.account_1.update_savings_balance(100)
        self.assertEqual(self.customer_1.balance_savings, 100)

        self.account_1.update_savings_balance(0.0)
        self.assertEqual(self.customer_1.balance_savings, 0.0)

        self.account_1.update_savings_balance(-100)
        self.assertEqual(self.customer_1.balance_savings, -100)


# Test for withdraw_from_savings() Method:

#   - successfully withdraws from savings when there are sufficient funds and no overdraft fee is charged
#   - successfully withdraws from savings with a $35 fee if balance falls below $0
#   - successfully prevents withdrawal from savings if the account is deactivated
#   - confirms no withdrawal can occur if there are insufficient funds

    def test_withdraw_from_savings(self):
        self.account_1.withdraw_from_savings(1)
        self.assertEqual(self.account_1.savings_balance, 99)

        self.account_1.withdraw_from_savings(120)
        self.assertEqual(self.account_1.savings_balance, -56)  
        self.assertEqual(self.account_1.overdraft, 1)

        self.account_1.withdraw_from_savings(1) #now the account is deactivated
        self.assertEqual(self.account_1.overdraft, 2)
        self.assertEqual(self.account_1.savings_balance, -92) 
        self.account_1.withdraw_from_savings(1) 
        self.assertEqual(self.account_1.savings_balance, -92)  # doesnt change because withdrawals are prevented
        
        self.account_1.savings_balance = 100
        self.account_1.withdraw_from_savings(200) 
        self.assertEqual(self.account_1.savings_balance, 100) #doesnt change cuz there is insufficient funds 

# Test for withdraw_from_checking() Method:

#   - successfully withdraws from checking when there are sufficient funds and no overdraft fee is charged
#   - successfully withdraws from checking with a $35 fee if balance falls below $0
#   - successfully prevents withdrawal from checking if the account is deactivated
#   - confirms no withdrawal can occur if there are insufficient funds

    def test_withdraw_from_checking(self):
        self.account_1.withdraw_from_checking(1)
        self.assertEqual(self.account_1.checking_balance, 99)

        self.account_1.withdraw_from_checking(120)
        self.assertEqual(self.account_1.checking_balance, -56)  
        self.assertEqual(self.account_1.overdraft, 1)

        self.account_1.withdraw_from_checking(1) #now the account is deactivated
        self.assertEqual(self.account_1.overdraft, 2)
        self.assertEqual(self.account_1.checking_balance, -92) 
        self.account_1.withdraw_from_checking(1) 
        self.assertEqual(self.account_1.checking_balance, -92)  # doesnt change because withdrawals are prevented
        
        self.account_1.checking_balance = 100
        self.account_1.withdraw_from_checking(200) 
        self.assertEqual(self.account_1.checking_balance, 100) #doesnt change cuz there is insufficient funds 

# Test for deposit() Method:

#   - deposits into the checking account and updates the balance
#   - deposits into the savings account and updates the balance
#   - handles invalid deposit when the wrong account type is provided

    def test_deposit(self):
        
        self.account_1.deposit('checking', 50)
        self.assertEqual(self.account_1.checking_balance, 150) # 100 + 50

        self.account_1.deposit('savings', 15.98)
        self.assertEqual(self.account_1.savings_balance, 115.98) # 100 + 15.98 

        self.account_1.deposit('investment', 50)  
        self.assertEqual(self.account_1.checking_balance, 150) # doesnt change
        self.assertEqual(self.account_1.savings_balance, 115.98) # also doesnt change

# Test for transfer() Method:

#   - transfers from checking to savings within the same account
#   - transfers from savings to checking within the same account
#   - transfers from checking to another customer’s checking account XXXXX
#   - transfers from savings to another customer’s checking account XXXXX
#   - prevents transfer if there are insufficient funds or invalid account details

    def test_transfer(self):

# customer 1 checking: 100
# customer 1 savings: 100

        self.account_1.transfer(50, 'checking', self.customer_1.account_id)
        self.assertEqual(self.account_1.checking_balance, 50)
        self.assertEqual(self.account_1.savings_balance, 150)

# customer 1 checking: 50
# customer 1 savings: 150

        self.account_1.transfer(50, 'savings', self.customer_1.account_id)
        self.assertEqual(self.account_1.savings_balance, 100)
        self.assertEqual(self.account_1.checking_balance, 100)

# customer 1 checking: 100
# customer 1 savings: 100
# customer 2 checking: 200
# customer 2 savings: 150

        self.account_1.transfer(50, 'checking', self.customer_2.account_id)
        self.assertEqual(self.account_1.checking_balance, 50)
        self.assertEqual(self.customer_2.balance_checking, 250)

# customer 1 checking: 50
# customer 1 savings: 100
# customer 2 checking: 250
# customer 2 savings: 150

        self.account_1.transfer(50, 'savings', self.customer_2.account_id)
        self.assertEqual(self.account_1.savings_balance, 50)
        self.assertEqual(self.customer_2.balance_checking, 300)

# customer 1 checking: 50
# customer 1 savings: 50
# customer 2 checking: 300
# customer 2 savings: 150

        self.account_1.transfer(500, 'savings', self.customer_1.account_id)
        self.assertEqual(self.account_1.savings_balance, 50) # doesnt change because there is not enough funds
        self.assertEqual(self.account_1.checking_balance, 50) # same

# customer 1 checking: 50
# customer 1 savings: 50








# if __name__ == '__main__':
    # unittest.main(verbosity=2)
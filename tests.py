#####################################################################################
#                           CUSTOMER CLASS TESTS                                    #
##################################################################################### 

from customer import reading_from_file, Customer 
import unittest

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



# Test for find_customer() Method:
#   - successfully finds a customer by their account id
#   - successfully returns the found customer instance 
#   - successfully returns none if the provided argument -account id- was invalid

    def test_find_customer(self):
        added_customer = Customer.add_new_customer('Renad', 'Alsadun', 'PASS@WORD', 1000, 500)
        found_customer = Customer.find_costumer(int(added_customer.account_id))
        self.assertIsNotNone(found_customer)
        self.assertEqual(found_customer.first_name, 'Renad')
        self.assertIsNone(Customer.find_costumer(0000))
        

        invalid_customer = Customer.add_new_customer('invalid', 'user', 'password', 'string balance!', None)
        self.assertIsNone(invalid_customer)
        invalid_customer_2 = Customer.add_new_customer('', '', '', None, None)
        self.assertIsNone(invalid_customer_2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
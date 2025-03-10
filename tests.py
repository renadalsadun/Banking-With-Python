#####################################################################################
#                           CUSTOMER CLASS TESTS                                    #
##################################################################################### 

from customer import reading_from_file, Customer 
import unittest

class Test_Customer(unittest.TestCase):


    # def setUp(self): 
        # self.customer = Customer()
        # test_customer = Customer.add_new_customer('fname', 'lastname', 'password', 100 , 90)



# reading_from_file() Method Testing:
#   # successfully read files 
    
    def test_reading_from_file(self):
        test_reading = reading_from_file('data')
        self.assertIsNotNone(test_reading)
        self.assertEqual(test_reading[0]['account_id'], '10001')



# add_new_customer() Method Testing:
#   - successfully adds a new customer to the all_customers list
#   - successfully assign the newly added customer's attributes (first name, last name, password, checking balance, saving balance)


    def test_add_new_customer(self):
        customer = Customer.add_new_customer('fname', 'lastname', 'password', 100 , 90)

        self.assertEqual(len(Customer.all_customers), 1)

        self.assertEqual(customer.first_name, 'fname')
        self.assertEqual(customer.last_name, 'lastname')
        self.assertEqual(customer.password, 'password')
        self.assertEqual(customer.balance_checking, 100)
        self.assertEqual(customer.balance_savings, 90)

        for customer in (Customer.all_customers):
            print(customer.first_name)

    def test_find_customer(self):
        added_customer = Customer.add_new_customer('Renad', 'Alsadun', 'PASS@WORD', 1000, 500)
        found_customer = Customer.find_costumer(int(added_customer.account_id))
        self.assertIsNotNone(found_customer)
        self.assertEqual(found_customer.first_name, 'Renad')
        self.assertIsNone(Customer.find_costumer(0000))

if __name__ == '__main__':
    unittest.main(verbosity=2)
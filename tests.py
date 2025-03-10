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
        print('hi')
        test_reading = reading_from_file('data')
        self.assertIsNotNone(test_reading)
        self.assertEqual(test_reading[0]['account_id'], '10001')



    def test_add_new_customer(self):
        Customer.add_new_customer('fname', 'lastname', 'password', 100 , 90)
        print(Customer.get_number_of_customers())
        # self.assertEqual(Customer.get_number_of_customers(), 1)         
        for customer in (Customer.all_customers):
            print(customer.first_name)


if __name__ == '__main__':
    unittest.main(verbosity=2)
#####################################################################################
#                                     CUSTOMER                                      #
##################################################################################### 

from customer import reading_from_file
import unittest

class Test_Customer(unittest.TestCase):

# reading_from_file() Method Testing:

#TEST CASES
    # I want to be able to read files 

    def test_reading_from_file(self):
        # print(reading_from_file('data'))
        self.assertIsNotNone(reading_from_file('data'))



if __name__ == '__main__':
    unittest.main(verbosity=2)
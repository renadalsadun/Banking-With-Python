# Prompt
# ACME Bank uses a file structure called bank.csv. 
# The cashiers will use this brand-new software to manage transactions, and you have been tasked with developing it.

# account_id	frst_name	last_name	password	balance_checking	balance_savings
# 10001	suresh	sigera	juagw362	1000	10000
# 10002	james	taylor	idh36%@#FGd	10000	10000
# ...	...	...	...	...	...
# To read from and write to this "database" you can use the python csv module. 
# How to do this is here: https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/

# write the entire Python program using classes, methods, file handling, and exception handling to meet the functional requirements below:

# Requirements
# You should have a minimum of:

# 4 classes;
# 1 file (bank.csv given to you);
# You're allowed to add more classes base on the OOP design
# The entire project should be carried out using a test-driven development (TDD) approach


############### Your app should have the following functionality:

# Add New Customer
    # customer can have a checking account
    # customer can have a savings account
    # customer can have both a checking and a savings account

# Withdraw Money from Account (required login)
    # withdraw from savings
    # withdraw from checking

# Deposit Money into Account (required login)
    # can deposit into savings
    # can deposit into checking

# Transfer Money Between Accounts (required login)
    # can transfer from savings to checking
    # can transfer from checking to savings
    # can transfer from checking or savings to another customer's account

# Build Overdraft Protection
    # charge customer ACME overdraft protection fee of $35 when overdraft
    # prevent customer from withdrawing more than $100 USD if account is currently negative
    # the account cannot have a resulting balance of less than -$100 OR
    # the customer cannot make a withdrawal of greater than $100
    # deactivate the account after 2 overdrafts
    # reactivate the account if the customer brings the account current, paying both the overdraft amount and the resulting overdraft fees

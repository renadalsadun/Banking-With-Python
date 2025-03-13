from tabulate import tabulate
from termcolor import colored, cprint
from simple_term_menu import TerminalMenu
from access_file import get_password, get_transactions_by_account_id
from customer import Customer
from account import Account

class Bank():


    cashier_input = ""
    main_menu_options = ['Add new Customer', 'Login to a Customer Account' , 'Quit']
    logged_customer_account_options = ['Withdraw Money from Account', 'Deposit Money into Account', 'Transfer Money Between Accounts', 'View Transaction History','Log Out']
    withdraw_options = ['Withdraw from Checking Account' ,'Withdraw from Savings Account', 'Back to Transactions Menu']
    deposit_options = ['Deposit into Checking Account','Deposit into Savings Account', 'Back to Transactions Menu']
    transfer_options = ['Transfer from Checking to Savings', 
                        'Transfer from Savings to Checking', 
                        'Transfer from Checking to Another Customer\'s Account ', 
                        'Transfer from Savings to Another Customer\'s Account', 
                        'Back to Transactions Menu']
    

    @classmethod
    def menu( cls, options ):
        bank_menu = TerminalMenu(options) 
        selected_index = bank_menu.show()
        selection = options[selected_index]
        return selection



    @classmethod
    def login(cls):
        while True:
            try:
                id = int(input("Enter Account ID: "))
                if not int(id):
                    raise ValueError
                
                password = input("Enter Password: ")
                customer = Customer.login(id,password)

                if customer:
                    return customer 
                else:
                    print(colored("Invalid ID or password. Please try again\n", "red"))

            except ValueError:
                print(colored("Please enter a valid numeric ID. Only numbers are allowed\n", "cyan", attrs=["dark"]))
            selection = cls.menu(["Try Again", "Back to Main Menu"])
            if selection == "Back to Main Menu":
                return None  



    @classmethod
    def logged_customer_menu(cls, logged_customer , logged_account):
        while True:
            print(colored(f"\nWelcome, {logged_customer.first_name} {logged_customer.last_name}!\n", 'cyan'))
            selection = cls.menu(cls.logged_customer_account_options)
            if selection == cls.logged_customer_account_options[0]:  # Withdraw Money from Account
                print(colored('>>> '+cls.logged_customer_account_options[0], 'grey'))
                cls.logged_customer_withdrawal(logged_customer , logged_account)

            elif selection == cls.logged_customer_account_options[1]:  # Deposit Money into Account
                print(colored('>>> '+cls.logged_customer_account_options[1], 'grey'))
                cls.logged_customer_deposit(logged_customer , logged_account)

            elif selection == cls.logged_customer_account_options[2]:  # Transfer Money Between Accounts
                print(colored('>>> '+cls.logged_customer_account_options[2], 'grey'))
                cls.logged_customer_transfer(logged_customer , logged_account)

            elif selection == cls.logged_customer_account_options[3]:  # View Transaction History
                print(colored('>>> '+cls.logged_customer_account_options[3], 'grey'))
                cls.logged_customer_transactions(logged_customer , logged_account)

            else:
                print(colored("Logging out and returning to the main menu...\n", "yellow")) #log out
                break  



    @classmethod
    def logged_customer_withdrawal(cls, logged_customer , logged_account):
        while True:
            print(colored(f"\nWelcome, {logged_customer.first_name} {logged_customer.last_name}!\n", "cyan"))
            selection = cls.menu(cls.withdraw_options)
            if selection == cls.withdraw_options[0]:  # Withdraw from Checking Account
                print(colored('>>>'+cls.withdraw_options[0], 'grey'))

                amount = input('Enter the Amount you want to Withdraw from Checking Account:')
                try:
                    if float(amount):
                        logged_account.withdraw_from_checking(float(amount))
                except ValueError:
                    print(colored("Please enter a valid numeric amount. Only numbers are allowed\n", "cyan", attrs=["dark"]))

                
            elif selection == cls.withdraw_options[1]:  # Withdraw from Savings Account
                print(colored('>>>'+cls.withdraw_options[1], 'grey'))
                            
                amount = input('Enter the Amount you want to Withdraw from Savings Account:')
                try:
                    if float(amount):
                        logged_account.withdraw_from_savings(float(amount))

                except ValueError:
                    print(colored("Please enter a valid numeric amount. Only numbers are allowed\n", "cyan", attrs=["dark"]))

            else:
                print(colored("Exiting out of the Withdrawal menu...\n", "yellow")) #Back to Main Menu
                break  



    @classmethod
    def logged_customer_deposit(cls, logged_customer , logged_account):
        while True:
            print(colored(f"\nWelcome, {logged_customer.first_name} {logged_customer.last_name}!\n", "cyan"))
            selection = cls.menu(cls.deposit_options)
            if selection == cls.deposit_options[0]:  # Deposit into Checking Account
                print(colored('>>>'+cls.deposit_options[0], 'grey'))
                
                amount = input('Enter the Amount you want to Deposit into Checking Account:')
                try:
                    if float(amount):
                        logged_account.deposit('checking', float(amount))
                except ValueError:
                    print(colored("Please enter a valid numeric amount. Only numbers are allowed\n", "cyan", attrs=["dark"]))


            elif selection == cls.deposit_options[1]:  # Deposit into Savings Account
                print(colored('>>>'+cls.deposit_options[1], 'grey'))
                            
                amount = input('Enter the Amount you want to Deposit into Checking Account:')
                try:
                    if float(amount):
                        logged_account.deposit( 'savings',float(amount))
                except ValueError:
                    print(colored("Please enter a valid numeric amount. Only numbers are allowed\n", "cyan", attrs=["dark"]))


            else:
                print(colored("Exiting out of the Deposit menu...\n", "yellow")) #Back to Main Menu
                break  



    @classmethod 
    def logged_customer_transfer(cls, logged_customer, logged_account):
        while True:
            print(colored(f"\nWelcome, {logged_customer.first_name} {logged_customer.last_name}!\n", "cyan"))
            selection = cls.menu(cls.transfer_options)
            if selection == cls.transfer_options[0]:  # Transfer from Checking to Savings
                print(colored('>>>'+cls.transfer_options[0], 'grey'))


                # checking
                amount = input('Enter the Amount you want to Transfer from Checking account into Savings Account:')
                try:
                    if float(amount):
                        logged_account.transfer(float(amount), 'checking', logged_customer.account_id)
                except ValueError:
                    print(colored("Please enter a valid numeric amount. Only numbers are allowed\n", "cyan", attrs=["dark"]))


            elif selection == cls.transfer_options[1]:  # Transfer from Savings to Checking
                print(colored('>>>'+cls.transfer_options[1], 'grey'))


                # savings
                amount = input('Enter the Amount you want to Transfer from Savings account into Checking Account:')
                try:
                    if float(amount):
                        logged_account.transfer(float(amount), 'savings', logged_customer.account_id)
                except ValueError:
                    print(colored("Please enter a valid numeric amount. Only numbers are allowed\n", "cyan", attrs=["dark"]))


            elif selection == cls.transfer_options[2]:  # Transfer from Checking to Another Customer\'s Account
                print(colored('>>>'+cls.transfer_options[2], 'grey'))

                
                try:
                    id = int(input("Enter the Account ID of the user you want to transfer to: "))
                except ValueError:
                    print(colored("Please enter a valid numeric ID. Only numbers are allowed\n", "cyan", attrs=["dark"]))

                if int(id):
                    amount = input(f'Enter the Amount you want to Transfer from your Checking account into {id}\'s Account:')
                    try:
                        if float(amount):
                            logged_account.transfer(float(amount), 'checking', id)
                    except ValueError:
                        print(colored("Please enter a valid numeric amount. Only numbers are allowed\n", "cyan", attrs=["dark"]))


            elif selection == cls.transfer_options[3]:  # Transfer from Savings to Another Customer\'s Account
                print(colored('>>>'+cls.transfer_options[3], 'grey'))

                
                try:
                    id = int(input("Enter the Account ID of the user you want to transfer to: "))
                except ValueError:
                    print(colored("Please enter a valid numeric ID. Only numbers are allowed\n", "cyan", attrs=["dark"]))

                if int(id):
                    amount = input(f'Enter the Amount you want to Transfer from your Savings account into {id}\'s Account:')
                    try:
                        if float(amount):
                            logged_account.transfer(float(amount), 'savings', id)
                    except ValueError:
                        print(colored("Please enter a valid numeric amount. Only numbers are allowed\n", "cyan", attrs=["dark"]))


            else:
                print(colored("Exiting out of the Transfer menu...\n", "yellow")) #Back to Main Menu
                break  



    @classmethod
    def logged_customer_transactions(cls, logged_customer, logged_account):
        transactions = get_transactions_by_account_id('transactions', logged_customer.account_id)
        if transactions:
            headers = ["Timestamp", "Account ID", "Transaction Type", "Amount", "Balance"]
            print(tabulate(transactions, headers=headers, tablefmt="grid"))
        else:
            print(colored("No transactions found for this account. Try making one!\n", 'light_blue'))



    @classmethod
    def create_new_customer(cls):
        flag= False
        user_input = 'Try Again'
        selection = cls.menu(['Create a Checking Account', 'Create a Savings Account', 'Create Both a Checking and a Savings Account'])
        while user_input == 'Try Again':
            try:
                f_name = (input("Enter First Name: "))
                l_name = (input("Enter Last Name: "))
                password = input("Enter Password: ")                    

                if not f_name or not l_name or not password:
                    raise ValueError
                else:
                    if selection == 'Create a Checking Account':
                        new_customer = Customer.add_new_customer(f_name, l_name, password, 0.0)
                    elif selection == 'Create a Savings Account':
                        new_customer = Customer.add_new_customer(f_name, l_name, password, balance_savings = 0.0)
                    else:
                        new_customer = Customer.add_new_customer(f_name, l_name, password, 0.0, 0,0)
                if new_customer :
                    print(colored(f'Customer added successfully!\nCustomer details: {new_customer}','green', attrs=['reverse']))
                    flag = True

            except ValueError:
                print(colored("All fields are required. Please do not leave any field blank\n", "cyan", attrs=["dark"]))
            if not flag:
                print('Would you like to go back to the main menu or attempt again?')
                user_input = cls.menu(['Try Again', 'Back to Main Menu'])
                if user_input == 'Back to Main Menu':
                    break
            else:
                break  



    @classmethod
    def start_bank(cls):

        print(colored("     Welcome to pyBank! \n", 'light_magenta'))

        while True:
            print(colored('\n------------------ pyBank            \n', 'grey', attrs=['bold']))
            selection = cls.menu(cls.main_menu_options)
            if selection == cls.main_menu_options[0]:
                cls.create_new_customer()
            
            elif selection == cls.main_menu_options[1]:
                print(colored(f'>>> {cls.main_menu_options[1]}', 'grey'))
                customer = cls.login()
                if customer:
                    cls.logged_customer_menu(customer, Account(customer))

            else :
                print(colored('It\'s been great having you! \nGoodbye! <3', 'magenta'))
                break


        
        
            # data = [["Name", "Account", "Balance"], ["Alice", "Savings", 1000], ["Bob", "Checking", 2000]]
            # headers = ["Customer Name", "Account Type", "Account Balance"]
            # table = tabulate(data, headers, tablefmt="github")
            # print(table)
            #tablefmt: The table output format such as “plain”, “pipe”, “grid”, or “html”.






pyBank =  Bank()
pyBank.start_bank()
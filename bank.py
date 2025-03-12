from tabulate import tabulate
from termcolor import colored, cprint
from simple_term_menu import TerminalMenu
from access_file import get_password
from customer import Customer
from account import Account

class Bank():

    cashier_input = ""
    main_menu_options = ['Add new Customer', 'Login to a Customer Account' , 'Quit']
    logged_customer_account_options = ['Withdraw Money from Account', 'Deposit Money into Account', 'Transfer Money Between Accounts']
    withdraw_options = ['Withdraw from Checking Account' ,'Withdraw from Savings Account']
    deposit_options = ['Deposit into Checking Account','Deposit into Savings Account']
    transfer_options = ['Transfer from Checking to Savings', 
                        'Transfer from Savings to Checking', 
                        'Transfer from Checking to Another Customer\'s Account ', 
                        'Transfer from Savings to Another Customer\'s Account']
    

    @classmethod
    def menu( cls, options ):
        bank_menu = TerminalMenu(options) 
        selected_index = bank_menu.show()
        selection = options[selected_index]
        return selection

    # @classmethod
    # def action_menu(cls,action_dict):
    #     action = Bank.menu(list(action_dict.keys()))  # Convert keys to list and display as a menu
    #     selected_action = action_dict.get(action)  # Get the method that corresponds to the selected action
    #     selected_action()  # Invoke the selected action



    @classmethod
    def login(cls):
        selection ='Try Again'
        while selection == 'Try Again':
            id = input('Enter Account ID: ')

            try:
                id = int(id)

            except ValueError:
                print(colored('Please enter a valid numeric ID. Only numbers are allowed. Try again', 'cyan', attrs=['dark']))
                print('What do you want to do?')
                selection = Bank.menu(['Try Again', 'Back to Main Menu'])

            if type(id) == int:
                password = get_password(id)
                if password:
                    input_password = input('Enter Password: ')
                    if input_password == password:
                        customer = Customer.find_customer(id)
                else:
                    print 




    @classmethod
    def start_bank(cls):

        print(colored("     Welcome to pyBank! \n", 'light_magenta'))

        selection = ''
        while cls.cashier_input.lower() != 'quit':
            print(colored('\n------------------ pyBank            \n\n', 'grey', attrs=['bold']))
            selection = Bank.menu(Bank.main_menu_options)
            if selection == 'Login to a Customer Account':
                print('login!')
                Bank.login()

            if selection == 'Quit':
                cls.cashier_input = 'Quit'
            # self.cashier_input = input() # input from cashier !


        
        
            # data = [["Name", "Account", "Balance"], ["Alice", "Savings", 1000], ["Bob", "Checking", 2000]]
            # headers = ["Customer Name", "Account Type", "Account Balance"]
            # table = tabulate(data, headers, tablefmt="github")
            # print(table)
            #tablefmt: The table output format such as “plain”, “pipe”, “grid”, or “html”.

pyBank =  Bank()
pyBank.start_bank()
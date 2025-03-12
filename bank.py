from tabulate import tabulate
import termcolor
from simple_term_menu import TerminalMenu

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

    @classmethod
    def action_menu(cls,action_dict):
        action = Bank.menu(list(action_dict.keys()))  # Convert keys to list and display as a menu
        selected_action = action_dict.get(action)  # Get the method that corresponds to the selected action
        selected_action()  # Invoke the selected action


    @classmethod
    def start_bank(cls):

        while cls.cashier_input.lower() != 'quit':
            print("Welcome to pyBank\nWhat are you up to?")
            selection = Bank.menu(Bank.main_menu_options)
            if selection == 'Login to a Customer Account':
                print('login!')
            elif selection == 'Quit':
                cls.cashier_input = 'Quit'
            else:
                print('not login :(')
            # self.cashier_input = input() # input from cashier !


        
        
            # data = [["Name", "Account", "Balance"], ["Alice", "Savings", 1000], ["Bob", "Checking", 2000]]
            # headers = ["Customer Name", "Account Type", "Account Balance"]
            # table = tabulate(data, headers, tablefmt="github")
            # print(table)
            #tablefmt: The table output format such as “plain”, “pipe”, “grid”, or “html”.

pyBank =  Bank()
pyBank.start_bank()
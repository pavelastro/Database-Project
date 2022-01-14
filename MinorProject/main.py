# Telephone Directory Management System

from engine import init
from menu   import show_menu


# connect to db
init()

# display the main menu
while(True):
    show_menu()
    print('\n\n\n\n', end='')

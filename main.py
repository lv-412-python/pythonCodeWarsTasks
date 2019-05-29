"""Menu of the project"""
import sys

import runners as funcs
from runners import get_docstring

FUNCTIONS = {key: getattr(funcs, key) for key in funcs.__all__}


def list_for_all_function():
    '''Shows all functions'''
    for index, values in enumerate(FUNCTIONS.values()):
        print('{}. {}'.format(index+1, values.__name__))


def exit_from_menu():
    """Exits from menu"""
    return sys.exit(0)



def run_function(name_of_function):
    """
    Runs a requested function
    :param name_of_function: str: name of function
    :return: None
    """
    run_task = FUNCTIONS.get(name_of_function)
    if run_task:
        run_task()
    else:
        print("Sorry, but I don't have this function")


def commands_help():
    """
I'm glad to see you here.
I have a few command for you:
1. run <name of function> -> performs the selected function.
2. tasks -> shows all functions which I have.
3. info <name of function> -> shows all information about selected function.
4. exit -> exit from menu.
    """
    print(commands_help.__doc__)


def show_info(name_of_function):
    """
    Prints a documentation of a function
    :param name_of_function: str: name of function
    :return: None
    """
    get_docstring(name_of_function)


DICT_FOR_COMMAND = {
    'run': run_function,
    'tasks': list_for_all_function,
    'info': show_info,
    'help': commands_help,
    'exit': exit_from_menu
}


def menu():
    """Menu of commands"""
    print('Make your choice and write one of the following command: ')
    choices = ['run <name_of_function>', 'tasks', 'info <name_of_function>', 'help', 'exit']
    for choice in choices:
        print('\t', choice)
    while True:
        user_input = input(': ')
        data = [i for i in user_input.split(" ") if i]
        key = user_input.strip()
        need_parameter = False
        if data[0] == 'run' or data[0] == 'info':
            if len(data) >= 2:
                need_parameter = True
                key = data[0]
                value = data[1]
            else:
                print('You have not entered any name of function, please write "help".')
                continue

        command = DICT_FOR_COMMAND.get(key, None)
        if command:
            if need_parameter:
                command(value)
            else:
                command()
        else:
            print("Ops, something wrong, but don't scare, you can try again.")


if __name__ == '__main__':
    menu()

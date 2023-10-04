"""Print to stdout menu, user enter to stdin option, that will be execute."""

from src.menu import get_user_choice, execute_user_choice


if __name__ == '__main__':
    opt = ''
    while opt != '4':
        opt, data_path = get_user_choice()
        execute_user_choice(opt, data_path)

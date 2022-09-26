print('Welcome user!')
summa_for_admins = int(input('Enter amount of money for admins: '))
login = str(input('Please, enter login: '))


def check_login(func):
    def checking():
        # print('hello')
        # func()
        # print('goodbye')
        if login == 'admin':
            func()
        else:
            print('Доступ запрещен!')
    return checking


@check_login
def summa_na_schete():
    print(summa_for_admins)


# summa_na_schete = check_login(summa_na_schete)
summa_na_schete()


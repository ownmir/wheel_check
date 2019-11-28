import argparse
import getpass
# import keyring


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--newpass", required=True, help="Set new password", action="store_true")
    arguments = parser.parse_args()
    return arguments


def fake_db_connection():
    # Функция, имитирующая подключение к базе данных или что-то подобное
    db_name = 'very_important_db'
    db_host = '147.237.0.71'
    passwdt = 'test'
    print('# Получаем пароль из хранилища: # passwd = keyring.get_password(systemname, username)')
    # passwd = keyring.get_password(systemname, username)

    print('Connecting to db: {}'.format(db_name))
    print('Using very secret password from vault: {}'.format(passwdt))
    print('Doing something important...')
    print('Erasing the database...')
    print('Task completed')

# Объявляем дефолтные переменные
systemname = 'important_database'
username = 'user1'

args = parse_arguments()
print('args: ', args, 'systemname: ', systemname, 'username: ', username)

# Записываем в хранилище пароль, если активирован параметр --newpass
if args.newpass:
    # Безопасно запрашиваем ввод пароля в CLI
    password = getpass.getpass(prompt="Enter secret password:")
    # Пишем полученный пароль в хранилище ключей
    print('# Пишем полученный пароль в хранилище ключей: #    keyring.set_password(systemname, username, password)')
    #try:
    #    keyring.set_password(systemname, username, password)
    #except Exception as error:
    #    print('Error: {}'.format(error))
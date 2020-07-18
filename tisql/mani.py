from getpass import getpass

def mani(conn):
    conn.setPassword(getpass('Please enter your password '))

import keyring

def keyring_pass(computer_user, database_user, password, hash_pass, mfo):
    keyring.set_password(computer_user, database_user, password.text())
##    print("key computer_user", computer_user, "key database_user",database_user)
##    print("key passw", keyring.get_password(computer_user, database_user))
    mfo.setFocus()
    password.setText('eeeeeeeeeeee')

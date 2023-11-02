login_info = {'user1': ['pw1'], 'user2': ['pw3_now', 'pw2', 'pw1']}
username = 'user1'
password_old = 'pw1'
password_new = 'pw0pw0pw0'

if login_info[username][0] == password_old:
    if len(password_new) >= 8:
        login_info[username].insert(0, password_new)
        print('Done!')
    else:
        print('Illegal new password')
else:
    print('Wrong password!')

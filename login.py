def login():
    username = input('enter the user you wish to login as  ')
    password = input('enter your password   ')
    user = find_user(username)
    if user:
        if password == user[1]:
            print(f'You have successfully logged in as {username}')
            return username
        else:
            print('Password is incorrect')
    else:
        print('username does not exist')
    return False


def create_user():
    username = input('Enter desired username  -  ')
    if not find_user(username):
        password = input('Enter your desired password  -  ')
        userdb = open(filename,'a')
        user = username + ' ' + password + '\n'
        userdb.writelines(user)
        print('User created successfully')
    else:
        print(f'username {username} already exists')


def find_user(username):
    for line in userdb:
        user = line.split()
        if user[0] == username:
            # user[0] = username  user[1] = password
            return user[0],user[1]

    return False


def display_options():
    if cur_user:
        print(f'logged in as {cur_user}  -  (l)ogout  (q)uit?')
    else:
        print('(l)ogin  (r)egister  (q)uit?')


filename = 'users.txt'
userdb = open(filename,'r')
cur_user = False

print('Welcome to terminal login system')
while True:
    display_options()
    decision = input().lower()
    if decision == 'l':
        if not cur_user:
            cur_user = login()
        else:
            cur_user = False
            print('successfully logged out')
    elif decision == 'r':
        create_user()
    elif decision == 'q':
        break
    else:
        print('Please enter a valid option')
    print()

userdb.close()
from getpass import getpass
from welcome import loading_animation, title_card
import json



class LoginSystem:

    def __init__(self, path):
        self.path = path

    def retrieve_json_data(self, path):
        with open(path, 'r') as json_file:
            data = json.load(json_file)
        return data


    def update_json_data(self, data, path):
        with open(path, 'w') as json_file:
            json.dump(data, json_file)


    def account_creation(self):
        password_test = ''
        password_visible = False
        data = self.retrieve_json_data(self.path)
        loading_animation(time=1)
        title_card('Account Creation', thickness=1)
        print()
        username = input('Enter username: ')
        loading_animation(time=1)
        while True:
            print('----- Account Creation ------')
            print()
            if not password_visible:
                print('Password hidden. Type "show" to show password.')
                print()
                password = getpass(prompt="Enter your password:" )
                if password != 'show':
                    password_test = getpass(prompt='Enter your password again: ')
            else:
                print('Password visible. Type "show" again to hide password.')
                print()
                password = input('Enter your password: ')
                if password != 'show':
                    password_test = input('Enter your password again: ')
            if password == 'show':
                loading_animation(time=1)
                password_visible = not password_visible
            elif password != password_test:
                loading_animation('Passwords didn\'t match! Try again.', time=2)
            else:
                data['users'].update({username:{'password':password, 'tokens':"500"}})
                loading_animation('Password set! Creating account...', time=2)
                break
        update_json_data(data, self.path)
        

    def account_login(self):
        password_visible = False
        logged_in = False
        create = False
        username_match = False
        data = self.retrieve_json_data(self.path)
        while not logged_in and not create:
            loading_animation(time=1)
            while not username_match:
                title_card('Login Screen', thickness=1)
                print()
                username = input('Enter your username: ')
                for name in data['users']:
                    if username == name:
                        username_match = True
                        loading_animation('username accepted...', time=1)
                        break
                else:
                    loading_animation('Sorry that username could not be located. Try again or type "create" to create an account.', time=3)

            while True:
                correct_password = data['users'][username]['password']
                print('----- Login -----')
                print()
                print('Type "reset" to reset your password.')
                if not password_visible:
                    print('Password entry is hidden by default. Type "show" and hit enter to show password.')
                    print()
                    password = getpass(prompt='Enter your password: ')
                else:
                    print('Password is visible. Type "show" again to hide it.')
                    print()
                    password = input('Enter your password: ')

                if password == 'show':
                    loading_animation(time=1)
                    password_visible = not password_visible

                elif password == 'reset':
                    loading_animation(time=1)
                    while True:
                        print('----- Password Reset -----')
                        print()
                        password = input('Enter new password: ')
                        password_test = input('Enter your new password again: ')
                        if password != password_test:
                            loading_animation("Passwords didn't match! Try again.", time=2)
                        else:
                            data['users'][username]['password'] = password
                            update_json_data(data, self.path)
                            loading_animation('Password set! Bringing you back to login...', time=2)
                            break

                elif password != correct_password:
                    loading_animation('ERROR: incorrect password...', time=1)

                elif password == correct_password:
                    loading_animation('Success! Logging in...', time=2)
                    logged_in = True
                    break
        if logged_in:
            token_count = data['users'][username]['tokens']
            return (username, int(token_count))
        else:
            loading_animation(time=1)


    def account_main(self):
        while True:
            account = input('Login or create account? (login/create): ')
            if account == 'login':
                user_info = self.account_login()
                break
            elif account == 'create':
                self.account_creation()
                user_info = self.account_login()
                break
            else:
                loading_animation('Please type "login" or "create"...', time=2)
        
        return user_info



if __name__ == '__main__':
    login = LoginSystem('../data/user-info.json')
    username, tokens = login.account_main()
    print(username, tokens)

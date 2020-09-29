# import class User from user.py
from user import User

def main():
    user1 = User('Frances', 'Ho')
    user1.build_profile(login='francesho', password='Econ$DD1',
                        pay_user='no')
    user1.print_profile()

if __name__ == '__main()__':
    main()
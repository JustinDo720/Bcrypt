from user_input_hash_bcrypt import *
import bcrypt
import unittest

'''Bcrypt's checkpw function'''
# Checking Username:
if checkpw(user_name,hash_user_name):
    print('\nUsername matched')
else:
    print('\nUsername does not match')

# Checking Password:
if checkpw(password,hash_user_password):
    print('\nPassword matched')
else:
    print('\nPassword does not match')


class TestPassUser(unittest.TestCase):

    def test_username(self):
        self.assertTrue(user_name,hash_user_name)

    def test_password(self):
        self.assertTrue(password,hash_user_password)
        print(f'\n{user_name=},\n{password=},\n{salt=}')

if __name__ == '__main__':
    unittest.main()



from app.login import *
from tests.test_login import *
import unittest


if __name__ == '__main__':
     #unittest.main()
     #print("faruk test completed")
    response = login("user", "password")
    print(response)

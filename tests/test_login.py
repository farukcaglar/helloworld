from app.login import *
import unittest

class TestLogin(unittest.TestCase):
    def test_empty_login(self):
        self.assertEqual(login(" ", " "), "Missing username or password!")

    def test_incorrect_login(self):
        self.assertEqual(login("user1","password1"), "Invalid username or password!")

    def test_correct_login(self):
        self.assertEqual(login("user","password"), "Login successful!")

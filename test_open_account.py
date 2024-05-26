import unittest
from bank import Bank

class TestOpenAccount(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_open_account_savings(self):
        self.bank.open_account(105, 125, 'savings', interest_rate=0.01)
        account = self.bank.accounts.get(125)
        self.assertIsNotNone(account, "Account should exist in the bank's records.")
        self.assertEqual(account.balance, 105, "Initial balance should be set correctly.")
        self.assertEqual(account.interest_rate, 0.01, "Interest rate should be set correctly.")

    def test_open_account_current(self):
        self.bank.open_account(200, 350, 'current', overdraft_limit=50)
        account = self.bank.accounts.get(350)
        self.assertIsNotNone(account, "Account should exist in the bank's records.")
        self.assertEqual(account.balance, 200, "Initial balance should be set correctly.")
        self.assertEqual(account.overdraft_limit, 50, "Overdraft limit should be set correctly.")

if __name__ == '__main__':
    unittest.main()

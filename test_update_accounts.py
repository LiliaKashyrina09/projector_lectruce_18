import unittest
from unittest.mock import patch
from bank import Bank

class TestUpdateAccounts(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.open_account(300, 123, 'savings', interest_rate=0.05)
        self.bank.open_account(100, 456, 'current', overdraft_limit=50)
        self.bank.accounts[456].withdraw(200)

    @patch('builtins.print')
    def test_update_accounts(self, mock_print):
        self.bank.update_accounts()

        self.assertAlmostEqual(self.bank.accounts[123].balance, 300 * 1.05, places=2)

        mock_print.assert_called_with('Account 456 is currently in overdraft.')

if __name__ == '__main__':
    unittest.main()

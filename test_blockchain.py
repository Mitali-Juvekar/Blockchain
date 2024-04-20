import unittest
import time
from blockchain import Blockchain
from block import Block
from transactions import Transactions

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_add_transaction(self):
        transaction = Transactions("Alice", "Bob", 10)
        self.blockchain.add_transaction(transaction)
        self.assertEqual(len(self.blockchain.current_transactions), 1)

    def test_mine_block(self):
        initial_length = len(self.blockchain.chain)
        self.blockchain.mine_block()
        self.assertEqual(len(self.blockchain.chain), initial_length + 1)

    def test_validate_chain(self):
        # Test case: Valid chain
        self.assertTrue(self.blockchain.validate_chain())

        # Test case: Modify a block to invalidate the chain
        modified_block = self.blockchain.chain[1]
        modified_block.transactions = [Transactions("Mallory", "Eve", 100)]
        self.assertFalse(self.blockchain.validate_chain())

if __name__ == "__main__":
    unittest.main()

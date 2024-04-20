import time
from transactions import Transactions 
from block import Block 
class Blockchain:
    def __init__(self):
        self.chain = [] #to store complete blocks
        self.current_transactions = []
        self.create_genesis_block()

# creating first ever block, initializing index and previous hash to 0
    def create_genesis_block(self):
        genesis_transactions = [Transactions("Satoshi", "HalFinney", 100)]
        timestamp = time.time()
        genesis_block = Block(index = 0, previous_hash = "0", transactions=genesis_transactions, timestamp=timestamp)
        self.chain.append(genesis_block)

    def add_transaction(self, transaction):
        # Add a transaction to the list of current transactions
        self.current_transactions.append(transaction)

    def mine_block(self):
        # creating new block
        last_block = self.chain[-1]
        index = last_block.index + 1
        previous_hash = last_block.hash
        timestamp = time.time() 
        new_block = Block(index, previous_hash, self.current_transactions, timestamp)
        self.chain.append(new_block)

        # reseting current transactions
        self.current_transactions = []

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            # checking if the hash of the current block is valid
            if current_block.hash != current_block.calculate_hash():
                return False
            # checks if the previous hash of the current block matches the hash of the previous block
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


        
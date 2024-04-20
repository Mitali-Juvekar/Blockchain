class Blockchain:
    def __init__(self):
        self.chain = [] #to store complete blocks
        self.current_transactions = []
        self.genesis_block()

# creating first ever block, initializing index and previous hash to 0
    def genesis_block(self):
        genesis_transactions = [Transaction("Satoshi", "HalFinney", 100)]
        timestamp = time.time()
        genesis_block = Block(index = 0, previous_hash = "0", transactions=genesis_transactions, timestamp=timestamp)
        self.chain.append(genesis_block)
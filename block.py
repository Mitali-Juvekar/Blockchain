import time

class Block:
    def __init__(self, index, previous_hash, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        #concatenate the attributes into a single string
        string_val = str(self.index) + str(self.previous_hash) + str(self.transactions) + str(self.timestamp)
        hash_val = 0
        #every character in the string will be converted into its ascii value
        for char in string_val:
            hash_val += ord(char)
        return hash_val
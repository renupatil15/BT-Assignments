import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        text = str(self.data) + str(self.previous_hash) + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(text.encode()).hexdigest()

    def mine_block(self, difficulty):
        print("\n⛏️ Mining started...")

        target = "0" * difficulty

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(" Block Mined!")
        print("Hash:", self.hash)
        print("Nonce:", self.nonce)


# ---------------- MAIN PROGRAM ----------------
difficulty = 4

block1 = Block("Alice pays Bob 10 BTC", "0")

block1.mine_block(difficulty)
import hashlib
import time

# ---------------------- Transaction Class ----------------------
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __str__(self):
        return f"{self.sender} -> {self.receiver} : {self.amount}"


# ---------------------- Block Class ----------------------
class Block:
    def __init__(self, transactions, previous_hash):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.timestamp) + str(self.transactions) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()


# ---------------------- Blockchain Class ----------------------
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block([], "0")
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        previous_hash = self.get_latest_block().hash
        new_block = Block(transactions, previous_hash)
        self.chain.append(new_block)


# ---------------------- Wallet Class ----------------------
class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


# ---------------------- Transaction Function ----------------------
def make_transaction(sender_wallet, receiver_wallet, amount, blockchain):

    print("\nTransaction Request:")
    print(f"{sender_wallet.owner} wants to send {amount} coins to {receiver_wallet.owner}")

    # Double Spending Check
    if sender_wallet.balance < amount:
        print(" Transaction Failed: Double Spending Detected!")
        print("Sender does not have enough balance.")
        return

    # Deduct and Add Balance
    sender_wallet.balance -= amount
    receiver_wallet.balance += amount

    # Create Transaction
    tx = Transaction(sender_wallet.owner, receiver_wallet.owner, amount)

    # Add transaction to blockchain
    blockchain.add_block([tx])

    print(" Transaction Successful")
    print(tx)


# ---------------------- Main Program ----------------------
blockchain = Blockchain()

# Create wallets
wallet_A = Wallet("Alice", 100)
wallet_B = Wallet("Bob", 50)

print("Initial Balances:")
print("Alice:", wallet_A.balance)
print("Bob:", wallet_B.balance)

# First Transaction
make_transaction(wallet_A, wallet_B, 40, blockchain)

# Attempt Double Spending
make_transaction(wallet_A, wallet_B, 70, blockchain)

print("\nFinal Balances:")
print("Alice:", wallet_A.balance)
print("Bob:", wallet_B.balance)

# Display Blockchain
print("\nBlockchain Data:")
for i, block in enumerate(blockchain.chain):
    print(f"\nBlock {i}")
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)
    print("Transactions:", block.transactions)
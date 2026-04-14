import hashlib

# Function to compute hash
def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Function to compute Merkle Root
def merkle_root(transactions):

    # Step 1: Hash all transactions
    hashes = [hash_data(tx) for tx in transactions]

    print("Initial Transaction Hashes:")
    for h in hashes:
        print(h)

    # Step 2: Build Merkle Tree
    while len(hashes) > 1:

        # If odd → duplicate last
        if len(hashes) % 2 != 0:
            hashes.append(hashes[-1])

        new_hashes = []

        # Pair and hash
        for i in range(0, len(hashes), 2):
            combined = hashes[i] + hashes[i + 1]
            new_hash = hash_data(combined)
            new_hashes.append(new_hash)

        hashes = new_hashes

        print("\nNext Level Hashes:")
        for h in hashes:
            print(h)

    return hashes[0]


# Sample transactions
transactions = [
    "Alice pays Bob 10 BTC",
    "Bob pays Charlie 5 BTC",
    "Charlie pays Dave 2 BTC",
    "Dave pays Eve 1 BTC"
]

# Compute Merkle Root
root = merkle_root(transactions)

print("\n Merkle Root:", root)
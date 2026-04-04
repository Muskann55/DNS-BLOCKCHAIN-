import hashlib
import time
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.nodes = set()  # Decentralized nodes for DDoS resistance
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = {
            'index': 0,
            'timestamp': time.time(),
            'transactions': [],
            'previous_hash': '0',
            'hash': self.hash_block({'index': 0, 'timestamp': time.time(), 'transactions': [], 'previous_hash': '0'})
        }
        self.chain.append(genesis)

    def hash_block(self, block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)
        self.mine_block()  # Simulate mining (in real Ethereum, this costs gas)

    def mine_block(self):
        if not self.pending_transactions:
            return
        last_block = self.chain[-1]
        new_block = {
            'index': len(self.chain),
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'previous_hash': last_block['hash'],
            'hash': ''
        }
        new_block['hash'] = self.hash_block(new_block)
        self.chain.append(new_block)
        self.pending_transactions = []
        print(f"Block {new_block['index']} mined with {len(new_block['transactions'])} transactions.")

    def get_transaction(self, domain):
        for block in reversed(self.chain):
            for tx in block['transactions']:
                if tx.get('domain') == domain:
                    return tx
        return None

    def audit_trail(self, domain):
        trail = []
        for block in self.chain:
            for tx in block['transactions']:
                if tx.get('domain') == domain:
                    trail.append({'block': block['index'], 'transaction': tx})
        return trail

# Global blockchain instance
blockchain = Blockchain()
from dataclasses import dataclass
from time import time

class Blockchain:
    
    @dataclass
    class Block:
        index: str
        timestamp: float
        transactions: list
        proof: int
        previousHash: int

    class GenesisBlock(Block):
        def __post_init__(self) -> None:
            self.index = 0

    def __init__(self):
        self.chain = []
        self.transactions = []

    def __len__(self) -> int:
        return len(self.chain)
    
    def add_block(self, proof:int, previousHash:str=None):

        if len(self) == 0:
            cls = self.GenesisBlock

            def gph():
                return None
        else:
            cls = self.Block

            def gph():
                return hash(self.chain[-1])
            
        self.chain.append(cls(index=len(self), timestamp=time(), transactions=self.transactions, proof=proof, previousHash=previousHash or gph()))
        self.transactions = []
        return cls
    
    def new_transaction(self, sender:str, recipient:str, amount:int):
        self.transactions.append({"sender":sender, "recipient":recipient, "amount": amount})

        return self.last_block["index"] + 1


    @property
    def last_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, last_proof:int) -> int:
        
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains 4 leading zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
         """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        
        return proof

    @staticmethod
    def valid_proof(last_proof:int, proof:int) -> bool:
        
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        """
        
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hash(guess)
        return guess_hash[:4] == "0000"
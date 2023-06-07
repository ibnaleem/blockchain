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
        
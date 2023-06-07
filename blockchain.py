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
    
    
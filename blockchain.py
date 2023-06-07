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
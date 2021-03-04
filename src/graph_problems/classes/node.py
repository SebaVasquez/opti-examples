import numpy as np

class Node:
    def __init__(self, id, pos):
        self.id = str(id)
        self.pos = pos
    
    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id
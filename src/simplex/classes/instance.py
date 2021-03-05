from numpy import matrix, array

class SimplexInstance:
    def __init__(self, args):
        self.A = matrix(args['A'])
        self.b = array(args['b'])
        self.c = array(args['c'])
        self.IBase = array(args['IBase'])

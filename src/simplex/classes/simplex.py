from numpy.linalg import inv
from numpy import argmin, array, squeeze, round, infty

class Simplex:
    def __init__(self, instance):
        self.A = instance.A
        self.b = instance.b
        self.c = instance.c
        self.B = instance.IBase
        self.n = instance.A[0].size
        self.A_B_inverse = None

    @property
    def solution(self):
        solution_B = list(self._to_vector((self.A_B_inverse @ self.b)))
        solution = [0 for i in range(self.n)]
        for idx in range(self.n):
            if idx in self.B:
                solution[idx] = solution_B.pop(0)

        if all([i >= 0 for i in solution]):
            status = 'Feasible'
        else: 
            status = 'Infeasible'

        solution = array(solution)
        cost = solution @ self.c

        return solution, status, cost
    
    @property
    def N(self):
        return [i for i in range(self.n) if i not in self.B]

    @property
    def c_B(self):
        return self.c[self.B]

    @property
    def c_N(self):
        return self.c[self.N]

    @property
    def A_B(self):
        return self.A[:, self.B]

    @property
    def A_N(self):
        return self.A[:, self.N]

    @property
    def reduced_costs(self):
        return self._to_vector((self.c_N - self.c_B @ self.A_B_inverse @ self.A_N))

    def _get_outgoing_idx(self, incoming_index):
        b_bar = self._to_vector(self.A_B_inverse @ self.b)
        A_bar = self._to_vector(self.A_B_inverse @ self.A[:, incoming_index])
        radios = [i if i >= 0 else infty for i in b_bar / A_bar]
        
        try: 
            return self.B[argmin(radios)]
        except:
            return None
    
    def _get_incoming_idx(self, reduced_costs):
        for idx, i in enumerate(reduced_costs):
            if i < 0:
                return self.N[idx]
    
    def _set_A_B_inverse(self):
        self.A_B_inverse = inv(self.A_B)
        return self.A_B_inverse

    def _get_new_Base(self, Base, incoming_idx, outgoing_idx):
        new_B = Base
        new_B.remove(outgoing_idx)
        new_B.append(incoming_idx)
        return new_B
    
    def _set_B(self, new_B):
        self.B = new_B

    def _check_optimality(self, reduced_costs):
        if all([i >= 0 for i in reduced_costs]):
            return True
        else:
            return False
    
    def _check_multiplicity(self, reduced_costs):
        if any([i == 0 for i in reduced_costs]):
            return True
        else:
            return False
    
    def _to_vector(self, matrix):
        return squeeze(array(matrix))
    
    def run(self):
        iter = 1
        optimal = False
        while iter <= 20:
            print('Executing iter', iter)
            print('\tUsing B =', self.B)
            A_B_inverse = self._set_A_B_inverse()
            print('\tComputing new solution...')
            solution, status, cost = self.solution
            print('\t\tActual solution:', round(solution, 2))
            print('\t\tSolution status:', status)
            print('\t\tObjective value:', cost)
            
            print('\tComputing reduced costs...')
            reduced_costs = self.reduced_costs
            print('\t\tReduced costs =', reduced_costs)
            
            if self._check_optimality(reduced_costs):
                if self._check_multiplicity(reduced_costs):
                    status += '-multiple_solutions'
                    print('\tMultiple optimal solutions found!')
                    print('\tAn optimal solution:', solution)
                else:
                    print('\tUnique optimal solution found!')
                    print('\tOptimal solution:', solution)
                
                print('\tOptimal objetive value:', cost)
                optimal = True
                break
            
            print('\t\tChecking incoming variable...')
            incoming_idx = self._get_incoming_idx(reduced_costs)
            print('\t\t\tIncoming variable index:', incoming_idx)

            print('\t\tChecking outgoing variable...')
            outgoing_idx = self._get_outgoing_idx(incoming_idx)
            print('\t\t\tOutgoing variable index:', outgoing_idx)

            print('\tBuilding new base...')
            new_B = self._get_new_Base(self.B, incoming_idx, outgoing_idx)
            self._set_B(new_B)
            print('\t\tNew base: {}\n'.format(self.B))
            iter += 1
        
        return iter, optimal
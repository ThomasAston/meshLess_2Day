'''
PyMFS solver module
'''

'''
To-do list:

- Shape function generation
- Integration point generation
- C matrix
- B matrix
- K matrix
- solve system
'''

import numpy as np
from .input_data import*
from .system_variables import*
import pickle
import time

class solve:
    def __init__(self, job_ID):
        
        start = time.time()
        self.job_ID = job_ID
        self.input_data = input_data(job_ID)
        self.system_variables = system_variables(self.input_data)
        self.K = self.system_variables.K
        self.f = self.system_variables.f
        self.delete = self.system_variables.delete[:]
        self.q = self.solve_system()
        self.output_file()
                
        end = time.time()
        time_taken = end-start
        print('Time elapsed (solver): ',time_taken)

    def solve_system(self):
        q = np.linalg.solve(self.K, self.f)
        q = q.tolist()
        for index in self.delete:
            q.insert(index,0)
        q = np.array(q)

        return q

    def output_file(self):

        return






        



# Atividade de Código distribuído
# Aluno: Stefano Calheiros Stringhini R.A.: 2312123

import time
import numpy as np
from multiprocessing import Pool, cpu_count


def multiply_row(args):
    A_row, B = args
    return np.dot(A_row, B)


def sequential_matrix_multiply(A, B):
    start = time.time()
    C = np.dot(A, B)
    end = time.time()
    return C, (end - start) * 1000


def parallel_matrix_multiply(A, B):
    start = time.time()
    with Pool(cpu_count()) as p:
        C = p.map(multiply_row, [(A[i], B) for i in range(len(A))])
    end = time.time()
    return np.array(C), (end - start) * 1000

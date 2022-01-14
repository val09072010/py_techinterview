from collections import Counter
from math import factorial, prod
import multiprocessing as mp

MOD = 1000000007
N = 1000000


def process_input() -> list:
    """
    Script expects the following input:
        9
        Average 1
        Premins 9
        Costs 2
        Ordering 3
        Books 3
        ABCs 2
        Mulitples 5
        Teleport 2
        P=NP 9
    """
    n = int(input().strip())
    res = []
    for _ in range(n):
        task_name, rate = input().strip().split(' ')
        if task_name and rate:
            res.append(rate)
    return res


def calc_reference_solution(arr: list) -> int:
    """Reference solution for the task"""
    counter = Counter(arr)
    k_counter = Counter(counter.values())
    prd = 1
    for k, v in k_counter.items():
        prd *= factorial(k)**v
    return prd % MOD
    
   
def calc(arr: list) -> int:
    """Solution with multiprocessing. Calculations divided into several chunks that will be processed in parallel"""
    counter = Counter(arr)
    k_counter = Counter(counter.values())
    
    k_keys = list(k_counter.keys())
    cpus = mp.cpu_count() // 2
    
    chunk = (len(k_keys) // cpus) + (len(k_keys) % cpus)
    
    res = []
    with mp.Pool(cpus) as pool:
        res = pool.map(unit, [(k_counter, k_keys[i*chunk:(i*chunk + chunk)]) for i in range(cpus)])
    return prod(res) % MOD


def unit(arg: tuple) -> int:
    """Calculation unit. Implements calculation of individual chunk"""
    prd = 1
    keys = arg[1]
    k_counter = arg[0]
    for k in keys:
        prd *= factorial(k)**k_counter[k]
    return prd


def main():
    input_data = process_input()
    if not input_data:
        return
    print(calc(input_data))
    
    
if __name__ == '__main__':
    main()

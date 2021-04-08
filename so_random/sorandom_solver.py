import time
import random
import os
import tqdm
from multiprocessing import Pool
import math
from functools import partial

class Generator():
    def __init__(self, seed):
        self.seed = seed
        assert(len(str(self.seed)) == 8)

    def getNum(self):
        self.seed = int(str(self.seed**2).rjust(16, "0")[4:12])
        return self.seed

# Somewhat inspired by this single-threaded
# implementation of a divisor generator
# https://stackoverflow.com/a/171779
def concurrentDivisorGeneratorIteration(n, c):
    res = []
    for i in c:
        if n % i == 0:
            res.append(i)
            if i*i != n:
                res.append(n / i)
    return res

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def concurrentDivisorGenerator(n, pool=None):
    if pool == None:
        pool = Pool()
    
    task_range = chunks(range(1, int(math.sqrt(n) + 1)), int(math.sqrt(n) / 64))
    func = partial(concurrentDivisorGeneratorIteration, n)
    divisors = tqdm.tqdm(pool.imap_unordered(func, task_range), total=len(task_range))

    divisors = [ent for sublist in divisors for ent in sublist]
    
    return divisors

def reducer(possible, target, iterations):
    res = []
    for p in possible:
        a = Generator(p[0])
        b = Generator(p[1])

        for i in range(iterations):
            a.getNum()
            b.getNum()

        if a.getNum() * b.getNum() == target:
            res.append(p)
    return res

def print_results(generator, iteration):
    a = Generator(generator[0])
    b = Generator(generator[1])

    for i in range(3):
        if i < iteration:
            a.getNum()
            b.getNum()
            i -= 1
        else:
            print(f'[{i}] {a.getNum() * b.getNum()}')

possible = []
iteration = 0
pool = Pool()
while True:
    target = int(input('gief number '))

    if len(possible) == 0:
        for divisor in concurrentDivisorGenerator(target,pool):
            a = divisor
            b = target // divisor
            if len(str(a)) == 8 and len(str(b)) == 8:
                possible.append((a, b))
    else:
        possible = reducer(possible, target, iteration)
        iteration += 1
    
    print(f'Candidates: {len(possible)}')

    if len(possible) == 1:
        print("Success! Enter the following values: ")
        print_results(possible[0], iteration)
        exit()

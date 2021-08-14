import random
import multiprocessing

if __name__ == '__main__':

    def compute(n):
        return sum([random.randint(1,100) for i in range(1000000)])
    pool = multiprocessing.Pool(processes=8)
    results = pool.map(compute, range(8))
    
    print("Results: %s" % results)
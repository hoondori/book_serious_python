from memory_profiler import profile 
class Point(object):
    def __init__(self, x):
        self.x = x 

@profile
def main():
    p = [Point(42) for i in range(100000)]

if __name__ == "__main__":
    main()
  
